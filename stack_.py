from debug_decorator import debug

@debug("()[]{}","(]","[")
def is_valid(s):
    stack = []
    left = ["(","[","{"]
    right = [")","]","}"]
    for char in s:
        if char in left:
            stack.append(char)
        elif char in right:
            if right.index(char) == left.index(stack[-1]):
                stack.pop()
            else:
                return False
    if len(stack) != 0:
        return False
    return True

@debug("/../","/home/","/home/user/Documents/../Pictures","/home//foo/")
def simplify_path(path):
    parts = path.split("/")
    stack = []
    for part in parts:
        if part == "." or part == "":
            continue
        elif part == "..":
            if stack:
                stack.pop()
        else:
            stack.append(part)
    res = "/" + "/".join(stack)
    return res


class MinStack:
    def __init__(self):
        self.data = []
        self.min_stack = []

    def push(self,val):
        self.data.append(val)
        minimum = val
        if self.min_stack:
            minimum = min(minimum,self.min_stack[-1])
        self.min_stack.append(minimum)

    def pop(self):
        self.data.pop()
        self.min_stack.pop()

    def top(self):
        return self.data[-1]

    def getMin(self):
        return self.min_stack[-1]


# minStack = MinStack()
# minStack.push(-2)
# minStack.push(0)
# minStack.push(-3)
#
# print(minStack.getMin())
# minStack.pop()
# print(minStack.top())
# print(minStack.getMin())


@debug(["2","1","+","3","*"],["4","13","5","/","+"],["10","6","9","3","+","-11","*","/","*","17","+","5","+"],["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
def evalRPN(tokens):
    stack = []
    for token in tokens:
        if token.isnumeric() or (token.startswith("-") and len(token) != 1):
            stack.append(int(token))
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            match token:
                case "+":
                    stack.append(num1+num2)
                case "-":
                    stack.append(num2-num1)
                case "*":
                    stack.append(num1*num2)
                case "/":
                    stack.append(int(num2 / num1))
                case _:
                    continue
    return stack[-1]


@debug("(1+(4+5+2)-3)+(6+8)",exec=True)
def calculate(s):
    ops = [1]
    sign = 1
    res = 0
    n = len(s)
    i = 0

    while i < n:
        if s[i] == ' ':
            i += 1
        elif s[i] == '+':
            sign = ops[-1] # 保持当前环境符号
            i += 1
        elif s[i] == '-':
            sign = -ops[-1] # 取当前环境符号的相反数
            i += 1
        elif s[i] == '(':
            ops.append(sign) # 进入新括号，记录这个括号前的符号环境
            i += 1
        elif s[i] == ')':
            ops.pop() # 退出括号，弹出环境符号
            i += 1
        else:
            # 读取完整的数字（处理多位数，如 "123"）
            num = 0
            while i < n and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            res += sign * num

    return res

