# Enter your code here. Read input from STDIN. Print output to STDOUT
def fn(x):
    result = 0
    for i in str(x):
        if i == "0":
            continue
        temp = 1
        for j in range(1,int(i)+1):
            temp = temp*j
        result += int(temp)
    return result

def sn(x):
    result = 0
    for i in str(x):
        result += int(i)
    return result
    
    
for _ in range(int(input())):
    numbers = input().split()
    numbers = [int(x) for x in numbers]
    result = 0
    x = 1
    hashmap = {}
    for i in range(1, numbers[0]+1):
        if i not in hashmap.values():
            while(sn(fn(x)) != i):
                hashmap[x] = sn(fn(x))
                x += 1
            hashmap[x] = sn(fn(x))
        
        position = list(hashmap.values()).index(i)
        result += sn(list(hashmap.keys())[position])
        
    print(result % numbers[1])