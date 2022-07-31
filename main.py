class Stack:

    def __init__(self):
        self.stack = []

    def isEpmty(self):
        return len(self.stack) == 0

    def push(self, i):
        self.stack.append(i)
        return

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


if __name__ == '__main__':
    s = input('Введите строку: ')
    stack = Stack()
    flag = True
    for i in s:
        if i in '([{':
            stack.push(i)
        elif i in ')]}':
            if stack.isEpmty():
                flag = False
                break
            ls = stack.pop()
            if ls == '(' and i == ')':
                continue
            if ls == '[' and i == ']':
                continue
            if ls == '{' and i == '}':
                continue
            flag = False
            break
    if flag is True and stack.isEpmty:
        print('Сбалансировано')
    else:
        print('Несбалансировано')



