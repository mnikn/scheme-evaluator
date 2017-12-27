class Frame:
    def __init__(self,variables):
        self._vars = variables
    def get_variables(self):
        return self._vars
    def set_variable(self,name,value):
        self._vars[name] = value
    def get_variable(self,name):
        return self._vars[name]
    def has_variable(self,name):
        return name in self._vars

class Environment:
    def __init__(self):
        self._frame = Frame({})
        self._parent_env = None
    def get_frame(self):
        return self._frame
    def set_frame(self,frame):
        self._frame = frame
    def set_parent_env(self,env):
        self._parent_env = env
    def get_variable(self,name):
        if self._frame.has_variable(name):
            return self._frame.get_variable(name)
        if self._parent_env == None:
            return None
        return self._parent_env.get_variable(name)
    def set_variable(self,name,value):
        if self._frame.has_variable(name):
            return self._frame.set_variable(name,value)
        if self._parent_env == None:
            raise "Cannot find variable " + name
        return self._parent_env.set_variable(name,value)
    def define_variable(self,name,value):
        self._frame.set_variable(name,value)
    @staticmethod
    def extend_environment(env):
        new_env = Environment()
        new_env.set_parent_env(env)
        return new_env
