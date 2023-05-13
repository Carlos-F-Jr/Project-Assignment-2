table = {
    ('E', 'a'): ['T', 'Q'],
    ('E', '('): ['T', 'Q'],
    ('Q', '+'): ['+', 'T', 'Q'],
    ('Q', '-'): ['-', 'T', 'Q'],
    ('Q', ')'): ['ε'],
    ('Q', '$'): ['ε'],
    ('T', 'a'): ['F', 'R'],
    ('T', '('): ['F', 'R'],
    ('R', '+'): ['ε'],
    ('R', '-'): ['ε'],
    ('R', '*'): ['*', 'F', 'R'],
    ('R', '/'): ['/', 'F', 'R'],
    ('R', ')'): ['ε'],
    ('R', '$'): ['ε'],
    ('F', 'a'): ['a'],
    ('F', '('): ['(', 'E', ')']
}

stack = ['$']

input_str1 = '(a+a)*a'

input_str2 = 'a*(a/a)'

input_str3 = 'a(a+a)'

def parse(input_str):
    stack.append('E')
    i = 0
    while len(stack) > 0:
        top = stack[-1]
        if top == input_str[i]:
            print(f"Stack: {stack}  Input: {input_str[i:]}  Action: match {top}")
            stack.pop()
            i += 1
        elif top in ('a', '+', '-', '*', '/', '(', ')', '$'):
            print(f"Stack: {stack}  Input: {input_str[i:]}  Action: error")
            return False
        else:
            try:
                production = table[(top, input_str[i])]
                print(f"Stack: {stack}  Input: {input_str[i:]}  Action: {top} -> {''.join(production)}")
                stack.pop()
                for symbol in reversed(production):
                    if symbol != 'ε':
                        stack.append(symbol)
            except KeyError:
                print(f"Stack: {stack}  Input: {input_str[i:]}  Action: error")
                return False
    return True

if parse(input_str1 + '$'):
    print("Accepted")
else:
    print("Rejected")

if parse(input_str2 + '$'):
    print("Accepted")
else:
    print("Rejected")

if parse(input_str3 + '$'):
    print("Accepted")
else:
    print("Rejected")
