from scheme_interp.nodes import (
    Program,
    Nil,
    Exps,
    Exp,
    Prim,
    If,
    Bool,
    Begin,
    While,
    Let,
    SetBang,
    Int,
    Op,
    Binding,
    Var,
    Define,
    Application,
    Lambda,
)
from scheme_interp.utils import flatten_params, flatten_exps
import operator as op

class Env(dict):
    def __init__(self, params=(), args=(), outer=None):
        self.update(zip(params, args))
        self.outer = outer

    def find(self, var):
        if var in self:
            return self
        elif self.outer is not None:
            return self.outer.find(var)
        else:
            raise NameError(f"Variable '{var}' is not defined.")
    
class Procedure(object):
    def __init__(self, params, body, env):
        self.params, self.body, self.env = params, body, env

    def __call__(self, *args):
        return interp(self.body, Env(self.params, args, self.env))


def standard_env():
    env = Env()
    env.update({
        'car': lambda x: x[0],
        'cdr': lambda x: x[1:],
        'cons': lambda x, y: [x, y],
        'list': lambda *x: list(x),
        'map': lambda *args: list(map(*args)),
        'eq?': op.is_,
        'equal?': op.eq,
        'list': lambda *x: list(x),
        'list?': lambda x: isinstance(x, list),
        'length': len,
        'null?': lambda x: x == [],
        
        })
    return env

global_env = standard_env()


def interp(exp, env=global_env):
    """
    takes an ast corresponding to the syntax tree and evaluates it in the context
    of the environment `global_env`; procedures have a local environment but also get
    evaluated in the context of the global environment.

    Examples:

    >>> ast = parser.parse("(+ 1 1)")
    >>> interp(ast, env)
    2
    >>> ast2 = parser.parse("(if #t 1 2)")
    >>> interp(ast2, env)
    1
    """
    match exp:
        case Exps(exps):
            result = None
            for exp in exps:
                result = interp(exp, env)
            return result
        
        case Exp(e):
            return interp(e, env)
        
        case Bool(b):
            return b
        
        case If(cnd, thn, els):
            match interp(cnd, env):
                case "#t":
                    return interp(thn, env)
                case "#f":
                    return interp(els, env)
                
        case Prim(Op(oper), e, e2):
            match oper:
                case 'and':
                    match interp(e, env):
                        case '#t':
                            match interp(e2, env):
                                case '#t':
                                    return '#t'
                                case '#f':
                                    return '#f'
                        case '#f':
                            return '#f'
                        
                case 'or':
                    match interp(e, env):
                        case '#t':
                            return '#t'
                        case '#f':
                            match interp(e2, env):
                                case '#t':
                                    return '#t'
                                case '#f':
                                    return '#f'
                                
                case '+':
                    return interp(e, env) + interp(e2, env)
                
                case '-':
                    return interp(e, env) - interp(e2, env)

                case '*':
                    return interp(e, env) * interp(e2, env)

                case '=':
                    return '#t' if interp(e, env) == interp(e2, env) else '#f'
        case Int(n):
            return n
        
        case Var(e):
            return env.find(e)[e]
        
        case Let(Binding(Var(var), e), body_exp):
            proc = Procedure([var], body_exp, env)
            exps = [e]
            vals = [interp(e2, env) for e2 in exps]

            return proc(*vals)
        
        case SetBang(var, e):
            env.find(var.var)[var.var] = interp(e, env)
            return None
            
        case Begin(exps):
            flat_expressions = flatten_exps(exps)
            expressions = flat_expressions[:-1]
            for exp in expressions:
                interp(exp, env)

            return interp(flat_expressions[-1], env)

        case Define(Var(var), exp):
            env[var] = interp(exp, env)

        case Lambda(params, body):
            parameters = flatten_params(params)

            return Procedure(parameters, body, env)

        case Application(exps):
            exps = flatten_exps(exps)
            operator = interp(exps[0], env)
            exps = exps[1:]
            vals = [interp(e, env) for e in exps]

            return apply_scm(operator, vals)
            
        case _:
            raise ValueError(f'Parse node {exp} is not valid node.')

def apply_scm(operator, exps):
    return operator(*exps)
