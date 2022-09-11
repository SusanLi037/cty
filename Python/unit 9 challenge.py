import random
original_list = []
for i in range(0, 100):
    original_list.append(random.randint(0, 100))
even_list = []
def even():
    for j in range(0, len(original_list)):
        if original_list[j] % 2 == 0:
            even_list.append(original_list[j])
        elif original_list[j] % 2 == 1:
            continue
    return(even_list)
odd_list = []
def odd():
    for j in range(0, len(original_list)):
        if original_list[j] % 2 == 1:
            odd_list.append(original_list[j])
        elif original_list[j] % 2 == 0:
            continue
    return(odd_list)
even()
odd()
print("Original list: {}, {} numbers".format(original_list, len(original_list)))
print()
print("Even list: {}, {} numbers".format(even_list, len(even_list)))
print()
print("Odd list: {}, {} numbers".format(odd_list, len(odd_list)))
