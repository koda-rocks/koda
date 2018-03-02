'''
1. Read the inputs from the file
2. MVP
'''
import numpy as np
import sys


def calculate_pizza_slices(np_arr,rows, columns, minimum, maximum):
    positions = []
    start_positions = []
    end_positions = []
    start_x = 0
    start_y = 0
    end_x = 1
    end_y = 1
    stop = False
    # for index, spice_position in enumerate(np.nditer(np_arr)):
    while not stop:
        # if index < 10:
        #     print('-' * 20)
        #     print(start_x)
        #     print (start_y)
        #     print(end_x)
        #     print(end_y)
        #     print('-' * 20)
        if check_array_slice_for_minimum_condition(np_arr[start_x:end_x, start_y:end_y], minimum, maximum):
            # start_positions.extend([start_x, end_x - 1])
            # end_positions.extend([start_y, end_y - 1])
            positions.append((start_x, start_y, end_x - 1, end_y - 1))
            # Determine the starting position
            start_y = end_y
            end_y += 1
        # check if the slice is too big
        elif np_arr[start_x:end_x, start_y:end_y].size > maximum:
            # start_x += 1
            # start_x, start_y = x_y_axis(start_x, start_y, True)
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
            # end_x, end_y = x_y_axis(end_x, end_y)
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
            # if (end_x == end_y) and (end_x <= rows):
            #     end_x += 1
            # elif (end_x > end_y) and (end_y <= columns):
            #     end_x -= 1
            #     end_y += 1
            # else:
            #     end_x += 1
    # result = zip(start_positions, end_positions)
    # print(list(result))
    # print(len(positions))
    # print(positions)
    return (len(positions), positions)


def write_result_to_file(number_of_slices, positions, filename):
    with open(filename, 'w') as f:
        f.write(str(number_of_slices) + '\n')
        # print(number_of_slices)
        for slice_axis in positions:
            f.write(' '.join(( str(char) for char in slice_axis )) + '\n')
            # print(' '.join(( str(char) for char in slice_axis )))

# def x_y_axis(x, y, axis_start=False):
#     if x == y:
#         x+=1
#         return (x, y)
#     elif axis_start:
#         y += 1
#         return (x, y)
#     elif x > y:
#         y+=1
#         x-=1
#         return(x, y)
#     else:
#         x+=1
#         return(x, y)


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
                # details = line.split()
                rows, columns, minimum, maximum = [ int(char) for char in line.split()  ]
            else:
                np_array.append(word_to_list(line))
    np_array = np.array(np_array)
    # calculate_pizza_slices(np_array,rows, columns, minimum, maximum)
    length_of_slices, positions = calculate_pizza_slices(np_array, rows, columns, minimum, maximum)
    filename = data_file.replace('in', 'txt')
    write_result_to_file(length_of_slices, positions, filename)


def patternCreator(rows, columns, minIngredient):
    minPattern = minIngredient * 2

    if rows < minPattern and columns < minPattern:
        return (getFactors(minPattern))
    if rows < minPattern and columns >= minPattern:
        return ('y', getFactors(minPattern))
    if columns < minPattern and rows >= minPattern:
        return ('x', getFactors(minPattern))
    return ('x', 'y', getFactors(minPattern))


