import random

p1 = "011110010000001011010110100101111010"
p2 = "100100100001011101011101101010001010"
p1_array = []
p2_array = []
p1_p2_array = []
child = ""
child_dictionary = {}


#------Turn string into array------ 
for i, p1_character in enumerate(p1):
    p1_array.append(str(p1_character))
        
for i, p2_character in enumerate(p2):
    p2_array.append(str(p2_character))


#------Go through array and randomly choose a gene over the other from the parents------
#------Make_Child Function------
def make_child():
    p1_p2_array = []
    for i in range(0, len(p1_array)):
        x = int(p1_array[i])
        y = int(p2_array[i])
        if x<y:
            p1_p2_array.append(random.randint(x,y))
        else:
            p1_p2_array.append(random.randint(y,x))
    child = ''.join(map(str, p1_p2_array))
    return int(child)


#------Create different itterations while reseting p1_p2_array------
#------Make_Children Function------
def make_children(z):
    for p in range(z):
        return make_child()
        

#------Add children to a dictionary------
def create_family(u):
    for x in range(u+1):
        child_dictionary.update({x+1:make_children(1)})
    print(child_dictionary)


create_family(20)
