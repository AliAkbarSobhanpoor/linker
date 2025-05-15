from duplicate_finder import SHADuplicateFinder, ByteDuplicateFinder
import os

def main():
    """Main function to find duplicate files."""
    file1 = input("Please enter the first file name: ")
    file2 = input("Please enter the second file name: ")
    
    duplicate_1 = SHADuplicateFinder(file1, file2)
    duplicate_1.compare()

    print("-"*20) 

    duplicate_2 = ByteDuplicateFinder(file1, file2)
    duplicate_2.compare()

main()