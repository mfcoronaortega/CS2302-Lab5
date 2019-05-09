#Course: CS 2302 Data Structures | Spring 2019
#Author: Maria Fernanda Corona Ortega
#Assignment: Lab 5
#Instructor: Olac Fuentes
#Purpose of Code: The purpose of this code is to explore the implementation
#of binary search trees and Hash tables in order ot explore what is 
#Natural Language Processing
#Last Modification: 4/1/2019

# Implementation of hash tables with chaining using strings
import numpy as np
import timeit

class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right      
        
def Insert(T,newItem):
    if T == None:
        T =  BST(newItem)
    elif T.item > newItem:
        T.left = Insert(T.left,newItem)
    else:
        T.right = Insert(T.right,newItem)
    return T

def Delete(T,del_item):
    if T is not None:
        if del_item < T.item:
            T.left = Delete(T.left,del_item)
        elif del_item > T.item:
            T.right = Delete(T.right,del_item)
        else:  # del_item == T.item
            if T.left is None and T.right is None: # T is a leaf, just remove it
                T = None
            elif T.left is None: # T has one child, replace it by existing child
                T = T.right
            elif T.right is None:
                T = T.left    
            else: # T has two chldren. Replace T by its successor, delete successor
                m = Smallest(T.right)
                T.item = m.item
                T.right = Delete(T.right,m.item)
    return T
         
def InOrder(T):
    # Prints items in BST in ascending order
    if T is not None:
        InOrder(T.left)
        print(T.item,end = ' ')
        print()
        InOrder(T.right)
  
def InOrderD(T,space):
    # Prints items and structure of BST
    if T is not None:
        InOrderD(T.right,space+'        ')
        print(space,T.item)
        InOrderD(T.left,space+'        ')
  
def SmallestL(T):
    # Returns smallest item in BST. Returns None if T is None
    if T is None:
        return None
    while T.left is not None:
        T = T.left
    return T   
 
def Smallest(T):
    # Returns smallest item in BST. Error if T is None
    if T.left is None:
        return T
    else:
        return Smallest(T.left)

def Largest(T):
    if T.right is None:
        return T
    else:
        return Largest(T.right)   

def Find(T,k):
    # Returns the address of k in BST, or None if k is not in the tree
    if T is None or T.item == k:
        return T
    if T.item<k:
        return Find(T.right,k)
    return Find(T.left,k)
    
def FindAndPrint(T,k):
    f = Find(T,k)
    if f is not None:
        print(f.item,'found')
    else:
        print(k,'not found')

def FindHeight(T):
    ct = 1
    if T.left is None:
        return ct
    else:
        ct += FindHeight(T.left)
    return ct
 
##############################################################################       
        
def MyBST():
    file = open("test_text.txt",'r') 
    T = None
    NodeCT = 0
    start = timeit.default_timer()  
    for line in file:
        L = []
        a = np.array([])
        tmp = []
        tmp = line.split(' ',1)
        a = tmp[1].split(' ')
        for i in a:
            float(i)
        if ord(tmp[0][0]) > 65:
            L.append(tmp[0])
            L.append(a)
            print(L[:])
            T = Insert(T,L)
            NodeCT += 1
    stop = timeit.default_timer() 

    print('Binary Search Tree stats:')     
    print('Number of nodes:', NodeCT)
    print('Height:', FindHeight(T))
    print('Running Time of Binary search tree construction: ', stop - start,'s\n')
#    print('Reading word file to determine similarities\n')
    
#    file2 = open("simword_test.txt",'r') 
##    print(file2.read())
#    L = []
#    
#    print('Word similarities found:\n')
#    start2 = timeit.default_timer()  
#    for line in file2:
#        tmp = []
#        tmp = line.split(' ')
#        sim_val = sim(tmp[0],tmp[1])
#         
#        print('- Similarity',tmp[0],tmp[1], sim_val)
#        L.append(tmp)
#    stop2 = timeit.default_timer()
#    print(L[:])
#    print(InOrder(T))
#    print(InOrderD(T,' '))
#    print('Running time for binary search tree query processing:', stop2 - start2,'s\n')  


#def sim(w1, w2):
#        return 0

##############################################################################

class HashTableC(object):
    # Builds a hash table of size 'size'
    # Item is a list of (initially empty) lists
    # Constructor
    def __init__(self,size, num_items = 0 ):  
        self.item = []
        self.num_items = num_items
        for i in range(size):
            self.item.append([])
        
def InsertC(H,k,l):
    # Inserts k in appropriate bucket (list) 
    # Does nothing if k is already in the table
    b = h(k,len(H.item))
    H.item[b].append([k,l]) 
   
def FindC(H,k):
    # Returns bucket (b) and index (i) 
    # If k is not in table, i == -1
    b = h(k,len(H.item))
    for i in range(len(H.item[b])):
        if H.item[b][i][0] == k:
            return b, i, H.item[b][i][1]
    return b, -1, -1
 
def h(s,n):
    r = 0
    for c in s:
        r = (r*255 + ord(c))% n
    return r

def load_factor(H):
    return H.num_items / len(H.item)

##############################################################################
def MyHT():
    file = open("test_text.txt",'r') 
#    print("Output of Readline function is :")
    size = 50
    H = HashTableC(size)  
    start = timeit.default_timer()  
    for line in file:
        L = []
        a = np.array([])
        tmp = []
        tmp = line.split(' ',1)
        a = tmp[1].split(' ')
        for i in a:
            float(i)
        if ord(tmp[0][0]) > 65:
            L.append(tmp[0])
            L.append(a)
#            print(L[:])
            InsertC(H,L[0],len(L))
            H.num_items += 1
#            print(H.item)
#            print(L[0],FindC(H,L[0]))
    stop = timeit.default_timer()
    
    print('Hash table stats:')    
#    print('Initial table size:')
    print('Final table size:', len(H.item))
    print('Load factor:', load_factor(H))
#    print('Percentage of empty lists:')
#    print('Standard deviation of the lengths of the lists:')
    print('Running Time of Hash Table construction: ', stop - start,'s\n')

#    print('Reading word file to determine similarities\n')
    
#    file2 = open("simword_test.txt",'r') 
##    print(file2.read())
#    L = []
#    
#    print('Word similarities found:\n')
#    start2 = timeit.default_timer()  
#    for line in file2:
#        tmp = []
#        tmp = line.split(' ')
#        sim_val = sim(tmp[0],tmp[1])
#         
#        print('- Similarity',tmp[0],tmp[1], sim_val)
#        L.append(tmp)
#    stop2 = timeit.default_timer()
#    print(L[:])
#    print(InOrder(T))
#    print(InOrderD(T,' '))
#    print('Running time for binary search tree query processing:', stop2 - start2,'s\n')    
    
##########################PROGRAM IMPLEMENTATION##############################

#user = input('Choose table implementation \nType 1 for binary search tree or 2 for hash table with chaining\n')

#if user is '1':
#    print('Choice:', user, '\n\nBuilding binary search tree\n\n')
#MyBST()

#if user is '2':
#    print('Choice:', user, '\n\nBuilding hash table with chaining\n\nHash table stats:\n')
MyHT()

