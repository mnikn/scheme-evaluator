from expression_formattor import *
from expression import *
from primitives import *
from environment import *


class Evaluator:
    def __init__(self,primitives):
        self._primitives = primitives
    def eval(self,exp,env):
        if exp == []: return

        if isinstance(exp,Expression) == False:
            exp = Expression.parser.parse(exp)
        return exp.analyze()(self,env)
    def apply(self,proc,args):
        if isinstance(proc,ProcedureExpression):
            proc.env = Environment.extend_environment(dict(zip(proc.args, args)),proc.env)
            return self.eval(proc,proc.env)
        return proc(*args)

def init_primitives():
    global_env.get_frame().set_variables(primitives)

def run_evaluator():
    print("--------------------\n")
    print("Input Expression:\n")
    exp = raw_input()

    exp = exp_formattor.format(exp)
    print(evaluator.eval(exp,global_env))
    print("\nEnd Evaluation")
    print("--------------------\n")
    run_evaluator()

if __name__ == '__main__':
    global_env = Environment()
    exp_formattor = ExpressionFormattor()
    primitives = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
        "=": equal,
        "list": to_list,
        "cons": cons,
        "car": car,
        "cdr": cdr,
        "null?": null}
    init_primitives()
    evaluator = Evaluator(primitives)
    run_evaluator()


