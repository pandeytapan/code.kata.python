#!/usr/bin/python3

import os
from faker import Faker

TWO_KIB_IN_BYTES = 2048
# Ask for the number of folders to create
num_folders = int(input("How many folders you want to create: "))

# Ask for the disk size to fill in bytes
disk_size = int(input("Enter the size of the disk to fill (in bytes): "))

main_folder = "root"

os.makedirs(main_folder, exist_ok=True)

fake = Faker()

for i in range(num_folders):
    # Generate a random folder name
    folder_name = fake.company().replace(" ", "_")

    # Make the complete path from root till the folder name and create the
    # folder
    folder_path = os.path.join(main_folder, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    print(f"Created folder: {folder_path}")

    print(f"Creating files inside folder {folder_path}")

    total_folder_size_in_bytes = 0
    # Keep track of number of files inside the folder
    max_files_in_a_folder = disk_size // (num_folders * TWO_KIB_IN_BYTES)

    # Create files till the disk dize is remaining and the number of files
    # remaining
    while total_folder_size_in_bytes < disk_size and max_files_in_a_folder:
        file_name = fake.file_name()
        file_path = os.path.join(folder_path, file_name)

        # limit the file size 
        file_size = min((disk_size - total_folder_size_in_bytes) // max_files_in_a_folder, 2048)
        # Now create the file in the given path and fill atleast 2KiB of
        # random data
        with open(file_path, mode="w") as f:
            paragraphs = [fake.paragraph() for _ in range(file_size // len(fake.paragraph()))]
            f.write("\n".join(paragraphs))

        print(f"Created file: {file_path}")

        total_folder_size_in_bytes += os.path.getsize(file_path)
        max_files_in_a_folder -= 1
