
class Sutdent:
    def __init__(self, name,id) -> None:
        self.name = name
        self.std_id= id
        self.next = None
    
    def __display__(self):
        print(f"Name : {self.name}, ID :{self.std_id}")

Sutdent1 = Sutdent("Prathmesh",1)
Sutdent2 = Sutdent("Pratham",2)
Sutdent3 = Sutdent("Ganesh",3)
Sutdent4 = Sutdent("Om",4)
Sutdent1.__display__()

l = [1,2,3,4]
for i in l:
    print(i)

Head = Sutdent1
Sutdent1.next = Sutdent2
Sutdent2.next = Sutdent3
Sutdent3.next = Sutdent4

Head = Sutdent1
while Head is not None:
    print(  Head.__display__())
    Head = Head.next