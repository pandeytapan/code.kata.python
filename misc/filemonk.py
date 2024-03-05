import os
from faker import Faker
import random

TWO_KIB_IN_BYTES = 2048
# Ask for the number of folders to create
num_folders = int(input("How many folders you want to create: "))

# Ask for the disk size to fill in bytes
disk_size = int(input("Enter the size of the disk to fill (in bytes): "))

if disk_size < TWO_KIB_IN_BYTES:
    print("Disk size should be atleast 2KiB")
    exit(1)

# Calculate the number of files to create in each folder
main_folder = "root"
total_files = disk_size // TWO_KIB_IN_BYTES
files_per_folder, extra_files = divmod(total_files, num_folders)

if not files_per_folder:
    print("Disk size is too small to create even one file in each folder")
    exit(1)

os.makedirs(main_folder, exist_ok=True)

fake = Faker()

for i in range(num_folders):
    # Generate a random folder name
    folder_name = fake.company().replace(" ", "_")

    folder_path = os.path.join(main_folder, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    print(f"Created folder: {folder_path}")

    print(f"Creating files inside folder {folder_path}")

    for j in range(files_per_folder):
        file_name = fake.file_name()
        file_path = os.path.join(folder_path, file_name)

        # limit the file size
        with open(file_path, mode="w") as f:
            textdata = fake.text(
                max_nb_chars=random.randint(100, TWO_KIB_IN_BYTES))
            f.write(textdata)

        print(f"Created file: {file_path}")

for j in range(extra_files):
    file_name = fake.file_name()
    file_path = os.path.join(folder_path, file_name)

    # limit the file size
    with open(file_path, mode="w") as f:
        textdata = fake.text(max_nb_chars=TWO_KIB_IN_BYTES)
        f.write(textdata)

    print(f"Created file: {file_path}")
