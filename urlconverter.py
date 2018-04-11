"""
url regex converter
https://blog.csdn.net/qq_40272386/article/details/78800507
"""

class FourDigitalYearConverter :
    regex = '[0-9]{4}'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return "%04d"%(value)

