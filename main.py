class Stack:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return None
        self.stack.pop()
        return self.stack[-1]

    def peek(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1]

    def size(self):
        return len(self.stack)


def balance(str):
    stack = []
    opened = ["(", "{", "["]
    closed = [")", "}", "]"]
    stackVerify = True
    for el in str:
        if el in opened:
            stack.append(el)
        elif el in closed:
            if len(stack) == 0:
                stackVerify = False
                break

            stack_el = stack.pop()
            if stack_el == "(" and el == ")":
                continue
            if stack_el == "[" and el == "]":
                continue
            if stack_el == "{" and el == "}":
                continue

            stackVerify = False
            break
    if stackVerify == True and len(stack) == 0:
        print("Сбалансированно")
    else:
        print("Несбалансированно")



myStr = input("Введите строку со скобками: ")
print(balance(myStr))

str1 = '(((([{}]))))'
str2 = '[([])((([[[]]])))]{()}'
str3 = '{{[()]}}'
str4 = '}{}'
str5 = '{{[(])]}}'
str6 = '[[{())}]'



