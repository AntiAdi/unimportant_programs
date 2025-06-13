import os
import subprocess

# List all .txt files in the current directory
txt_files = [f for f in os.listdir() if f.startswith("quotes") and f.endswith(".txt")]

for txt_file in txt_files:
    # Output folder = filename without .txt + "out"
    base_name = os.path.splitext(txt_file)[0]
    output_folder = base_name + "out"

    print(f"Generating: {txt_file} --> {output_folder}/")

    # Run generate.py with output folder and txt file as arguments
    subprocess.run(["python3", "generate.py", output_folder, txt_file], check=True)

print("\n✅ All batches completed.")