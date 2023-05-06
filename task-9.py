


'''

>>> string = "abracadabra"
>>> l = list(string)
>>> l[5] = 'k'
>>> string = ''.join(l)
>>> print string
abrackdabra

'''











def mutate_string(string, position, character):
    
    l = list(string)
    
    l[position] = character
    
    w = " ".join(l)
    
    return w



s = input("Enter the string :")
i, c = input("Enter num plus the char :").split()
s_new = mutate_string(s, int(i), c)
print(s_new)

