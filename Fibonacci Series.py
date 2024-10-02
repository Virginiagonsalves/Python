num=int(input("Enter the Fibonacci sequence length to be generated:"))
firstTerm=0
secondTerm=1
print('The Fibonacci series with',num,"terms is:")
print(firstTerm,secondTerm)
for i in range(2,num):
    curTerm=firstTerm+secondTerm
    print(curTerm,end=" ")
    firstTerm=secondTerm
    secondTerm=curTerm
