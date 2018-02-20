'''
1. Read the inputs from the file
2. MVP
'''
import numpy as np
import sys
import os


def calculate_pizza_slices(np_arr,rows, columns, minimum, maximum):
    positions = []
    start_x = 0
    start_y = 0
    end_x = 1
    end_y = 1
    stop = False

    while not stop:
        if check_array_slice_for_minimum_condition(np_arr[start_x:end_x, start_y:end_y], minimum, maximum):
            positions.append((start_x, start_y, end_x - 1, end_y - 1))
            start_y = end_y
            end_y += 1
        elif np_arr[start_x:end_x, start_y:end_y].size > maximum:
            if start_x < rows:
                if (start_x <= start_y) or (start_y == columns - 1):
                    start_x += 1
                else:
                    start_y += 1
            elif start_y < columns:
                start_y += 1
            else:
                stop = True
        else:
            if (end_x <= rows):
                if (end_x <= end_y) or (end_y > columns):
                    end_x += 1
                elif end_x > end_y:
                    end_x -= 1
                    end_y += 1
                else:
                    end_x += 1
            elif end_y <= columns:
                end_y += 1
            else:
                stop =  True
    return (len(positions), positions)


def write_result_to_file(number_of_slices, positions, filename):
    with open(filename, 'w') as f:
        print(number_of_slices)
        f.write(str(number_of_slices) + '\n')
        for slice_axis in positions:
            print(' '.join(( str(char) for char in slice_axis )))
            f.write(' '.join(( str(char) for char in slice_axis )) + '\n')
    print("Results have been written to file {}".format( filename))

def check_array_slice_for_minimum_condition(pizza_slice, minimum_for_each_slice, maximum_for_both_slices):
    unique, counts = np.unique(pizza_slice, return_counts=True)
    spices_and_count = dict(zip(unique, counts))
    tomato_count = spices_and_count.get('T', None)
    mushroom_count = spices_and_count.get('M', None)

    if not (mushroom_count and tomato_count):
        return False
    pizza_slice_count = tomato_count + mushroom_count
    slice_is_satisfied = (tomato_count >= minimum_for_each_slice) and (mushroom_count >= minimum_for_each_slice) and (pizza_slice_count <= maximum_for_both_slices)
    return slice_is_satisfied

def word_to_list(wrd):
    return [ char for char in wrd ][:-1]

def main():
    np_array = []
    data_file = sys.argv[1]
    with open(data_file) as f:
        for index, line in enumerate(f):
            if index == 0:
                rows, columns, minimum, maximum = [ int(char) for char in line.split()  ]
            else:
                np_array.append(word_to_list(line))
    np_array = np.array(np_array)
    length_of_slices, positions = calculate_pizza_slices(np_array,rows, columns, minimum, maximum)
    filename = data_file.replace('in', 'txt')
    write_result_to_file(length_of_slices, positions, filename)

if __name__ == '__main__':
    main()