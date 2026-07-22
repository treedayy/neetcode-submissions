class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in '+-*/':
                stack.append(int(i))
            if i == '+':
                temp = stack.pop()
                temp2 = stack.pop()
                print(temp, temp2)
                stack.append(temp+temp2)
            if i == '-':
                temp = stack.pop()
                temp2 = stack.pop()
                print(temp, temp2)
                stack.append(temp2-temp)
            if i == '*':
                temp = stack.pop()
                temp2 = stack.pop()
                print(temp, temp2)
                stack.append(temp2*temp)
            if i == '/':
                temp = stack.pop()
                temp2 = stack.pop()
                stack.append(int(temp2 / temp))
            
        return int(stack[-1])