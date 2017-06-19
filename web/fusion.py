from  web import models



class Info(object):
    def __init__(self,*args,**kwargs):
        self.userdb = kwargs
    @property
    def talk(self):
        print('方法',self)
