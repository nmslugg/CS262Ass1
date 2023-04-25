# Name: Nicholas Slugg
# OSU Email: sluggn@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 1
# Due Date:
# Description: This is a series of functions from assignment 1 for reviewing the basics of python


import random
from static_array import StaticArray


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------

def min_max(arr):
    '''This function finds the minimum and maximum value of a Static Array'''

    min = arr.get(0)  # initialize minimum and maximum value to be first value in array
    max = arr.get(0)

    for i in range(arr.length()):
        if arr.get(i) > max:  # if the new value is larger than the current maximum, update
            max = arr.get(i)
        elif arr.get(i) < min:# if the new value is smaller than the current minimum, update
            min = arr.get(i)

    return (min, max)


# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------

def fizz_buzz(arr):
    '''This function takes a static array as an input and modifys the array, replacing an integer divisible by both
    5 and 3 with 'fizzbuzz', an integer only divisible by 3 with 'fizz', an integer only divisible by 5 with 'buzz',
    and all else unchanged'''

    fb_static_array = StaticArray(arr.length())  # initialize new static array

    for i in range(arr.length()):
        if (arr.get(i) % 3 == 0) and (arr.get(i) % 5 == 0):  # replace integer divisible by 3 and 5 with 'fizzbuzz'
            fb_static_array.set(i, 'fizzbuzz')
        elif arr.get(i) % 3 == 0:  # replace integer divisible by 3 only with 'fizz'
            fb_static_array.set(i, 'fizz')
        elif arr.get(i) % 5 == 0:  # replace integer divisible by 5 only with 'buzz'
            fb_static_array.set(i, 'buzz')
        else:
            fb_static_array.set(i, arr.get(i))  # for all else, leave unchanged

    return fb_static_array


# ------------------- PROBLEM 3 - REVERSE -----------------------------------

