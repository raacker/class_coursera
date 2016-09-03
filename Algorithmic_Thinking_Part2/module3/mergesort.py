import time

def merge_in_last_one(given_list):
    if len(given_list) == 1:
        return given_list

    left_list = merge_in_last_one(given_list[:len(given_list)/2])
    right_list = merge_in_last_one(given_list[len(given_list)/2:])

    new_list = []

    left_index = 0
    right_index = 0
    while len(left_list) != 0:
        if len(right_list) == 0:
            new_list += left_list
            break
        else:
            if left_list[0] > right_list[0]:
                new_list.append(right_list.pop(0))
            else:
                new_list.append(left_list.pop(0))

    if len(right_list) != 0:
        new_list += right_list

    return new_list

def merge_in_second_one(given_list):
    if len(given_list) == 2:
        if given_list[0] > given_list[1]:
            temp = given_list[0]
            given_list[0] = given_list[1]
            given_list[1] = temp
        return given_list

    left_list = merge_in_last_one(given_list[:len(given_list)/2])
    right_list = merge_in_last_one(given_list[len(given_list)/2:])

    new_list = []

    left_index = 0
    right_index = 0
    while len(left_list) != 0:
        if len(right_list) == 0:
            new_list += left_list
            break
        else:
            if left_list[0] > right_list[0]:
                new_list.append(right_list.pop(0))
            else:
                new_list.append(left_list.pop(0))

    if len(right_list) != 0:
        new_list += right_list

    return new_list

def merge_in_fourth_one(given_list):
    if len(given_list) <= 4:
        for x_index in range(len(given_list)):
            min_element = min(given_list[x_index:])
            given_list[x_index] = min_element
        return given_list

    left_list = merge_in_last_one(given_list[:len(given_list)/2])
    right_list = merge_in_last_one(given_list[len(given_list)/2:])

    new_list = []

    left_index = 0
    right_index = 0
    while len(left_list) != 0:
        if len(right_list) == 0:
            new_list += left_list
            break
        else:
            if left_list[0] > right_list[0]:
                new_list.append(right_list.pop(0))
            else:
                new_list.append(left_list.pop(0))

    if len(right_list) != 0:
        new_list += right_list

    return new_list



start = time.time()
print merge_in_last_one([7,6,10,20,30,40,50,60,5,4,3,2,1])
end = time.time()

print end-start

start = time.time()
print merge_in_second_one([7,6,10,20,30,40,50,60,5,4,3,2,1])
end = time.time()

print end-start

start = time.time()
print merge_in_fourth_one([7,6,10,20,30,40,50,60,5,4,3,2,1])
end = time.time()

print end-start

