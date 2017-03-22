#coding: utf-8
#created at 17-3-4 17:36


def wrap(fun):
    print "i run"
    def foo(fun):
        print id(fun)
    return foo

@wrap
def a():
    pass

@wrap
def b():
    pass

