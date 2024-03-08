from scheme_interp.parser import parser
from scheme_interp.interp import interp

def repl(prompt='lambda> '):
    while True:
        user_input = input(prompt)
        if user_input.strip() == "(quit)":
            break

        tree = parser.parse(user_input)
        val = interp(tree)
        if val is not None:
            print(py_to_scheme(val))

def py_to_scheme(e):
    match e:
        case [*exps]:
            return '(' + ' '.join(map(py_to_scheme, exps)) + ')'
        case True:
            return '#t'
        case False:
            return '#f'
        case _:
            return str(e)
