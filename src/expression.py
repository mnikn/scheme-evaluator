from environment import *
from primitives import accumulate

class ExpressionParser:
    def parse(self,exp):
        if exp == [] or isinstance(exp,Expression): return exp

        if isinstance(exp,list) == False:
            if exp.isdigit():
                exp = NumberExpression(exp)
            elif exp.find('"') != -1 or exp[0].find("'") != -1:
                exp = StringExpression(exp)
            else:
                exp = VariableExpression(exp)
            return exp

        if exp[0] == "define":
            exp = DefineExpression(exp)
        elif exp[0] == "set!":
            exp = AssignmentExpression(exp)
        elif exp[0] == "if":
            exp = IfExpression(exp)
        elif exp[0] == "cond":
            exp = CondExpression(exp)
        elif exp[0] == "lambda":
            exp = LambdaExpression(exp)
        elif exp[0] == "begin":
            exp = SequenceExpression(exp)
        else:
            exp = ApplicationExpression(["application",exp[0],exp[1:]])
        return exp

class Expression:
    parser = ExpressionParser()
    def __init__(self):
        pass
    def analyze(self):
        raise "Not implmented yet!"

class NumberExpression(Expression):
    def __init__(self,exp):
        self.value = int(exp)
    def analyze(self):
        def _do_eval(evaluator,env):
            return self.value
        return _do_eval

class StringExpression(Expression):
    def __init__(self,exp):
        self.value = exp[1:len(exp)-1]
    def analyze(self):
        def _do_eval(evaluator,env):
            return self.value
        return _do_eval
    

class VariableExpression(Expression):
    def __init__(self,exp):
        self.name = exp
    def analyze(self):
        def _do_eval(evaluator,env):
            return env.get_variable(self.name)
        return _do_eval
    

class DefineExpression(Expression):
    def __init__(self,exp):
        if isinstance(exp[1],list):
            self.variable = exp[1][0]
            self.value = LambdaExpression(['lambda',exp[1][1:],exp[2]])
        else:
            self.variable = exp[1]
            self.value = exp[2]
    def analyze(self):
        def _do_eval(evaluator,env):
            env.define_variable(self.variable,value(evaluator,env))
            return "ok"
        value = Expression.parser.parse(self.value).analyze()
        return _do_eval

class AssignmentExpression(Expression):
    def __init__(self,exp):
        self.variable = exp[1]
        self.value = exp[2]
    def analyze(self):
        def _do_eval(evaluator,env):
            env.set_variable(self.variable,value(evaluator,env))
            return "ok"
        value = Expression.parser.parse(self.value).analyze()
        return _do_eval

class IfExpression(Expression):
    def __init__(self,exp):
        self.pred = exp[1]
        self.true_exp = exp[2]
        self.false_exp = exp[3]
    def analyze(self):
        def _do_eval(evaluator,env):
            if pred(evaluator,env):
                return true_exp(evaluator,env)
            return false_exp(evaluator,env)
        pred = Expression.parser.parse(self.pred).analyze()
        true_exp = Expression.parser.parse(self.true_exp).analyze()
        false_exp = Expression.parser.parse(self.false_exp).analyze()
        return _do_eval

class CondExpression(Expression):
    def __init__(self,exp):
        self.conditions = exp[1:len(exp)-1]
        self.otherwise = exp[-1]
    def analyze(self):
        def _do_eval(evaluator,env):
            return IfExpression(exps).analyze()(evaluator,env)
        exps = self._cond_to_if(self.conditions)
        return _do_eval
    def _cond_to_if(self,conditions):
        if len(conditions) == 1:
            return ["if"] + conditions[0] + [self.otherwise[-1]]
        conditions[0] += [self._cond_to_if(conditions[1:])]
        return ["if"] + conditions[0]

class LambdaExpression(Expression):
    def __init__(self,exp):
        self.args = exp[1]
        self.body = exp[2]
    def analyze(self):
        def _do_eval(evaluator,env):
            return ProcedureExpression(["procedure",self.args,self.body,env])
        return _do_eval

class SequenceExpression(Expression):
    def __init__(self,exp):
        self.exps = exp[1:]
    def analyze(self):
        def _do_eval(evaluator,env):
            result = None
            for exp in self.exps:
                result = evaluator.eval(exp,env)
            return result
        return _do_eval

class ProcedureExpression(Expression):
    def __init__(self,exp):
        self.args = exp[1]
        self.proc = exp[2]
        self.env = exp[3]
    def analyze(self):
        def _do_eval(evaluator,env):
            return evaluator.eval(self.proc,env)
        return _do_eval

class ApplicationExpression(Expression):
    def __init__(self,exp):
        self.operator = exp[1]
        self.args = exp[2]
    def analyze(self):
        def _do_eval(evaluator,env):
            values = map(lambda arg: arg(evaluator,env),arg_values)
            return evaluator.apply(operator(evaluator,env),values)
        operator = Expression.parser.parse(self.operator).analyze()
        arg_values = map(lambda arg: Expression.parser.parse(arg).analyze(),self.args)
        return _do_eval
