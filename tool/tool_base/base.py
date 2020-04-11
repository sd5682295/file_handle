# encoding = "utf-8"
class base(object):
    def setdata(self, method, data):
        if method in dir(self):
            setattr(self, method, data)
        else:
            "ERROR! method is not in self"

    def __call__(self, *args, **kwargs):
        """
        设置call方法，直接使用本身的set方法
        :return: 本身的set方法
        """
        return self.set(*args, **kwargs)

    def dispatch(self, method, *args, **kwargs):
        """
        反射方法，通过方法名和参数自动调用方法
        :param method:string 方法名 
        :return: 返回调用的方法
        """
        if method in dir(self):
            handle = getattr(self, method)
            return handle(*args, **kwargs)

    def getdata(self, method):
        """
        根据属性名获取属性
        :param method: string 属性名
        :return: 返回属性值
        """
        if method in self:
            return getattr(self, method)
        else:
            "ERROR! method is not in self"

