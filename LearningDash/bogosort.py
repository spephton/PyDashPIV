'''hehe bogo'''
import random

def main():
    '''pylint really wants a docstring for main()?!'''
    list10 = list(range(10))
    random.shuffle(list10)
    list100 = list(range(100))
    random.shuffle(list100)
    print(list10)
    print(bogo_sort(list10)) # even this takes ages on an i9 lmao
    print(list100)
    print(bogo_sort(list100)) # nope, not waiting for this

def is_sorted(my_list):
    '''Tells you if a list is sorted'''
    if len(my_list) > 1:
        for i in range(len(my_list) - 1):
            if my_list[i] > my_list[i+1]:
                return False
    return True

def bogo_sort(my_list):
    '''Bogo sort best sort'''
    while not is_sorted(my_list):
        random.shuffle(my_list)
    return my_list

if __name__ == '__main__':
    main()
