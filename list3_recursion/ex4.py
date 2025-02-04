print("||| Exercise 4 - Find the index of the highest element |||")

list_n = [1,7,8,3,10,11,9]

def high_number(n_list, index = 0, max_index = 0):
    if len(n_list) == index:
        return max_index
    if n_list[index] > n_list[max_index]:
        max_index = index        
    return high_number(n_list, index + 1, max_index)

print(f"Now we are going to show the index of the highest number in the list {list_n}:")
print(high_number(list_n))
