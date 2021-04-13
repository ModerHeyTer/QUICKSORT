class Counter():
    count = 0
    def __init__(self):
        self.count = 0

    def increase(self):
        self.count += 1



def quickSort_with_iter(alist):
   counter = Counter()
   quickSortHelper(alist,0,len(alist)-1, counter)
   return alist, counter.count

def quickSortHelper(alist,first,last, counter):
   counter.increase()
   if first<last:

       splitpoint = partition(alist,first,last, counter)

       quickSortHelper(alist,first,splitpoint-1, counter)
       quickSortHelper(alist,splitpoint+1,last, counter)


def partition(alist,first,last, counter):
   counter.increase()
   pivotvalue = alist[first]
   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and \
               alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and \
               rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark
