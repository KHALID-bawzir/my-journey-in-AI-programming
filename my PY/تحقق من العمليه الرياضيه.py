from typing import List
def math_expr(expr: str):
    s = expr.strip()
    if not s:
        return False
    return s.replace(' ', '').replace('+', '').replace('-', '').replace('*', '').replace('/', '').replace('(','').replace(')', '').replace('.', '').isdigit()


print(math_expr('1+2-9'))
