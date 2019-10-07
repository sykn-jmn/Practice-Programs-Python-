
def digit_number(number):
    counter = 0
    while number>0:
        number = number//10
        counter+=1
    return counter



class Heap:
    def __init__(self):
        self.heap = []

    def swap(self,a,b):
        temp = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = temp

    def insert(self,data):
        self.heap.append(data)
        self.swapup(len(self.heap)-1)



    def swapup(self,index):
        while index!=0:
            oldindex = int((index-1)/2)
            if self.heap[index] < self.heap[oldindex]:
                self.swap(oldindex,index)
                index = oldindex
            else:
                break

    def swapdown(self,index):
        leftindex = (index*2)+1
        rightindex = (index*2)+2
        if leftindex < len(self.heap):
            min = leftindex
            if rightindex < len(self.heap):
                if self.heap[rightindex]<self.heap[leftindex]:
                    min = rightindex
            if self.heap[min]<self.heap[index]:
                self.swap(min,index)
                self.swapdown(min)
            else:
                return
        else:
            return

    def pop(self):
        if len(self.heap)>0:
            head = self.heap[0]
            popped = self.heap.pop()
            if len(self.heap)>1:
                self.heap[0] = popped
            self.swapdown(0)
            return head
        else:
            return None

    def print(self):
        number = 1;
        counter = 0
        done = False
        distance = 120
        initialdistance = 60
        while done == False:
            print(' '*initialdistance, end = '')
            for i in range (0,number):
                if counter < len(self.heap):
                    print(self.heap[counter],end = ' '*(distance-(digit_number(self.heap[counter]) - 1)))
                    counter +=1
                else:
                    done = True
                    break
            digitcounter = 0
            distance = int(distance/2)
            initialdistance = initialdistance-int(distance/2)
            print()
            number = number *2









hep = Heap()
while True:
    print('Enter data: ', end = '')
    a = input()
    if a.isalpha():
        if a == 'p':
            hep.print()
        else:
            print('Popped: ', hep.pop())
            hep.print()
    else:
        hep.insert(int(a))
        hep.print()



