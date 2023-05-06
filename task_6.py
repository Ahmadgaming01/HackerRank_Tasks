'''
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
'''



if __name__ == '__main__':
    N = int(input("Enter the range :"))
    
    T_List = []
    R_list = []

    for i in range(N):
        f_Input = input( "enter the function and number :" ).split()
        print(f_Input)
        T_List.append(f_Input)
        
    for f_Input in T_List:
        if f_Input[0] == "insert":
            R_list.insert(int(f_Input[1]),int(f_Input[2]))
'''
        elif f_Input[0] == "print":
            print(R_list)

        elif f_Input[0] == "remove":
            R_list.remove(int(f_Input[1]))
        elif f_Input[0] == "append":
            R_list.append(int(f_Input[1]))
        elif f_Input[0] == "sort":
            R_list.sort()
        elif f_Input[0] == "pop":
            R_list.pop()
        elif f_Input[0] == "reverse":
            R_list.reverse()
'''

