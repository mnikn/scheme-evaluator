from expression import *

class ExpressionParser:
    def parse(self,exp,env):
        if exp == []: return []

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
        elif exp[0] == "lambda":
            exp = LambdaExpression(exp)
        elif exp[0] == "begin":
            exp = SequenceExpression(exp)
        else:
            exp = ApplicationExpression(["application",exp[0],exp[1:]])
        return exp
