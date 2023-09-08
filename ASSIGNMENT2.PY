#multiple inheritance
class mother:
    def mother_name():
        print("this is function of mother")
     
class father:
    def father_name():
        print("this is a function of father")
        
class child(mother , father):
    def child_name():
        print("this is a function of child")
        

x1 = child()
x1 = child.mother_name()
x1 = child.father_name()
x1 = child.child_name()

