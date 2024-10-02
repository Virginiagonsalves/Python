'''To write a menu driven program to implement stack using Lists'''
class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,item):
        self.stack.append(item)
        print("Pushed",item,"into the stack")
    def pop(self):
        if not self.is_empty():
            item=self.stack.pop()
            print("Popped",item,"from the stack")
            return item
        else:
            print("Stack is empty")
    def peek(self):
        if not self.is_empty():
            item=self.stack[-1]
            print("Top item of Stack is",item)
            return item
        else:
            print("Stack is empty")
    def is_empty(self):
        return len(self.stack)==0
    def display(self):
        if not self.is_empty():
            print("Stack:",self.stack)
        else:
            print("Stack is empty")
#Function to display menu options
def display_menu():
 print("\nStack Operations:")
 print("1.Push")
 print("2.Pop")
 print("3.Peek")
 print("4.Display Stack")
 print("5.Exit")

#Main function
def main():
 stack=Stack()
 while True:
     display_menu()
     choice=input("Enter your choice(1-5):")
     if choice=='1':
        item=input("Enter item to push:")
        stack.push(item)
     elif choice=='2':
         stack.pop()
     elif choice=='3':
         stack.peek()
     elif choice=='4':
         stack.display()
     elif choice=='5':
         print("Exiting the program...")
     else:
         print("Invalid choice!Please try again.")
if __name__=="__main__":
    main()
