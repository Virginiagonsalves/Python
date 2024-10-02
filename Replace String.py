'''Program to implement search and replace multiple occurrences of a given substring in
the main string in a list.'''
def search_replace_strings(strings, search_str, replace_str):
    #Function to search and replace multiple occurrences of a substring in a list of strings
    replaced_strings=[]
    for string in strings:
        replaced_string = string.replace(search_str, replace_str)
        replaced_strings.append(replaced_string)
    return replaced_strings
def main():
    # Input list of strings
    strings=[]
    n=int(input("Enter the number of strings: "))
    for i in range(n):
        string=input("Enter string" + str(i+1) + ":")
        strings.append(string)

    # Input search and replace strings
    search_str = input("Enter the substring to search: ")
    replace_str = input("Enter the substring to replace with: ")

    # Search and replace in the list of strings
    replaced_strings = search_replace_strings(strings, search_str, replace_str)

    # Output replaced strings
    print("\nReplaced strings:")
    for i, replaced_string in enumerate(replaced_strings):
            print(str(i+1) + "." + replaced_string)
if __name__=="__main__":
    main()
