print("||| Exercise 1 - Reverse string |||")

def reverse_string(stri):
    if len(stri) == 0:
        return stri
    return stri[-1] + reverse_string(stri[:-1]) 

string = input("Type anything: ")
print("Now we are going to show you what you writed but reversed:")
print(reverse_string(string))
