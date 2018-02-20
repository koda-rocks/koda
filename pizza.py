'''
1. Read the inputs from the file
2. MVP
'''
import numpy as np


rows = 3
columns = 5
minimum = 1
maximum = 6


row1 = ['T', 'T', 'T', 'T', 'T']
row2 = ['T', 'M', 'M', 'M', 'T']
row3 = ['T', 'T', 'T', 'T', 'T']


pizza = np.array([row1, row2, row3])

# recursion
# def count_occurrence_of(arr):
#     unique, counts = np.unique(arr, return_counts=True)
#     least_spice, least_spice_total = sorted(list(zip(unique,counts)), key=lambda pair: pair[1])[0]
#     spices_and_count = dict(tuple(zip(unique, counts)))
#
#     max_possible_valid_slices = least_spice_total // minimum
#     # first minimum occurrence of the least_spice
#     # position
#     start_positions = [[0, 0]]
#     end_positions = []
#     minimum_spice = []
#     while (len(minimum_spice) < minimum):
#
#         for spice in np.nditer(arr[start_positions[-1]]):
#             if (spice == least_spice):
#                 minimum_spice.append(spice)
#
#
# def find_positions(np_arr, least_spice, start_positions=[(0,0)], end_positions=[]):
#     end_position = list(end_positions[-1])
#     if end_positions and (np_arr[list(end_positions[-1][0]), list(end_positions[-1][1])] == ):
#         return start_positions, end_positions
#     minimum_spice = []
#     while (len(minimum_spice) < minimum):
#         start_position = list(start_positions[-1])
#         for spice in np.nditer(np_arr[start_position[0], start_position[1]]):
#             if (spice == least_spice):
#                 minimum_spice.append(spice)
#
#
#
# def find_positions_2(np_arr, least_spice):
#     match = False
#     x, y = 0, 0
#     test_x, test_y = minimum, 0
#     test_start = slice(test_x, test_y)
#     unique, counts = np.unique(np_arr[test_start], return_counts=True)
#     spices_and_count = dict(tuple(zip(unique, counts)))
#     while not match:
#         if spices_and_count.get(least_spice) == minimum:
#             match = True


def main(np_arr):
    # np_arr = np.transpose(np_arr)
    # print(np_arr)
    start_positions = []
    end_positions = []
    start_x = 0
    start_y = 0
    end_x = 0
    end_y = 0
    for index, spice_position in enumerate(np.nditer(np_arr)):
        print(np_arr[start_x:end_x, start_y:end_y])

        # print(np_arr[0:3, 0:3])
        print('------------------------------')
        # print(index)
        # pizza_slice = slice()
        # minimum_for_each_slice, maximum_for_both_slices = calculate_requirements(len(start_positions))
        # if check_array_slice_for_minimum_condition(pizza_slice, minimum_for_each_slice, maximum_for_both_slices):
        #     pass
        # print(check_array_slice_for_minimum_condition(np_arr[start_x:end_x, start_y:end_y], minimum, maximum))
        if check_array_slice_for_minimum_condition(np_arr[start_x:end_x, start_y:end_y], minimum, maximum):
            start_positions.extend([start_x, end_x - 1])
            end_positions.extend([start_y, end_y - 1])
            start_y = end_y
            end_x = start_x + minimum
            end_y = start_y + minimum
            # print("x", end_x)
            # print("y", end_y)
        # check if the slice is too big
        elif np_arr[start_x:end_x, start_y:end_y].size >= maximum:
            # start_x += 1
            if start_x > start_y:
                start_y += 1
            else:
                start_x += 1
        else:
            if end_x > end_y:
                end_y += 1
            else:
                end_x += 1


    result = zip(start_positions, end_positions)
    print(list(result))


def calculate_requirements(number_of_slices_got):
    minimum_for_each_slice = number_of_slices_got * minimum
    maximum_for_both_slices = number_of_slices_got * maximum
    result = (minimum_for_each_slice, maximum_for_both_slices)
    return result


def check_array_slice_for_minimum_condition(pizza_slice, minimum_for_each_slice, maximum_for_both_slices):
    unique, counts = np.unique(pizza_slice, return_counts=True)
    spices_and_count = dict(zip(unique, counts))
    tomato_count = spices_and_count.get('T', None)
    mushroom_count = spices_and_count.get('M', None)
    # print(tomato_count)
    # print(mushroom_count)
    # import pdb;pdb.set_trace()
    if not (mushroom_count and tomato_count):
        return False
    pizza_slice_count = tomato_count + mushroom_count
    slice_is_satisfied = (tomato_count >= minimum_for_each_slice) and (mushroom_count >= minimum_for_each_slice) and (pizza_slice_count < maximum_for_both_slices)
    return slice_is_satisfied

main(pizza)