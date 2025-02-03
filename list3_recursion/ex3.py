print("||| Exercise 3 - Counting characters in a string |||")
import re

def onechar():
     while True:
        char = input("Type one character: ")
        if re.fullmatch(r".", char):  # Verifica se há exatamente um caractere
            return char
        else:
            print("Invalid answer. Type only one character")

def count_char(stri, chara):
    sumc=0
    if len(stri) == 0:
        return 0
    if stri[-1] == chara:
        sumc+=1
    return sumc + count_char(stri[:-1],chara) 

string = input("Type anything: ").lower().strip()
char = onechar()
print(f"Now we are going to show how many '{char}' there are in the string '{string}':")
print(count_char(string, char))