from src.interpreter.parser import (
    Exps,
    Exp,
    Vec,
    Matrix,
    Int,
    Var,
    Sum,
    Minus,
    Product,
    Elements,
    Element,
    Vectors,
)
from src.interpreter.utils import get_vector_elements, get_matrix_elements
from src.interpreter.linear_algebra import V, Mat


"""Module corresponding to the basic linear algebra interpreter. It supports basic linear algebra
such as matrix and vector arithmetic.

Example Usage:

      >>> ast = parser.parse('[3 4 5] + [4 5 6]')
      >>> evaluate(ast)
      [7,9,11]

"""
def evaluate(ast):
    """Evaluate a given basic linear algebra expression."""
    match ast:
        case Exp(exp):
            match exp:
                case Vec(elements):
                    vector_entries = get_vector_elements(elements)
                    return vector_entries

                case Matrix(elements):
                    matrix_entries = get_matrix_elements(elements)
                    return matrix_entries

                case Sum(Vec(elements),Vec(elements2)):
                    vec = get_vector_elements(elements)
                    vec2 = get_vector_elements(elements2)
                    vec_object = V(vec)
                    vec2_object = V(vec2)
                    return vec_object + vec2_object

                case Minus(Vec(elements), Vec(elements2)):
                    vec = get_vector_elements(elements)
                    vec2 = get_vector_elements(elements2)
                    vec_object = V(vec)
                    vec2_object = V(vec2)
                    return vec_object - vec2_object

                case Product(Vec(elements), e2):
                    operand = V(get_vector_elements(elements)) 
                    operand2 = V(get_vector_elements(e2.elements)) if isinstance(e2, Vec) else e2.num
            
                    return operand * operand2

                case Sum(Matrix(e1), Matrix(e2)):
                    mat = Mat(get_matrix_elements(e1))
                    mat2 = Mat(get_matrix_elements(e2))
                    return mat + mat2

                case Minus(Matrix(e1), Matrix(e2)):
                    mat = Mat(get_matrix_elements(e1))
                    mat2 = Mat(get_matrix_elements(e2))
                    return mat - mat2

                case Product(Matrix(e1), e2):
                    operand = Mat(get_matrix_elements(e1))
                    operand2 = Mat(get_matrix_elements(e2)) if isinstance(e2, Matrix) else e2.num
                    return operand * operand

        
