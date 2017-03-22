#coding: utf-8
#created at 16-12-13 09:34


class gg(object):
    n = 99

    def __getattr__(self, name):
        return 111


    def __getitem__(self, name):
        return getattr(self, name)

a=gg()
print a.n
print a.xx
# print a[a.xx+33]