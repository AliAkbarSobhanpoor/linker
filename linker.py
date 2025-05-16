import os
import glob
import itertools
from duplicate_finder import ByteDuplicateFinder

class Linker:
    """
        Abstract base class for create  duplicate files.
    """
    def __init__(self, path):
        self.path = path  # This will call the setter

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        if not os.path.isdir(value):
            raise ValueError(f"Invalid directory: '{value}'")
        self._path = value

    def get_all_dir_files(self):
        # list of all directories.dosent return a list . insted return an iterator
        dirs = glob.iglob(f"{self._path}/**/*", recursive=True)
        return dirs

    def duplicate_checker(self):
        files = [file for file in self.get_all_dir_files() if os.path.isfile(file)] # only get the files.
        for file_1, file_2 in itertools.combinations(files, 2):
            d = ByteDuplicateFinder(file_1=file_1, file_2=file_2)
            is_duplicate = d.base_compare_file()
            if is_duplicate:
                print(f"the file {file_1}, {file_2} are duplicate")

            # here we need to do some works for create and stack and then make symlink for newest one file
            # to oldest one . and also remove the main file. 

if __name__ == "__main__":
    dir = input("pls enter a dir: ")
    linker = Linker(dir)
    linker.duplicate_checker()