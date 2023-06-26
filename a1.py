
class Empty():
    "trying to access empty stack"
    pass
#implementing stack by using singly linked list
class node():
    def __init__(self,data):
        self.next=None
        self.data=data
class stack():
    def __init__(self):
        self.head=None
        self.len=0
    def isempty(self):
        return self.len==0
    def push(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            new=node(data)
            new.next=self.head
            self.head=new
        self.len+=1
    def pop(self):
        if self.isempty():
            raise Empty("stack is empty")
        else:
            prev_node=self.head
            self.head=self.head.next
            prev_node.next=None
            self.len-=1
        return prev_node.data
    def __len__(self):
        return self.len
    def top(self):
        if self.isempty():
            raise Empty("stack is empty")
        else:
            return (self.head.data)
# defining function findPositonandDistance
def  findPositionandDistance(t):
    sx,sy,sz,sd,s_=stack(),stack(),stack(),stack(),stack()
    sx.push(0),sy.push(0),sz.push(0)
    n,d,i,m=1,0,0,1,
     # ans is the list which contains x_coordiniates,y_coordinates, z coordinates and distance
    while i<len(t):
        if t[i].isdigit(): # when t[i]=0,1,2,3,4,5,6,7,8,9
         m=str(t[i])
         while t[i+1].isdigit():
            m+=t[i+1]
            i=i+1
         s_.push(int(m)) # pushing integer s_ stack
         n*=int(m) 
        if t[i]==")" and not s_.isempty(): # if there is closed bracket then divide by previous multiplier
            n=n//(s_.pop())
        if t[i]=="+": # if there is "+" then increment the coordinate
            if t[i+1]=="X":
                d+=n
                if sx.isempty():
                     sx.push(1*n)
                else:
                     sx.push(sx.pop()+n*1)
            if t[i+1]=="Y":
                d+=n
                if sy.isempty():
                    sy.push(1*n)
                else:
                    sy.push(sy.pop()+n*1)    
            if t[i+1]=="Z":
                d+=n
                if sz.isempty():
                    sz.push(1*n)
                else:
                    sz.push(sz.pop()+n)
        elif t[i]=="-": # if there is "-" then decrement the coordinate
            if t[i+1]=="X":
                d+=n
                if sx.isempty():
                    sx.push((-1)*n)
                else:
                     sx.push(sx.pop()+n*(-1))
            if t[i+1]=="Y":
                d+=n
                if sy.isempty():
                    sy.push((-1)*n)
                else:
                    sy.push(sy.pop()+n*(-1))    
            if t[i+1]=="Z":
                d+=n
                if sz.isempty():
                    sz.push((-1)*n)
                else: 
                    sz.push(sz.pop()+n*(-1)) 
        i=i+1 # incrementing index
    return [sx.top(),sy.top(),sz.top(),d]
