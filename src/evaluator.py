from expression_formattor import *
from expression_parser import *
from expression import *
from primitives import *
from environment import *


class Evaluator:
    def __init__(self,primitives):
        self._exp_parser = ExpressionParser()
        self._primitives = primitives
    def eval(self,exp,env):
        if exp == []: return

        if isinstance(exp,Expression) == False:
            exp = self._exp_parser.parse(exp,env)
        return exp.eval(self,env)
    def apply(self,proc,args):
        if isinstance(proc,ProcedureExpression):
            proc.env = Environment.extend_environment(dict(zip(proc.args, args)),proc.env)
            return proc.eval(self,proc.env)
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
        "list": to_list,
        "cons": cons,
        "car": car,
        "cdr": cdr,
        "null?": null}
    init_primitives()
    evaluator = Evaluator(primitives)
    run_evaluator()


