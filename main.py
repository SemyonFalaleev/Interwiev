from refactoring import Email
class Stack:
    def __init__(self, object=None):
        if object == None:
            self.stack = []
        else:
            self.stack = [object]

    def is_empty(self):
        if self.stack == []:
            return True
        else:
            return False

    def push(self, element):
        self.stack.insert(0, element)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop(0)
        else:
            return None
    def peek(self):
        if not self.is_empty():
            return self.stack[0]
        else:
            return None

    def size(self):
        return len(self.stack)

    def __str__(self):
        return f"{self.stack}"

def balanced(elements):
    stack = Stack()
    pairs = {")": "(", "}": "{", "]": "["}

    for item in elements:
        if item in "({[":
            stack.push(item)
        elif item in ")}]":
            if stack.peek() == pairs[item]:
                stack.pop()
            else:
                 return "Несбалансированно"
    if stack.is_empty():
        return "Сбалансированно"

if __name__ == "__main__":
    email = Email('login@gmail.com','qwerty')
    email.send_message(['vasya@email.com', 'petya@email.com'], 'Subject', 'Message')
    email.receive()