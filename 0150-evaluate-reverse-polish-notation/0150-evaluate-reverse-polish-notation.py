class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # push num into stack, pop num when reach operators

        stack = []
        # operators = ["+","-","*","/"]
        operators = {"+": lambda x, y: x + y, "-": lambda x, y: x - y, "*": lambda x, y: x * y, "/": lambda x, y: int(x / y)}  # Use int() for correct truncation towards zero

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                operation = operators[token]
                stack.append(operation(operand1, operand2))
  
        return stack.pop()
  
                
        