class A:
    def xyz(self):
        print("from xyz A")
    

    def __init__(self):
        print("from A")
      

  from A import A
class B(A):
    def abc(self):
        print("from abc B")

    def __init__(self):
        print("from B")
        #A.__init__(self)
        super().__init__()

from A import A
class C(A):
    def pqr(self):
        print("from pqr B")

    def __init__(self):
        print("from c")
        #A.__init__(self)
        super().__init__()


from B import B
from C import C
class D(B,C):
  def mno(self):
    print("from mno D")

  def __init__(self):
    print("from D")
    super().__init__()

obj=D()
  
