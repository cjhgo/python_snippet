#coding: utf-8
#created at 16-12-12 18:04

def x():
    a = [1,2,3]
    def xc():
        print a
        return a
    print id(a)
    return xc

def y(callback):
    b = ('a','b')
    def yc():

        return b,id(callback())
    return yc

def z(callback):
    print callback()


z(y(x()))