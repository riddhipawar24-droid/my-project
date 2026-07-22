class p1:
  def xyz(self):
    print("from p1 xyz") 

  def show(self):
    print("from p1 show")

  def __init__(self,name):
    self.name=name
    print("p1 con ")
    print(self.name)


class p2:
  def abc(self):
     print("from p2 abc")

  def show(self):
     print("from p2 show")

  def __init__(self,age):
    self.age=age
    print("p2 con ")
    print(self.age)


from p1 import p1 
from p2 import p2
class c(p1,p2):
    def pqr(self):
        print("im from child pqr")

    def call_p2_show(self):
        return p2.show(self)

    def __init__(self,name,age):
        print("c con ")
        p1.__init__(self,name)
        p2.__init__(self,age)
        
        
#object 
obj=c("ram",20);
