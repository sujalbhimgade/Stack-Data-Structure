class Stack:
    def __init__(self):
        self.stack = []

    
    def push(self, item):
        self.stack.append(item)
        print(f"Pushed {item} to the stack.")

    
    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty.")
        else:
            item = self.stack.pop()
            print(f"Popped {item} from the stack.")

   
    def display(self):
        if len(self.stack) == 0:
            print("Stack is empty.")
        else:
            print("Stack:", self.stack)

def stack_operations():
    s = Stack()
    while True:
        print("\nStack Operations:")
        print("1. Push")
        print("2. Pop")
        print("3. Display Stack")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            item = int(input("Enter the value to push: "))
            s.push(item)
        elif choice == 2:
            s.pop()
        elif choice == 3:
            s.display()
        elif choice == 4:
            print("Exiting Stack operations.")
            break
        else:
            print("Invalid choice. Please try again.")


stack_operations()
