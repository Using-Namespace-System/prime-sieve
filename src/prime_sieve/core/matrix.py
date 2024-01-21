from prime_sieve.util.visuals import visual
import numpy as np
import math

def flatten(input_data, input_cols, input_rows):
    y,x = input_data
    flat = (x+(input_cols*(y))).astype(int)
    mask = (flat<(input_cols * input_rows))
    x = np.zeros(flat.shape)
    return (flat,x, mask)

def drop(input_data, input_cols, count):
    y,x = input_data
    x[count-2] = -1
    keep = ((x != (input_cols-1)))
    return (keep)

def expand(input_data, input_cols, input_rows, count, mask):
    y,x = input_data
    new_y = np.divide(y,input_cols).astype(int)
    new_x = y % input_cols
    mask = mask & ((new_y < input_rows) & drop((new_y,new_x), input_cols, count))
    new_x[count-2] = (input_cols-1)
    return (new_y[mask],new_x[mask])


class sieve_matrix:
    coordinates = ()
    values = []
    shape = ()

    def __init__(self, size: int):
        self.shape = (size,2)
        self.y = np.arange(0,(((size-1)*2)+1),2,dtype=int)
        self.y[0] = 1
        self.values = self.y
        self.x = np.zeros(self.y.shape)
        #start with sparse x and y coordinates of a 2 dimentional binary matrix
        #where the first dimension and the first item in dimension 2 are set to 1
        self.mask = self.x == 0
        self.size = size * 2
        self.new_cols = 3
        self.count = self.new_cols
        self.new_rows = int(self.size/self.new_cols)
        new_y = np.divide(self.y,2).astype(int)
        new_x = self.y % 2
        self.coordinates = (new_y,new_x)
        

    def advance(self):
        #select the next noonzero element as n
        #shift coordinates n dimensional
        #all but the first item in dimension n is set to 0
        self.y, self.x = expand((self.y,self.x), self.new_cols, self.new_rows, self.count, self.mask)
        self.shape = (self.new_rows,self.new_cols)
        self.coordinates = (self.y,self.x)
        self.y, self.x, self.mask = flatten((self.y,self.x),self.new_cols, self.new_rows)
        self.values = self.y + 1
        self.size = self.new_cols * self.new_rows
        self.new_cols = self.y[self.count-1] + 1
        self.count += 1
        self.new_rows = int(self.size/self.new_cols)

    def display(self):
        visual(self.coordinates,self.values,self.shape)
