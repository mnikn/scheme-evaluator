def accumulate(proc,init,args):
    result = init
    for i in args:
        result = proc(result,i)
    return result

def add(*args):
    return accumulate(lambda a,b:a + b,0,args)
def subtract(*args):
    return accumulate(lambda a,b:a - b,0,args)
def multiply(*args):
    return accumulate(lambda a,b:a * b,1,args)
def divide(*args):
    return accumulate(lambda a,b:a / b,1,args)

def to_list(*args):
    return accumulate(lambda a,b:a + [b],[],args)

def cons(first,second):
    return [first] + second
def car(pair):
    if isinstance(pair,list) == False:
        return pair
    return pair[0]
def cdr(pair):
    if isinstance(pair,list) == False:
        return []
    if len(pair) == 2:
        return pair[1]
    return pair[1:]
def null(seq):
    return seq == [] or seq == None
