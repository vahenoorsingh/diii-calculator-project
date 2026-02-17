

def split_arr(arr):
    lst = []
    currentString = ""
    a = 0
    while a < len(arr):
        i = arr[a]
        if (i.isdigit() or i == "."):
            currentString = currentString + i
        elif i == '(':
            if currentString:
                lst.append(currentString)
                currentString = ""
            lst.append(split_arr(arr[a + 1:]))
            s = ['(']
            a += 1
            while(a < len(arr) and len(s) != 0):
                if(arr[a] == '('):
                    s.append('(')
                elif(arr[a] == ')'):
                    s.pop()
                if(len(s) != 0):
                    a+=1
        elif i == ')':
            if(currentString):
                lst.append(currentString)
            return lst
        else:
            if(currentString):
                lst.append(currentString)
            currentString = ""
            lst.append(i)
        a += 1
    if(currentString):
        lst.append(currentString)
    print(lst)
    return lst


def evaluate(arr):
    lst = split_arr(arr)
    
    tmp = 1
    i = 0
    while(i < len(lst)):
        a = lst[i]
        if isinstance(a, list):
            tmp = evaluate(a)
            del lst[i]
            lst.insert(i, tmp)
            print(lst)
        i += 1

    i = 0
    while(i < len(lst)):
        a = lst[i]
        if a == '*':
            tmp = float(lst[i-1]) * float(lst[i+1])
            del lst[i-1:i+2]
            lst.insert(i-1,str(tmp))
        elif a == '/':
            tmp = float(lst[i-1]) / float(lst[i+1])
            del lst[i-1:i+2]
            lst.insert(i-1,str(float(tmp)))
        else:
            i += 1
    
    i = 0
    while(i < len(lst)):
        a = lst[i]
        if a == '+':
            tmp = float(lst[i-1]) + float(lst[i+1])
            del lst[i-1:i+2]
            lst.insert(i-1,str(tmp))
        elif a == '-':
            tmp = float(lst[i-1]) - float(lst[i+1])
            del lst[i-1:i+2]
            lst.insert(i-1,str(float(tmp)))
        else:
            i += 1
    print(lst[0])
    return(str(lst[0]))

evaluate(input("Enter valid expression with +-/* only: "))