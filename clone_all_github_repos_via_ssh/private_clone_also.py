import os
import subprocess
import requests

def start_ssh_agent_and_add_key():
    print("Starting ssh-agent and adding your key.")
    agent_output = subprocess.check_output(["ssh-agent", "-s"], universal_newlines=True)
    for line in agent_output.splitlines():
        if line.startswith("SSH_AUTH_SOCK"):
            os.environ["SSH_AUTH_SOCK"] = line.split(";")[0].split("=")[1]
        elif line.startswith("SSH_AGENT_PID"):
            os.environ["SSH_AGENT_PID"] = line.split("=")[1].split(";")[0]

    subprocess.run(["ssh-add", os.path.expanduser("~/.ssh/id_ed25519")], check=True)

def get_all_repos(token):
    headers = {
        "Authorization": f"token {token}",
        "User-Agent": "Mozilla/5.0"
    }
    repos, page = [], 1
    while True:
        url = f"https://api.github.com/user/repos?per_page=100&page={page}&affiliation=owner"
        r = requests.get(url, headers=headers)
        if r.status_code != 200:
            raise Exception(f"GitHub API error: {r.status_code} {r.text}")
        data = r.json()
        if not data:
            break
        repos.extend(data)
        page += 1
    return repos

def clone_repo(ssh_url, clone_all, clone_dir):
    if clone_all or input(f"Clone {ssh_url}? (Yes/No): ").strip().lower().startswith("y"):
        print(f"Cloning {ssh_url}")
        subprocess.run(["git", "clone", ssh_url], cwd=clone_dir)
        print("Done")
    print("\n" + "_" * 66 + "\n")

def main():
    github_token = input("Enter GitHub Personal Access Token (with repo access): ").strip()
    clone_dir = input("Clone Folder Directory (default: ./cloned_repos): ").strip() or "./cloned_repos"
    os.makedirs(clone_dir, exist_ok=True)

    clone_all = input("Clone all Repos (Yes/No): ").strip().lower().startswith("y")

    start_ssh_agent_and_add_key()
    repos = get_all_repos(github_token)
    print(f"Found {len(repos)} repos (including private ones if token has permission)")

    for repo in repos:
        clone_repo(repo["ssh_url"], clone_all, clone_dir)

if __name__ == "__main__":
    main()