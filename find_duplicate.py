import hashlib
import os
import sys


def calculate_file_hash(file_name):
    """calculate the SHA-256 hash of the file."""
    hash_obj = hashlib.sha256()
    try:
        with open(file_name, 'rb') as file:
            while chunk := file.read(8192):
                hash_obj.update(chunk)
            return hash_obj.hexdigest()

    except FileNotFoundError:
        print(f"Error: file '{file_name}' not found.")
        return None
    except PermissionError:
        print(f"Error: permission denied for file '{file_name}'.")
        return None
    except Exception as e:
        print(f"Error while proccesing file {file_name}: {e}")
        return None


def compare_files(file1, file2):
    """compare 2 files using their SHA-256 hashes."""
    file_1_size = os.path.getsize(file1)
    file_2_size = os.path.getsize(file2) 
    print(f'Comparing Files:')
    print(f"file 1: {file1} ({file_1_size} bytes)")
    print(f"file 2: {file2} ({file_2_size} bytes)")

    if file_1_size != file_2_size:
        print("Files are different in size. so files cant be same")
        return False
    
    print("Files have the same size. Calculating hashes please wait...")

    # calculate the hashes 
    hash1 = calculate_file_hash(file1)
    hash2 = calculate_file_hash(file2)

    if hash1 is None or hash2 is None:
        print("Hash calculation failed.")
        return None
    
    if hash1 == hash2:
        print("files are identical.")
        return True
    else:
        print("Files are not identical.")
        return False
    

def main():
    """Main function to find duplicate files."""
    file1 = input("pls enter first file name: ")
    file2 = input("pls enter second file name: ")

    if not os.path.isfile(file1):
        print("File does not exist.")
        return 
    if not os.path.isfile(file2):
        print("File does not exist.")
        return
    
    compare_files(file1, file2) # compare 2 files using their SHA-256 hashes


if __name__ == "__main__":
    main()