def reverse(arr):
    '''This function reverses the contents of a static array'''
    for i in range(arr.length()//2):
        temp = arr.get(arr.length() - i - 1)  # temporary value
        arr.set(arr.length() - i - 1, arr.get(i))  # update both values with the opposite
        arr.set(i, temp)


# ------------------- PROBLEM 4 - ROTATE ------------------------------------

def rotate(arr, steps):
    """This function rotates a static array"""
    rot_arr = StaticArray(arr.length())  # initialize new array

    for i in range(0, arr.length()):
        rot_arr.set(i, arr.get((i - steps) % arr.length()))  # update new array value with one 'steps' positions prior

    return rot_arr


# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------

def sa_range(start, end):
    """This function returns a static array of integers from start to end values passed"""
    sa_arr = StaticArray(abs(end - start) + 1)  # initialize static array

    if end >= start:  # if then statement to determine the direction of the integers
        d = 1   # ascending
    else:
        d = -1  # descending

    for i in range(abs(end - start) + 1):
        sa_arr.set(i, start + d*i)  # add new integer in direction

    return sa_arr


# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------

def is_sorted(arr):
    """This funtion indicates whether or not a static array is sorted, returning 1 if ascending, -1 if descending, and 0
    if not ordered"""
    num = 0  # initial value for variable

    for i in range(arr.length()-1):
        if arr.get(i) < arr.get(i + 1):
            num += 1  # adds one for each term that is ascending
        elif arr.get(i) > arr.get(i + 1):
            num += -1  # subtracts one for each term descending
        else:
            num += 0  # all other terms go to zero

    if arr.length() == 1:
        return 0  # default case of one element
    elif abs(num/(arr.length()-1)) < 1:
        return 0  # if the number has magnitude less than one, cannot be ordered, and 0 is returned
    else:
        return num//(arr.length()-1)  # if not, returns the sign of 'num'


# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------

def find_mode(arr):
    """This function finds the mode of a static array, returning its value and frequency"""

    p = 0  # initial values for keeping track of repeated values and frequencies
    max_p = 0
    n = 1
    max_n = 1

    for i in range(arr.length() - 1):
        if arr.get(i) == arr.get(i + 1):
            n += 1  # if the next value is the same, add 1 to the frequency of this value
        elif arr.get(i) != arr.get(i + 1):
            p += n  # if the next one is different, let 'p' point to the new value
            n = 1  # update current frequency to 1

        if n > max_n:  # if the new frequency is larger than the previous maximum, update index and frequency
            max_p = p
            max_n = n

    return (arr.get(max_p), max_n)

# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------

def remove_duplicates(arr):
    """This program finds duplicates in a static array, and returns a new one without them"""
    n_count = 1  # counter for unique values
    for i in range(arr.length() - 1):
        if arr.get(i) != arr.get(i+1):
            n_count += 1  # adds one for each unique value

    new_arr = StaticArray(n_count)  # initializes array for unique values with first element the first from the array
    new_arr.set(0, arr.get(0))

    n = 1  # counter for unique elements

    for i in range(1, arr.length()):
        if arr.get(i) != arr.get(i - 1):
            new_arr.set(n, arr.get(i))  # if new element, add it to new array, and increase counter
            n += 1

    return new_arr


# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------

def count_sort(arr):
    """This function sorts a static array using the count sort algorithm"""
    max = arr.get(0)  # First, find the minimum and maximum values so that we can assess the range
    min = arr.get(0)

    for i in range(1, arr.length()):  # This is similar to min, max algorithm. If an element is greater than previous maximum, update it, same with minimum.
        if arr.get(i) > max:
            max = arr.get(i)
        elif arr.get(i) < min:
            min = arr.get(i)

    count_arr = StaticArray(abs(max - min)+1)  # Array to count values of each element

    for i in range(count_arr.length()):
        count_arr.set(i, 0)  # initialize all values to 0 instead of None

    for i in range(arr.length()):
        temp = count_arr.get(arr.get(i)-min) # temporary value for previous count of an element.
        count_arr.set(arr.get(i)-min, temp + 1)  # add one for each new count

    for i in range(count_arr.length() - 1):
        temp = count_arr.get(i+1)  # temporary value for next element
        count_arr.set(i + 1, temp + count_arr.get(i))  # adds the previous elements values

    output_arr = StaticArray(arr.length())  # this is the array that is returned

    for i in range(arr.length()):
        output_arr.set(count_arr.get(arr.get(i)-min) - 1, arr.get(i))  # adds value to output array in position specified in counting array
        temp = count_arr.get(arr.get(i)-min)  # temporary value for previous count
        count_arr.set(arr.get(i)-min, temp - 1)  # subtracts one from count for next one.

    return output_arr


# ------------------- PROBLEM 10 - TRANSFORM_STRING ---------------------------

def transform_string(source, s1, s2):
    """This function takes a string as an input, and if an element is upper case, replaces it with a space, if it is
     lower case, replaces it with hashtag, if it is a digit, replaces it with !, and replaces all else with '='"""
    TStr = ''

    for i in range(len(source)):
        for j in range(len(s1)):
            if source[i] == s1[j]:
                TStr += s2[j]  # if a character is in s1, replaces it with value from s2
                break
        if source[i].isupper():  # replaces upper case characters with space
            TStr += ' '
        elif source[i].islower():  # replaces lower case characters with hashtag
            TStr += '#'
        elif source[i].isdigit():  # replaces digits with !
            TStr += '!'
        else:
            TStr += '='  # replaces others with equal signs

    return TStr


# ------------------- BASIC TESTING -----------------------------------------

if __name__ == "__main__":

    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]: 3}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 3')
    test_cases = (
        [3, 3, 3],
        [-10, -30, -5, 0, -10],
        [25, 50, 0, 10],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        result = min_max(arr)
        if result:
            print(f"Min: {result[0]: 3}, Max: {result[1]}")
        else:
            print("min_max() not yet implemented")

    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)

    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)

    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2 ** 28, -2 ** 31]:
        space = " " if steps >= 0 else ""
        print(f"{rotate(arr, steps)} {space}{steps}")
    print(arr)

    print('\n# rotate example 2')
    array_size = 1_000_000
    source = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(f'Started rotating large array of {array_size} elements')
    rotate(arr, 3 ** 14)
    rotate(arr, -3 ** 15)
    print(f'Finished rotating large array of {array_size} elements')

    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-95, -89), (-89, -95)]
    for start, end in cases:
        print(f"Start: {start: 4}, End: {end: 4}, {sa_range(start, end)}")

    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = is_sorted(arr)
        space = "  " if result and result >= 0 else " "
        print(f"Result:{space}{result}, {arr}")

    print('\n# find_mode example 1')
    test_cases = (
        [1, 20, 30, 40, 500, 500, 500],
        ['A', 'A', 'B', 'C', 'C', 'C', 'C'],
        [2, 2, 2, 2, 1, 1, 1, 1],
        ["zebra", "sloth", "otter", "otter", "moose", "koala"],
        ["Albania", "Belgium", "Chile", "Denmark", "Egypt", "Fiji"]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = find_mode(arr)
        if result:
            print(f"{arr}\nMode: {result[0]}, Frequency: {result[1]}\n")
        else:
            print("find_mode() not yet implemented\n")

    print('# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)

    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        before = arr if len(case) < 50 else 'Started sorting large array'
        print(f"Before: {before}")
        result = count_sort(arr)
        after = result if len(case) < 50 else 'Finished sorting large array'
        print(f"After : {after}")

    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')

    print('\n# transform_string example 1\n')
    original = (
        '#     #  =====  !      =====  =====  #     #  =====',
        '#  #  #  !      !      !      !   !  ##   ##  !    ',
        '# # # #  !===   !      !      !   !  # # # #  !=== ',
        '##   ##  !      !      !      !   !  #  #  #  !    ',
        '#     #  =====  =====  =====  =====  #     #  =====',
        '                                                   ',
        '         TTTTT OOOOO      22222   66666    1       ',
        '           T   O   O          2   6       11       ',
        '           T   O   O       222    66666    1       ',
        '           T   O   O      2       6   6    1       ',
        '           T   OOOOO      22222   66666   111      ',
    )
    test_cases = ('eMKCPVkRI%~}+$GW9EOQNMI!_%{#ED}#=-~WJbFNWSQqDO-..@}',
                  'dGAqJLcNC0YFJQEB5JJKETQ0QOODKF8EYX7BGdzAACmrSL0PVKC',
                  'aLiAnVhSV9}_+QOD3YSIYPR4MCKYUF9QUV9TVvNdFuGqVU4$/%D',
                  'zmRJWfoKC5RDKVYO3PWMATC7BEIIVX9LJR7FKtDXxXLpFG7PESX',
                  'hFKGVErCS$**!<OS<_/.>NR*)<<+IR!,=%?OAiPQJILzMI_#[+}',
                  'EOQUQJLBQLDLAVQSWERAGGAOKUUKOPUWLQSKJNECCPRRXGAUABN',
                  'WGBKTQSGVHHHHHTZZZZZMQKBLC66666NNR11111OKUN2KTGYUIB',
                  'YFOWAOYLWGQHJQXZAUPZPNUCEJABRR6MYR1JASNOTF22MAAGTVA',
                  'GNLXFPEPMYGHQQGZGEPZXGJVEYE666UKNE11111WGNW2NVLCIOK',
                  'VTABNCKEFTJHXATZTYGZVLXLAB6JVGRATY1GEY1PGCO2QFPRUAP',
                  'UTCKYKGJBWMHPYGZZZZZWOKQTM66666GLA11111CPF222RUPCJT')

    for case in test_cases:
        print(transform_string(case, '612HZ', '261TO'))
