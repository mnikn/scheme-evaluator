import unittest
from src.expression import *
from src.evaluator import Evaluator
from src.environment import *


class TestEvaluator(unittest.TestCase):
	def test_eval(self):
		pass
	def test_apply(self):
		pass

class TestNumberExpression(unittest.TestCase):
	def setUp(self):
		self.exp = NumberExpression(1)
	def test_init(self):
		self.assertEqual(self.exp.value,1)
	def test_eval(self):
		evaluator = Evaluator({})
		self.assertEqual(1,self.exp.eval(evaluator,{}))

class TestStringExpression(unittest.TestCase):
	def setUp(self):
		self.exp = StringExpression("'dasda'")
	def test_init(self):
		self.assertEqual(self.exp.value,"dasda")
	def test_eval(self):
		evaluator = Evaluator({})
		self.assertEqual("dasda",self.exp.eval(evaluator,{}))

class TestVariableExpression(unittest.TestCase):
	def setUp(self):
		self.exp = VariableExpression("var_name")
	def test_init(self):
		self.assertEqual(self.exp.name,"var_name")
	def test_eval(self):
		evaluator = Evaluator({})
		env = Environment()
		env.define_variable("var_name",54)
		self.assertEqual(54,self.exp.eval(evaluator,env))

class TestDefineExpression(unittest.TestCase):
	def setUp(self):
		self.exp1 = DefineExpression(["define","x","65"])
	def test_init(self):
		self.assertEqual("x",self.exp1.variable)
		self.assertEqual("65",self.exp1.value)
	def test_eval(self):
		evaluator = Evaluator({})
		env = Environment()
		self.exp1.eval(evaluator,env)
		self.assertEqual(env.get_variable("x"),65)


if __name__ == '__main__':
    unittest.main()
