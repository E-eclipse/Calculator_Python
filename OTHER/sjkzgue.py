
#! 1
def nums_sum(numbers):
    summa = 0
    for i in numbers:
        summa += i
    return summa

print(nums_sum([1, 2, 3, 4, 5]))

#! 2
def bigest_num(numbers):
    bigest = 0
    for i in numbers:
        if i > bigest:
            bigest = i
    
    return bigest

print(bigest_num([1, 2, 67, 4, 5]))

#! 3
def bez_dub(numbers):
    return list(set(numbers))

print(bez_dub([1, 2, 3, 4, 5, 2, 5, 10]))

#! 4
def list_list(numbers, numbers2):
    return numbers + numbers2

print(list_list([1, 2, 3, 4, 5], [5, 7, 34, 7]))

#! 5 
def in_tuple(nums, number):
    return nums.index(number)

print(in_tuple((1, 2, 3), 2))


#! 6
def tuple_tuple(num, num2):
    return num + num2

print(tuple_tuple((1, 2, 3), (1, 3, 4, 5)))

#! 7 
def bez_elem(numbers, a):
    return tuple(list(numbers).remove(a))

print(bez_elem((1, 2, 3), 2))

#! 8
def count_elem(numbers, a):
    return list(numbers).count(a)

print(count_elem((1, 2, 3, 2, 3, 2), 2))
