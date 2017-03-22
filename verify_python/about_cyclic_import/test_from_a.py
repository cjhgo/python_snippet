#coding: utf-8
#created at 17-3-8 11:05
import sys
from test_from_b import fun
# import test_from_b
print "hello"

fun()
print '\n'.join(sys.modules.keys())
print sys.modules.get("test_from_b")