# site constant
# https://blog.csdn.net/u010941728/article/details/51417483

class _const():
    class ConstError(TypeError):
        pass

    def __setattr__(self, key, value):
        # self.__dict__
        if key in self.__dict__:
            raise self.ConstError("constant reassignment error!")
        self.__dict__[key] = value


import sys

sys.modules[__name__] = _const()


