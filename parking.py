def parking(rate, regular_slots, priority_slots, vip_slots):

    slots_left_dict = {'Regular': regular_slots, 'Priority': priority_slots, 'VIP': vip_slots}
    multiplier = {'Regular':rate , 'Priority':rate*2, 'VIP': rate*3}
    cars = []

    def print_list():
        i = 0
        def next():
            nonlocal i
            car = cars[i]
            print(f"car: {car[0]}, parking type: {car[1]}, parking time: {car[2]}")
            i += 1

        def end():
            return i >= len(cars)
        return {'next': next, 'end': end}

    def print_parking(slot):
        if slot not in slots_left_dict:
            return "invalid classifier"
        for car in cars:
            if slot == car[1]:
                print(f"car: {car[0]}, parking time: {car[2]}")
        return

    def next_time():
        for car in cars:
            car[2] += 1

    def start_parking(car_num,classifier):

        if slots_left_dict[classifier] > 0:
            slots_left_dict[classifier] -= 1
            cars.append([car_num,classifier,0])
        else:
            print(classifier + " parking is full")

    def end_parking(car_num):
        for car in cars:
            if car[0] == car_num:
                cars.remove(car)
                slots_left_dict[car[1]] += 1
                print(f"car: {car[0]}, parking type: {car[1]}, parking time: {car[2]}")
                print(f"payment: {multiplier[car[1]] * car[2]}")
                return
        return "car not found"
    return {
        'print_list': print_list,
        'print_parking': print_parking,
        'next_time': next_time,
        'start_parking': start_parking,
        'end_parking': end_parking
    }