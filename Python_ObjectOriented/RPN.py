#Jonah Ebent, CSC310, 12/6/23, HW17 (RPN.py)
"""
Extend the function to_postfix() (and hence RPN()) defined in class so that it handles function calls for
either built in or user-defined functions. Make the simplifying assumption that the functions have no
keyword arguments (so just things like f(x,y)). For example, RPN('2 + f(x,g(1,2,3))') = '2 x 1 2 3 g f +'. Hint:
Try something as simple as ast.parse('pow(2,4)'). What type of expression is it (it isn't a BinOp, it is
something else)? You should be able to discover what it is interactively in the shell. Once you know what
it is – how do you get to the arguments of the function call? The name of the call? Note: the stack-based
evaluation algorithm would still apply (suitablt modified), but you would need a dictionary to distinguish
ordinary variables from function names and associate the right function with its name. Extra credit:
extend postfix_eval() in this way. For the extra credit inspect.signature might be helpful.
"""
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
    elif isinstance(expr,ast.Call): # this is what I added
        args = [to_postfix(i) for i in expr.args]
        func = expr.func.id
        return ' '.join([*args, func])
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
    
