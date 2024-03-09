from scheme_interp.nodes import Exps

def flatten_exps(node):
    expressions = []
    match node:
        case Exps(e):
            return flatten_exps(e)
            
        case [*exps]:
            for exp in exps:
                expressions.extend(flatten_exps(exp))
        
        case _:
            expressions.append(node)

    return expressions

def flatten_params(params):
    unnested_params = []
    match params:
        case [*parms]:
            for parm in parms:
                flattened_parm = flatten_params(parm)
                if flattened_parm is not None:
                    unnested_params.extend(flattened_parm)
        case _:
            unnested_params.append(params)

    return unnested_params
