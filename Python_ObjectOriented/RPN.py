#RPN.py

import ast

def to_postfix(expr):
    if isinstance(expr,ast.Constant):
        return str(expr.value)
    elif isinstance(expr,ast.Name):
        return expr.id
    elif isinstance(expr,ast.UnaryOp):
        if isinstance(expr.op, ast.USub):
            return to_postfix(expr.operand) + ' ~'
        else:
            raise ValueError(f"Can't parse {expr}")
    elif isinstance(expr,ast.BinOp):
        left = to_postfix(expr.left)
        right = to_postfix(expr.right)
        if isinstance(expr.op,ast.Add):
            op = '+'
        elif isinstance(expr.op,ast.Sub):
            op = '-'
        elif isinstance(expr.op,ast.Mult):
            op = '*'
        elif isinstance(expr.op,ast.Div):
            op = '/'
        elif isinstance(expr.op,ast.Mod):
            op = '%'
        elif isinstance(expr.op,ast.Pow):
            op = '**'
        elif isinstance(expr.op,ast.FloorDiv):
            op = '//'
        else:
            raise ValueError(f"Can't parse {expr}")
        return ' '.join([left, right, op])
            
    else:
        raise ValueError(f"Can't parse {expr}")

def RPN(e):
    expr = ast.parse(e).body[0].value
    try:
        return to_postfix(expr)
    except ValueError:
        raise ValueError(f"Can't parse {e}")
    
def postfix_eval(expr, d = None):
    stack = []
    for token in expr.split():
        if token.isnumeric():
            stack.append(ast.literal_eval(token))
        elif token in {'+', '-', '*', '/', '%', '**', '//'}:
            right = stack.pop()
            left = stack.pop()
            if token == '+':
                stack.append(left + right)
            elif token == '-':
                stack.append(left - right)
            elif token == '*':
                stack.append(left * right)
            elif token == '/':
                stack.append(left / right)
            elif token == '%':
                stack.append(left % right)
            elif token == '**':
                stack.append(left ** right)
            else:
                stack.append(left // right)
        elif token == '~':
            stack.append(-stack.pop())
        else:
            #must be a variable
            if d and token in d:
                stack.append(d[token])
            else:
                raise ValueError(f'No value provided for {token}')
    if len(stack) == 1:
        return stack.pop()
    else:
        raise ValueError(f'{expr} is malformed')
    
