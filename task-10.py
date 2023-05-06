


#here is the format output
'''
Output Format

Output the integer number indicating the total number of occurrences of the substring in the original string.
'''

# here is the test on my IDLE 


'''
s = "llbue"
sb ="b"


find_s = s.find(sb)



print(find_s)




# here is the task on hackerRank



def count_substring(string, sub_string):
    result = string.find(sub_string)
    return result

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)







def count_substring(string, sub_string):
    index = [x for x in range(len(string)) if string.startswith(sub_string,x)]   #ABCDCDC
    x = len(index)
    print(x)
    print(index)
'''

'''    
    return x

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)


    
# finish the task

'''

string = "ABCDCDCCDC"
sub_string ='CDC'

index = [x for x in range(len(string)) if string.startswith(sub_string,x)]   #ABCDCDC
x = len(index)

print(x)
'''

string = "ABCDCDCCDC"
sub_string ='CDC'

x = len(string)
s = []
for x in range(len(string)):

    if string.startswith(sub_string,x):
        s.append(x)        

print(s)
print(len(s))
'''

































