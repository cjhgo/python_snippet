#coding: utf-8
#created at 17-3-8 10:18
import sys

print "b in"
print "b imported: %s" % ("b" in sys.modules, )
import a
print "b out"
x = 3