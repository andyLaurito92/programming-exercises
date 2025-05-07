def balanced_expression(exp: str) -> bool:
    """
    Return whether the exp recieved is balanced or not.
    Accepted characters: (, ), {, }, [, ]
    """
    if len(exp) < 2:
        return False
    
    stack_paren = []
    closing_map = {')': '(', '}':'{', ']':'['}

    for c in exp:
        if c == '(' or c == '{' or c == '[':
            stack_paren.append(c)
        elif c == ')' or c == ']' or c == '}':
            if len(stack_paren) == 0:
                return False

            last_char = stack_paren.pop()

            if last_char != closing_map[c]:
                return False
        else:
            raise ValueError(f"Found invalid character {c} ")
    return len(stack_paren) == 0
            


assert True == balanced_expression("[{()}]")
assert False == balanced_expression("([]")

assert False == balanced_expression("([)]")
