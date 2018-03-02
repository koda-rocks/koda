import sys

cars = {}
fleets = {}


def initialize_cars(number_of_cars):
    while number_of_cars:
        cars[number_of_cars-1] = (0,0,0)
        number_of_cars -= 1

def write_result_to_file(fleets, filename):
    with open(filename, 'w') as f:
        for fleet in fleets:
            f.write(str(fleet) + ' ' + ' '.join( str(e) for e in fleets[fleet] ) + '\n')

def move(x1, y1, x2, y2, start_step, finish_step, current_step, car_number):
    min_steps = check_distance(x1, y1, x2, y2)
    if start_step > current_step:
      current_step = start_step
    if finish_step >= current_step + min_steps:
      current_step = min_steps + current_step
    cars[car_number] = (x2, y2, current_step)
    return cars


def check_distance(x1, y1, x2, y2):
    if x1 == x2:
        return abs(y2 - y1)
    if y1 == y2:
        return abs(x2 - x1)
    min_steps = abs(x1 - x2) + abs(y1 - y2)
    return min_steps

def get_nearest_car(x1, y1, x2, y2, start_step, finish_step):
    nearest = cars[0]
    min_steps = check_distance(x1, y1, x2, y2)
    nearest_car_number = 0
    for car in cars:
        nearest_x, nearest_y, nearest_current_step = nearest
        nearest_distance = check_distance(nearest_x, nearest_y, x1, y1)
        car_x, car_y, current_step = cars[car]
        car_distance = check_distance(car_x, car_y, x1, y1)
        current_step += car_distance
        nearest_current_step += nearest_distance
        if start_step > current_step:
            current_step = start_step
        if car_distance < nearest_distance:
            if current_step <= nearest_current_step :
                nearest = cars[car]
                nearest_car_number = car
    # If at the end, the nearest car can never complete the trip, use car-0
    # so that it will be the one taking all impossible trips, giving chances for other cars to 
    # utilize there available steps
    if finish_step < nearest[2] + min_steps:
        nearest_car_number = 0
    return nearest_car_number


def assign_car(ride_turple):
    ride_number, ride = ride_turple[0], ride_turple[1]
    x1,y1,x2,y2,start_step,finish_step = ride
    nearest_car = get_nearest_car(x1,y1,x2,y2,start_step,finish_step)
    current_step = cars[nearest_car][2]
    if nearest_car in fleets:
        fleets[nearest_car].append(ride_number)
    else:
        fleets[nearest_car] = [ride_number]
    move(x1,y1,x2,y2,start_step,finish_step,current_step,nearest_car)


def sorter(ride_turple):
    sorter = check_distance(0, 0, ride_turple[1][0], ride_turple[1][1])
    return sorter

def main():
    np_array = []
    data_file = sys.argv[1]
    with open(data_file) as f:
        for index, line in enumerate(f):
            if index == 0:
                # details = line.split()
                rows, columns, number_of_cars, number_of_rides, bonus, max_step = [ int(char) for char in line.split()  ]
                initialize_cars(number_of_cars)
            else:
                ride = (index - 1, list(map(int, line.split())))
                np_array.append(ride)
    np_array = sorted(np_array, key=sorter)
    for index, element in enumerate(np_array):
        assign_car(element)
    filename = data_file.replace('in', 'txt')
    write_result_to_file(fleets, filename)
    return fleets

if __name__ == '__main__':
    # initialize_cars(3)
    # move(2,0,3,4,3,8,0,1)
    # move(2,0,2,4,3,8,0,0)
    # move(2,0,2,3,3,8,0,2)
    # print('Cars', cars)
    # print(nearest_car(0,0,1,3,2,9))
    print(main())