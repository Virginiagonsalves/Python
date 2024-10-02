'''Program to read, display and count number of sentences of the given file.'''
def count_sentences(text):
    delimiters=[".","!","?"]
    sentence_count=0
    for char in text:
        if char in delimiters:
            sentence_count+=1
    return sentence_count
file_path="Hi.txt"
with open(file_path)as file:
    file_contents=file.read()
print("Contents of file:")
print(file_contents)
num_sentences=count_sentences(file)
print("\nNumber of sentences in the file:",num_sentences)
