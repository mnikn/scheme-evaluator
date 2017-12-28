from environment import *

class Expression:
    def __init__(self):
        pass
    def eval(self,evaluator,env):
        raise "Not implmented yet!"

class NumberExpression(Expression):
    def __init__(self,exp):
        self.value = int(exp)
    def eval(self,evaluator,env):
        return self.value

class StringExpression(Expression):
    def __init__(self,exp):
        self.value = exp[1:len(exp)-1]
    def eval(self,evaluator,env):
        return self.value

class VariableExpression(Expression):
    def __init__(self,exp):
        self.name = exp
    def eval(self,evaluator,env):
        return env.get_variable(self.name)

class DefineExpression(Expression):
    def __init__(self,exp):
        if isinstance(exp[1],list):
            self.variable = exp[1][0]
            self.value = LambdaExpression(['lambda',exp[1][1:],exp[2]])
        else:
            self.variable = exp[1]
            self.value = exp[2]
    def eval(self,evaluator,env):
        value = evaluator.eval(self.value,env)
        env.define_variable(self.variable,value)
        print("ok")

class AssignmentExpression(Expression):
    def __init__(self,exp):
        self.variable = exp[1]
        self.value = exp[2]
    def eval(self,evaluator,env):
        value = evaluator.eval(exp.value,env)
        env.set_variable(self.variable,value)
        print("ok")

class IfExpression(Expression):
    def __init__(self,exp):
        self.pred = exp[1]
        self.true_exp = exp[2]
        self.false_exp = exp[3]
    def eval(self,evaluator,env):
        if evaluator.eval(self.pred,env):
            return evaluator.eval(self.true_exp,env)
        return evaluator.eval(self.false_exp,env)

class LambdaExpression(Expression):
    def __init__(self,exp):
        self.args = exp[1]
        self.body = exp[2]
    def eval(self,evaluator,env):
        return ProcedureExpression(["procedure",self.args,self.body,env])

class SequenceExpression(Expression):
    def __init__(self,exp):
        self.exps = exp[1:]
    def eval(self,evaluator,env):
        result = None
        for exp in self.exps:
            result = evaluator.eval(exp,env)
        return result

class ProcedureExpression(Expression):
    def __init__(self,exp):
        self.args = exp[1]
        self.proc = exp[2]
        self.env = exp[3]
    def eval(self,evaluator,env):
        return evaluator.eval(self.proc,env)

class ApplicationExpression(Expression):
    def __init__(self,exp):
        self.operator = exp[1]
        self.args = exp[2]
    def eval(self,evaluator,env):
        operator = evaluator.eval(self.operator,env)
        arg_values = map(lambda arg: evaluator.eval(arg,env),self.args)
        return evaluator.apply(operator,arg_values)
