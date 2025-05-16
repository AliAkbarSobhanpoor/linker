import os # for system operations
import hashlib # for check duplication
from abc import ABC, abstractmethod


# need a function or class that get all the files. in the directory. and send them to this class . 
# then compare them and then create links. 


# todo: create a file duplicator finder. 
# todo: create cli for fast colaboration.
# todo: has django-app structure in your mind.


class DuplicateFinder(ABC):
    """
    Class to find duplicate files.
    2 methods are provided in 2 different classes.
        1. Compare files using SHA-256 hashes -> user SHADuplicateFinder
        2. Compare files byte by byte. -> user ByteDuplicateFinder
    """
    def __init__(self, file_1, file_2):
        if not os.path.exists(file_1):
            raise FileNotFoundError(f"{file_1} does not exist.")
        else:
            self.file_1 = file_1
            self.file_1_size = os.path.getsize(file_1)
       
        if not os.path.exists(file_2):
            raise FileNotFoundError(f"{file_2} does not exist.")
        else:
            self.file_2 = file_2
            self.file_2_size = os.path.getsize(file_2)

    @abstractmethod
    def compare(self):
        """
            Compare the two files for duplication.
        """
        pass
    
    
    def base_compare_file(self):
        """
            only compare the basics like size. and if it matches give let standard compare function to do other things.
        """
        if self.file_1_size != self.file_2_size:
            print("Files are of different sizes.") # todo: remove this message.
            return False
        print("some other data")
        print("some other data")
        print("some other data")
        print("some data.")

        print("some other data")
        print("Files have the same size. Calculating hashes please wait...") # todo: remove this message.
        return self.compare()


class ByteDuplicateFinder(DuplicateFinder):
    """
        compare files byte by byte
        - this is good for smaller file
        - its slower than byte sha-256 compare.
    """
    
    def compare(self):
        """Compare two files byte by byte."""
        try:
            with open(self.file_1, 'rb') as f1, open(self.file_2, 'rb') as f2:
                while True:
                    bytes1 = f1.read(8192)
                    bytes2 = f2.read(8192)
                    if bytes1 != bytes2:
                        print("Files are not identical.") # todo: remove this message.
                        return False
                    if not bytes1:
                        break

            print("Files are identical.") # todo: remove this message.
            return True
        except FileNotFoundError:
            print(f"Error: file '{self.file_1}' or '{self.file_2}' not found.") # todo: remove this message.
            return None
        except PermissionError:
            print(f"Error: permission denied for file '{self.file_1}' or '{self.file_2}'.") # todo: remove this message.
            return None
        except Exception as e:
            print(f"Error while processing files: {e}") # todo: remove this message.
            return None


class SHADuplicateFinder(DuplicateFinder):
    """
        compare files with the SHA-256 hashing algorithm.
        - this is good for big files
        - its faster than byte byte compare.
    """


    @staticmethod
    def calculate_file_hash(file_name):
        """calculate the SHA-256 hash of the file."""
        hash_obj = hashlib.sha256()
        try:
            with open(file_name, 'rb') as file:
                while chunk := file.read(8192):
                    hash_obj.update(chunk)
                return hash_obj.hexdigest()

        except FileNotFoundError:
            print(f"Error: file '{file_name}' not found.") # todo: remove this message.
            return None
        except PermissionError:
            print(f"Error: permission denied for file '{file_name}'.") # todo: remove this message.
            return None
        except Exception as e:
            print(f"Error while proccesing file {file_name}: {e}") # todo: remove this message.
            return None
    
    def compare(self):
        """Compare two files using their SHA-256 hashes."""
        hash1 = self.calculate_file_hash(self.file_1)
        hash2 = self.calculate_file_hash(self.file_2)
        if hash1 is None or hash2 is None:
            print("Error calculating hashes.") # todo: remove this message.
            return False
        if hash1 != hash2:
            print("Files are not identical.") # todo: remove this message.
            return False
        print("Files are identical.") # todo: remove this message.
        return True
