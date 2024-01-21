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

def prime_seive(size):
    y = np.arange(0,(((size-1)*2)+1),2,dtype=int)
    y[0] = 1
    x = np.zeros(y.shape)
    #start with sparse x and y coordinates of a 2 dimentional binary matrix
    #where the first dimension and the first item in dimension 2 are set to 1
    mask = x == 0
    size = size * 2
    new_cols = 3
    count = new_cols
    new_rows = int(size/new_cols)

    while((new_rows > new_cols) ):
        #select the next noonzero element as n
        #shift coordinates n dimensional
        #all but the first item in dimension n is set to 0
        y, x = expand((y,x), new_cols, new_rows, count, mask)
        y, x, mask = flatten((y,x),new_cols, new_rows)
        size = new_cols * new_rows
        new_cols = y[count-1] + 1
        count += 1
        new_rows = int(size/new_cols)
    print(y.shape)
    return y + 1

prime_seive(10**7)