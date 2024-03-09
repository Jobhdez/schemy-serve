import ply.lex as lex
import ply.yacc as yacc
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
    Application,
    Lambda,
    Define,
)

reserved = {
    'if': 'IF',
    'let': 'LET',
    'while': 'WHILE',
    'begin': 'BEGIN',
    'and': 'AND',
    'or': 'OR',
    'not': 'NOT',
    'set': 'SET',
    'define': 'DEFINE',
    'lambda': 'LAMBDA',
    }
tokens = [
    'LPAREN', 'RPAREN', 'PLUS', 'MINUS', 'MUL',
    'LESS', 'GREATER', 'LESSEQ', 'EQ', 'EQQ',
    'GREATEREQ', 'INTEGER',
    'TRUE', 'FALSE', 'NAME', 'EXCLAMATION',
    
    ] + list(reserved.values())

t_PLUS = r'\+'
t_MINUS = r'-'
t_MUL = r'\*'
t_IF = r'if'
t_LET = r'let'
t_BEGIN = r'begin'
t_AND = r'and'
t_OR = r'or'
t_TRUE = r'\#t'
t_FALSE = r'\#f'
t_LESS = r'<'
t_EQ = r'='
t_LESSEQ = r'<='
t_GREATER = r'>'
t_GREATEREQ = r'>='
t_NOT = r'not'
t_SET = r'set'
t_WHILE = r'while'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_EXCLAMATION = r'\!'
t_DEFINE = r'define'
t_LAMBDA = r'lambda'
t_EQQ = r'eq\?'

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_?]*'
    t.type = reserved.get(t.value, 'NAME')
    return t


def t_INTEGER(t):
    r'-?[0-9]+'
    t.value = int(t.value)
    return t

t_ignore = ' \t\n'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
lexer = lex.lex()

def p_program(p):
    "expressions : expression expressions"
    p[0] = Exps([p[1], p[2]])

def p_program_empty(p):
    "expressions : expression"
    p[0] = Exp(p[1])
    
def p_expression_int(p):
    "expression : INTEGER"
    p[0] = Int(p[1])

def p_expression_bool(p):
    """expression : TRUE
                  | FALSE"""
    p[0] = Bool(p[1])

    
def p_expression_prim(p):
    "expression : LPAREN op expression expression RPAREN"
    p[0] = Prim(p[2], p[3], p[4])

def p_expression_var(p):
    "expression : NAME"
    p[0] = Var(p[1])

def p_expression_if(p):
    "expression : LPAREN IF expression expression expression RPAREN"
    p[0] = If(p[3], p[4], p[5])

def p_expression_while(p):
    "expression : LPAREN WHILE expression expression RPAREN"
    p[0] = While(p[3], p[4])

def p_expression_set(p):
    "expression : LPAREN SET EXCLAMATION expression expression RPAREN"
    p[0] = SetBang(p[4], p[5])

def p_expression_let(p):
    "expression : LPAREN LET binding expressions RPAREN"
    p[0] = Let(p[3], p[4])

def p_expression_begin(p):
    "expression : LPAREN BEGIN expressions RPAREN"
    p[0] = Begin(p[3])

def p_expression_application(p):
    "expression : LPAREN expressions RPAREN"
    p[0] = Application(p[2])

def p_op(p):
    """op : PLUS
        | MUL
        | MINUS
        | AND
        | OR
        | EQ
        | LESS
        | LESSEQ
        | GREATER
        | GREATEREQ
        | NOT"""
    p[0] = Op(p[1])

def p_binding(p):
    "binding : LPAREN LPAREN NAME expression RPAREN RPAREN"
    p[0] = Binding(Var(p[3]) if isinstance(p[3], str) else p[3], p[4])

def p_define(p):
    "expression : LPAREN DEFINE expression expression RPAREN"
    p[0] = Define(p[3], p[4])

def p_lambda(p):
    "expression : LPAREN LAMBDA LPAREN params RPAREN expression RPAREN"
    p[0] = Lambda(p[4], p[6])

def p_params(p):
    "params : NAME params"
    p[0] = [p[1], p[2]]

def p_params_single(p):
    'params : NAME'
    p[0] = [p[1]]

def p_error(p):
    print("Syntax error at '%s'" % p.value)
                 
parser = yacc.yacc()
