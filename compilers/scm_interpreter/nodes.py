class Program:
    "PROGRAM node."
    __match_args__ = ('expressions,')
    def __init__(self, expressions):
        self.expressions = expressions

    def __repr__(self):
        return f'(Program {self.expressions})'

class Nil:
    pass
    
class Exps:
    "PROGRAM node."
    __match_args__ = ('expressions',)
    def __init__(self, expressions):
        self.expressions = expressions

    def __repr__(self):
        return f'(Exps {self.expressions})'

class Exp:
    "PROGRAM node."
    __match_args__ = ('exp',)
    def __init__(self, exp):
        self.exp = exp
      

    def __repr__(self):
        return f'(Exp {self.exp})'

class Prim:
    __match_args__ = ('op', 'exp1', 'exp2')
    def __init__(self, op, exp1, exp2):
        self.op = op
        self.exp1 = exp1
        self.exp2 = exp2

    def __repr__(self):
        return f'(Prim {self.op} {self.exp1} {self.exp2})'
    
class If:
    "IF node."
    __match_args__ = ('condition', 'scmthen', 'scmelse')
    def __init__(self, condition, scmthen, scmelse):
        self.condition = condition
        self.scmthen = scmthen
        self.scmelse = scmelse

    def __repr__(self):
        return f'(IF (Condition {self.condition}) (Then {self.scmthen}) (Else {self.scmelse}))'

class Bool:
    __match_args__ = ('boolscm',)
    def __init__(self, boolscm):
        self.boolscm = boolscm

    def __repr__(self):
        return f'(Bool {self.boolscm})'

class Begin:
    __match_args__ = ('exps',)
    def __init__(self, exps):
        self.exps = exps

    def __repr__(self):
        return f'(Begin {self.exps})'

class While:
    __match_args__ = ('condition', 'expr')
    def __init__(self, condition, expr):
        self.condition = condition
        self.expr = expr

    def __repr__(self):
        return f'(While {self.condition} {self.expr})'

class Let:
    __match_args__ = ('binding', 'expr')
    def __init__(self, binding, expr):
        self.binding = binding
        self.expr = expr

    def __repr__(self):
        return f'(Let {self.binding} {self.expr})'

class SetBang:
    __match_args__ = ('var', 'expr')
    def __init__(self, var, expr):
        self.var = var
        self.expr = expr

    def __repr__(self):
        return f'(SetBang {self.var} {self.expr})'

class Int:
    "INT node."
    __match_args__ = ('num',)
    def __init__(self, num):
        self.num = num

    def __repr__(self):
        return f'(Int {self.num})'

class Op:
    __match_args__ = ('op',)
    def __init__(self, op):
        self.op = op

    def __repr__(self):
        return f'(OP {self.op})'


class Binding:
    "BINDING node."
    __match_args__ = ('var', 'exp')
    def __init__(self, var, exp):
        self.var = var
        self.exp = exp

        
    def __repr__(self):
        return f'(Binding {self.var} {self.exp})'

class Var:
    __match_args__ = ('var',)
    def __init__(self, var):
        self.var = var

    def __repr__(self):
        return f'(Var {self.var})'

class Application:
    __match_args__ = ('exps',)
    def __init__(self, exps):
        self.exps = exps

    def __repr__(self):
        return f'(Application (Exps {self.exps}))'

class Define:
    __match_args__=('var', 'exp')
    def __init__(self, var, exp):
        self.var = var
        self.exp = exp

    def __repr__(self):
        return f'(Define (Var {self.var}) (Exp {self.exp}))'

class Lambda:
    __match_args__=('params', 'body')
    def __init__(self, params, body):
        self.params = params
        self.body = body

    def __repr__(self):
        return f'(Lambda (Params {self.params}) (Body {self.body}))'
