class stack:
    def pop(self,l,sub):
        x = l.pop()
        if x == sub[-1]:
            sub.pop()

    def push(self,element,l,sub):
        l.append(element)
        if len(sub) == 0:
            sub.append(element)
        else:
            if element < sub[-1]:
                sub.append(element)

    def get_min(self,sub):
        print(sub[-1])
s = stack()
l = list()
sub = list()
s.push(1,l,sub)
s.push(2,l,sub)
s.push(10,l,sub)
s.push(0,l,sub)
s.push(5,l,sub)
s.push(16,l,sub)
s.pop(l,sub)
s.pop(l,sub)
s.pop(l,sub)
#s.push(0,l,sub)
s.get_min(sub)