'''Program that reads a file, display the contents, builds a histogram of the words in the file and
print most common words in the file.'''
from collections import Counter
import re
def read_file(filename):
    with open(filename)as file:
        contents=file.read()
    return contents
def build_histogram(text):
    #Use regular expressions to split the text into words
    words=re.findall(r'\b\w+\b',text.lower())
    #print(words)
    #Count the frequency of each word using counter
    histogram=Counter(words)
    return histogram
def print_most_common_words(histogram,n=10):
    most_common=histogram.most_common(n)
    #print(most_common)
    print("Most common words:")
    for word,frequency in most_common:
        print(word,":",frequency)

def main():
    #Read the file
    filename=input("\nContents of the file:")
    contents=read_file(filename)
    print("\nContents of the file:")
    print(contents)
    histogram=build_histogram(contents)
    #print(histogram)
    #Print most common words
    print_most_common_words(histogram)
if __name__=="__main__":
    main()
