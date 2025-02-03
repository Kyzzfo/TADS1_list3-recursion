print("||| Exercise 2 - Sum numbers in a list |||")

def sumlist(nlist):
    sumn=0
    for number in nlist:
        if isinstance(number, list):
                sumn += sumlist(number)
        else:
            sumn += number
    return sumn
    
nest_list = [3,2,[11,30,3],1,[1,2],32,[1,2,[3,4,5]]]
print("Now we are going to show you what you writed but reversed:")
print(sumlist(nest_list))
