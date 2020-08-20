# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

stack = []
string = ""

while n:
    std_input = input()
    step = std_input.split()[0]
    
    if step =="1":
        value = std_input.split()[1]
        if stack ==[]:
            string = value
            stack.append(string)
        else:
            string = stack[-1] + value
            stack.append(string)
            #print (stack)
            #print (string)
    
    elif step=="2":
        value = std_input.split()[1]
        k = int(value)
        string = stack[-1]
        string = string[:len(string)-k]
        stack.append(string)
        #print (stack)
        #print (string)
    
    elif step=="3":
        value = std_input.split()[1]
        #print (step,value)
        index = int(value)-1
        last_stack = stack[-1]
        #print (stack)
        print (last_stack[index])

    else:
        stack.pop()
        #print (stack)
    n = n-1
