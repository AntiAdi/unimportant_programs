# 🔧 GitHub Repo Cloner (SSH-Based)

This Python script clones **all public repositories** of any GitHub user using the **SSH protocol**. It supports both:

- ✅ **Batch mode**: Automatically clones all repositories
- ✅ **Interactive mode**: Asks before cloning each repository

---

## 🚀 Features

- 🔐 Automatically starts `ssh-agent` and adds your SSH key (`~/.ssh/id_ed25519`)
- 🌐 Fetches repositories via GitHub REST API (paginated)
- 📁 Clones repositories into a specified or default folder
- 💬 Handles errors and malformed input gracefully

---

## 🧠 Requirements

- Python 3.7+
- Git installed and available in your system PATH
- SSH key (`id_ed25519`) added to your GitHub account
- Python `requests` module  
  Install via:

  ```bash
  pip install requests


## How to use

- Use the public version to clone only public repos. Only need the ssh running in this case.
- To make this script work for private repos as well, use the private version :
	1. Generate a GitHub PAT:
	  - Go to https://github.com/settings/tokens
	  - Scopes: repo (for full control of private repos).
	2. Paste it when the script asks.
	3. Make sure your ~/.ssh/id_ed25519.pub key is added to your GitHub account.