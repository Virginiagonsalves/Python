'''Write a program that searches a directory and all of its subdirectories, recursively, and returns a list
of complete paths for all files with a given suffix.'''
import os
def find_files_with_suffix(directory,suffix):
    files_with_suffix=[]
    #Traverse the directory and its subdirectories recursively
    for root, dirs, files in os.walk(directory):
        for file in files:
            #Check if the file has the desired suffix
            if file.endswith(suffix):
                #Append the complete path of the file to the list
                files_with_suffix.append(os.path.join(root, file))
    return files_with_suffix
def main():
    directory=input("enter the directory path:")
    suffix=input("enter the suffix to search for(e.g.,txt,.jpg):")
    #Find files with the given suffix in the directory
    files_with_suffix=find_files_with_suffix(directory,suffix)
    if files_with_suffix:
        print("Files found with the suffix '{}' in directory '{}' and its subdirectories:".format(suffix, directory))
        for file_path in files_with_suffix:
            print(file_path)
    else:
        print("No files found with the suffix '{}' in directory '{}' and its subdirectories.".format(suffix, directory))
if __name__=="__main__":
    main()
