import os
import re

def zero_pad_filenames(directory):
    pattern = re.compile(r'^(\d+)-(.*)')
    files = os.listdir(directory)

    numbers = []

    # First pass: collect all leading numbers
    for filename in files:
        match = pattern.match(filename)
        if match:
            number = int(match.group(1))
            numbers.append(number)

    if not numbers:
        print("No matching files found.")
        return

    max_digits = len(str(max(numbers))) + 1

    renamed = 0
    for filename in files:
        match = pattern.match(filename)
        if match:
            number, rest = match.groups()
            padded_number = number.zfill(max_digits)
            new_filename = f"{padded_number}-{rest}"

            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)

            if old_path != new_path:
                os.rename(old_path, new_path)
                renamed += 1
                print(f"Renamed: {filename} → {new_filename}")

    print(f"\nDone. {renamed} files renamed.\nPadding used: {max_digits} digits.")

# Replace with your target folder path
target_directory = "./"
zero_pad_filenames(target_directory)