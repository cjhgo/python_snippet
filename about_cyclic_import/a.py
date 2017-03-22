#coding: utf-8
#created at 17-3-8 10:18

print "a in"
import sys
print "a imported: %s" %("a" in sys.modules, )
print "b imported: %s" % ("b" in sys.modules, )
import b
print "b imported: %s" % ("b" in sys.modules, )
print "a out"