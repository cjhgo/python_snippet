#coding: utf-8
#created at 17-2-24 16:31

from aaa import bar

xx = None


def fun():
    global xx
    xx = {}
    xx["bbb"] = 123
    bar(xx)


fun()
print xx