
'''
Example of the task:

from collections import defaultdict
d = defaultdict(list)
d['python'].append("awesome")
d['something-else'].append("not relevant")
d['python'].append("language")
for i in d.items():
    print i
    
'''

from collections import defaultdict
d = defaultdict(list)

n, m = map(int, input('Enter tow Values :').split())

for i in range(n):
    a = input('Enter the list values :')
    d[a].append(i+1)



for i in range(m):
    b = input('Enter the secound values of list :')
    if len(d[b]) > 0:
        print(*d[b])
        
    else :
        print(-1)