def getFactors(n):
    return [x for x in range(2, n//2+1) if n%x == 0]


def main2():
    np_array = []
    data_file = sys.argv[1]
    with open(data_file) as f:
        for index, line in enumerate(f):
            if index == 0:
                # details = line.split()
                rows, columns, minimum, maximum = [ int(char) for char in line.split()  ]
            else:
                np_array.append(word_to_list(line))
    np_array = np.array(np_array)

    rectPositions = rectPatterns(np_array, rows, columns, minimum, maximum)
    colPositions = colPatterns(np_array, rows, columns, minimum, maximum)
    rowPositions = rowPatterns(np_array, rows, columns, minimum, maximum)

    bestPattern, leftOver = rectPositions[0], rectPositions[1]
    lenRect = len(rectPositions[0])
    lenRow = len(rowPositions[0])
    lenCol = len(colPositions[0])
    bestPattern, leftOver = colPositions[0] if lenCol > len(bestPattern) else bestPattern, \
                            colPositions[1] if lenCol > len(bestPattern) else leftOver
    bestPattern, leftOver = rowPositions[0] if lenRow > len(bestPattern) else bestPattern, \
                            rowPositions[1] if lenRow > len(bestPattern) else leftOver

    length_of_slices = len(bestPattern)
    positions = bestPattern
    filename = data_file.replace('in', 'txt')
    leftOverFile = data_file.replace('.in', '_left.txt')
    rectFile = data_file.replace('.in', '_rect.txt')
    rectLeftFile = data_file.replace('.in', '_rect_left.txt')
    rowFile = data_file.replace('.in', '_row.txt')
    rowLeftFile = data_file.replace('.in', '_row_left.txt')
    colFile = data_file.replace('.in', '_col.txt')
    colLeftFile = data_file.replace('.in', '_col_left.txt')

    write_result_to_file(length_of_slices, positions, filename)
    write_result_to_file(length_of_slices, leftOver, leftOverFile)

    write_result_to_file(lenRect, rectPositions[0], rectFile)
    write_result_to_file('Rect Leftover', rectPositions[1], rectLeftFile)

    write_result_to_file(lenRow, rowPositions[0], rowFile)
    write_result_to_file('Row Leftover', rowPositions[1], rowLeftFile)

    write_result_to_file(lenCol, colPositions[0], colFile)
    write_result_to_file('Row Leftover', colPositions[1], colLeftFile)

def rowPatterns(np_array, rows, columns, minimum, maximum):
    new_np_array = np.copy(np_array)
    minIngredient = minimum * 2
    positions = []
    start_positions = []
    end_positions = []
    start_x = 0
    start_y = 0
    end_x = 1
    end_y = minIngredient
    stop = False

    while not stop:
        if end_y > columns and start_x > rows:
            stop = True
        if end_y <= columns:
            # print (np_array[start_x:end_x, start_y:end_y])
            if check_array_slice_for_minimum_condition(new_np_array[start_x:end_x, start_y:end_y], minimum, maximum):
                positions.append((start_x, start_y, end_x-1, end_y-1))
                hole = np.zeros(minIngredient)
                new_np_array[start_x:end_x, start_y:end_y] = hole[None,:]
                # Determine the starting position
                start_y = end_y
                end_y = start_y + minIngredient
            else:
                start_y += 1
                end_y +=1
        elif end_y > columns:
            start_y = 0
            end_y = minIngredient
            start_x += 1
            end_x +=1
    return positions, new_np_array

def colPatterns(np_array, rows, columns, minimum, maximum):
    minIngredient = minimum * 2
    positions = []
    start_x = 0
    start_y = 0
    end_y = 1
    end_x = minIngredient
    stop = False
    new_np_array = np.copy(np_array)

    while not stop:
        if end_x > rows and start_y > columns:
            stop = True
        if end_x <= rows:
            # print (np_array[start_x:end_x, start_y:end_y])
            if check_array_slice_for_minimum_condition(new_np_array[start_x:end_x, start_y:end_y], minimum, maximum):
                positions.append((start_x, start_y, end_x-1, end_y-1))
                hole = np.zeros(minIngredient)
                new_np_array[start_x:end_x, start_y:end_y] = hole[:,None]
                # Determine the starting position
                start_x = end_x
                end_x = start_x + minIngredient
            else:
                start_x += 1
                end_x +=1
        elif end_x > rows:
            start_x = 0
            end_x = minIngredient
            start_y += 1
            end_y +=1
    return positions, new_np_array

def rectPatterns(np_array, rows, columns, minimum, maximum):
    factors = getFactors(minimum*2)
    minIngredient = minimum * 2
    positions = []
    positions_and_holes = ()

    for i, factorX in enumerate(factors):
        factorY = factors[len(factors) - (i+1)]
        start_x = 0
        start_y = 0
        end_y = factorY
        end_x = factorX
        stop = False
        new_np_array = np.copy(np_array)
        new_positions = []

        # Just concentrate on rows movement, change in factors will take care of rotated rectangle
        while not stop:
            if end_y > columns and (start_x > rows or end_x > rows):
                stop = True
            if end_y <= columns:
                if check_array_slice_for_minimum_condition(new_np_array[start_x:end_x, start_y:end_y], minimum, maximum):
                    new_positions.append((start_x, start_y, end_x-1, end_y-1))
                    hole = np.zeros(factorX)
                    new_np_array[start_x:end_x, start_y:end_y] = hole[:,None]
                    # Determine the starting position
                    start_y = end_y
                    end_y = start_y + factorY
                else:
                    start_y += 1
                    end_y +=1
            elif end_y > columns:
                start_y = 0
                end_y = factorY
                start_x = end_x
                end_x += factorX
        positions = new_positions if len(new_positions) > len(positions) else positions
        positions_and_holes = (positions, new_np_array)
    return positions_and_holes

def move(x1, y1, x2, y2):
    x_max, y_max = max[x1, x2], max[y1, y2]
if __name__ == '__main__':
    main2()
