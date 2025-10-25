class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if self.is_empty():
            print("Stack is empty.")
            return None
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print("Stack:", list(reversed(self.items)) if self.items else "Empty")

    def evaluate_rpn(self):
        expr = input("Enter RPN expression (e.g., 3 4 + 2 *): ")
        self.items.clear()
        for token in expr.split():
            if token in '+-*/':
                if len(self.items) < 2:
                    print("Error: Not enough operands.")
                    return
                b = self.pop()
                a = self.pop()
                if token == '+': self.push(a + b)
                elif token == '-': self.push(a - b)
                elif token == '*': self.push(a * b)
                elif token == '/':
                    if b == 0:
                        print("Error: Division by zero.")
                        return
                    self.push(a / b)
            else:
                try:
                    self.push(float(token))
                except ValueError:
                    print(f"Invalid token: {token}")
                    return
        if len(self.items) == 1:
            print("RPN Result:", self.pop())
        else:
            print("Error: Invalid RPN expression.")

def main():
    stack = Stack()
    while True:
        print("\n1. Push  2. Pop  3. Display  4. Evaluate RPN  5. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            try:
                num = float(input("Enter value to push: "))
                stack.push(num)
                print(f"Pushed {num}")
            except ValueError:
                print("Invalid number.")
        elif choice == '2':
            val = stack.pop()
            if val is not None:
                print(f"Popped: {val}")
        elif choice == '3':
            stack.display()
        elif choice == '4':
            stack.evaluate_rpn()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()