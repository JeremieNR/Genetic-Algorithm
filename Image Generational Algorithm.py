import random
from PIL import Image
import numpy as np
import math

array = []
child = ""
sequence_length = 1600
square_length = int(math.sqrt(int(sequence_length)))


#---Function to Make 1 sequence of Genetic code---
def make_child():
    array = []
    for x in range(sequence_length):
        array.append(random.randint(0,1))
        child = ''.join(map(str, array))
    print(child)
    return child


#---Make multiple sequences of Genetic code---
def make_children(p):
    for x in range(p):
        make_child()


#---Make 5 images of Child's Genetic code as test---
for k in range(5):
    value = make_child()

    cmap = {'0': (255,255,255),
            '1': (0,0,0)}

    data = [cmap[letter] for letter in value]
    img = Image.new('RGB', (square_length, len(value)//square_length), "white")
    img.putdata(data)
    img.show()   


