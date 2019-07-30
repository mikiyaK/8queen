import sys, time

class Queue:

    def __init__(self):
        raise NotImplementedError

    def extend(self, items):
        for item in items:
            self.append(item)

def Stack():
    """Return an empty list, suitable as a Last-In-First-Out Queue."""
    return []

class FIFOQueue(Queue):

    """A First-In-First-Out Queue."""

    def __init__(self):
        self.A = []
        self.start = 0

    def append(self, item):
        self.A.append(item)

    def __len__(self):
        return len(self.A) - self.start

    def extend(self, items):
        self.A.extend(items)

    def pop(self):
        e = self.A[self.start]
        self.start += 1
        if self.start > 5 and self.start > len(self.A)/2:
            self.A = self.A[self.start:]
            self.start = 0
        return e

    def __contains__(self, item):
        return item in self.A[self.start:]



def expand(node,process):
    list = []
    for i in range(1,9):
        judge = 1
        for j in range(1,node[0]+1):
            for k in process:
                if k[0] == j:
                    a = k[1]
                    break
            if ((i == a) or (i == a+node[0]+1-j) or (i == a-node[0]-1+j)):
                judge = 0
                break
        if (judge == 1):
            list.append((node[0]+1, i))
    return list
            
    
    

candidate = Stack()
process = Stack()
answer = FIFOQueue()
for i in range(8):
    candidate.append((1,i))
    
while candidate:
    node = candidate.pop()
    process.insert(0, node)
    if (node[0] == 8):
        break
    candidate += expand(node,process)
for j in range(1,9):
    for k in process:
        if k[0] == j:
            answer.append(k)
            break
for i in range(1,9):
    queen = answer.pop()
    print("")

    for j in [1,2,3,4,5,6,7,8]:
    
        if (j == queen[1]):
            sys.stdout.write("Q ")
        else:
            sys.stdout.write("* ")

    sys.stdout.write("\n")
    sys.stdout.flush()

    

    
