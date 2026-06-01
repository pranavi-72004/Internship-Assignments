import hashlib
import os

def calculate_hash(file_path):

    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:

        while True:
            data = file.read(4096)

            if not data:
                break

            sha256.update(data)

    return sha256.hexdigest()

file_path = input("Enter File Path: ")

original_hash = calculate_hash(file_path)

print("\nOriginal Hash:")
print(original_hash)

input("\nModify file if required and press Enter...")

new_hash = calculate_hash(file_path)

print("\nNew Hash:")
print(new_hash)

if original_hash == new_hash:
    print("\nFile Integrity Maintained")
else:
    print("\nWARNING: File Modified")