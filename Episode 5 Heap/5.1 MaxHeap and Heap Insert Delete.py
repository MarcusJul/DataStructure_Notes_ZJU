# Complete binary tree
# Heap is a CBT that can be represented by array
# Max Heap (the largest value in the parent), Min Heap vice versa
# 
class Node(object):
    def __inti__(self, data):
        self.data = data
        self.right, self.left = None, None

class Heaper(object):
    def __init__(self,
                 array, # the array (use list in Python) that coordinates with the structure of the CBT
                 capacity# the maximum number of values that the heap can hold
                 ):
        self.Create()
    
    def Create(self, capa):
        self.capa = capa
        self.size = 0
        self.array = [capa] # set capa as the first element of the array
    
    def IsFull(self):
        return True if self.size>=self.capa else False
    
    def IsEmpty(self):
        return True if self.size==0 else False
        
    def Insert(self, data):
        if self.IsFull():
            print("The Heap is full")
            return 
        else:
            self.size+=1
            i = self.size
            while(self.array[int(i/2)]<data):# No need to add "and i>1" because the first item is the max capacity
                self.array[i] = self.array[int(i/2)]
                i = int(i/2)
            self.array[i] = data
            
    def DeleteMax(self, data):
        if self.IsEmpty():
            print("The CBT is empty.")
        else:
            MaxItem = self.array[1]
            self.size-=1
            temp = self.array[self.size]
            parent = 1
            # for a parent at i, the left child is at 2i and right at 2i+1
            # if left child doesnt exist then right child ofc wont exist
            while(parent*2<=self.size): 
                child = parent*2 
                # find the larger child
                # if child == size means child is the last element, hence no right child
                if child != self.size and self.array[child]<self.array[child+1]:
                    child+=1
                else:
                    if temp>=self.array[child]:
                        break
                    else:
                        self.array[parent] = self.array[child]
                        parent = child
                
                    
            