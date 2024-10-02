'''To write a function called most_frequent that takes a string and prints the letters in decreasing order of
frequency.'''
def most_frequent(string):
    #Create a dictionary to store the frequency of each letter
    frequency={}
    #Count the frequency of each letter in the string
    for char in string:
        if char.isalpha():   #Consider on;ly alphabetic characters
            if char in frequency:
                frequency[char]+=1
            else:
                frequency[char]=1
    #Sort the dictionary based on the frequency in decreasing order
    sorted_frequency=sorted(frequency.items(),key=lambda x : x[1],reverse=True)
    #Print the letter in decreasin order of frequency
    print("Letters in decreasing order of frequency:")
    for char,freq in sorted_frequency:
        print(char,":",freq)
#Test the function)
test_string="hello world"
most_frequent(test_string)

