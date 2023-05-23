from data_structures.queue import Queue
from data_structures.stack import Stack


def multi_bracket_validation(text):
    bracketStack = Stack()
    for char in text:
        if (char == '(') or (char == '[') or (char == '{'):
            bracketStack.push(char)
        elif (char == ')') or (char == ']') or (char == '}'):
            if bracketStack.is_empty():
                return False
            if char == ')':
                if bracketStack.peek() != '(':
                    return False
            elif char == ']':
                if bracketStack.peek() != '[':
                    return False
            elif char == '}':
                if bracketStack.peek() != '{':
                    return False
            bracketStack.pop()

    if bracketStack.is_empty():
        return True

    return False

