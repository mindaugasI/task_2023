road_length = 2000000
displacement = 20
y = 0
light_index = 0
list_of_lights = [0]
while y < road_length:
    y += displacement
    light_index += 1
    list_of_lights.append(light_index)
new_list_of_lights = list_of_lights

light_list = []
while True:
    non_working_lights = input(f"Enter non-working light index (from 0 to {new_list_of_lights[-1]}): ")
    if non_working_lights == '':
        break
    if int(non_working_lights) > new_list_of_lights[-1]:
        print("The number too big. Please try again.")
        continue
    light_list.append(int(non_working_lights))
list_of_non_working_lights = light_list

def left_side ():
    left_dist_dict = {}
    left_illum_dict = {}
    for item in list_of_non_working_lights:
        left_item = item - 1
        x = 0
        while left_item in list_of_non_working_lights:
            left_item -= 1
            if left_item < 0:
                break
            x += displacement
        if left_item not in list_of_non_working_lights and left_item >= 0:
            x += displacement
        else:
            x = 0
        left_dist_dict[item] = x
        left_illum_dict[item] = 3 ** (-(x/90) ** 2)
        print(f'For light No. {item} the nearest light to the left is at the distance of {x} m')
        print(f'The illumination for the non working light {item} from the left is: {3 ** (-(x/90) ** 2)}')
    return left_dist_dict, left_illum_dict

def right_side ():
    right_dist_dict = {}
    right_illum_dict = {}
    for item in list_of_non_working_lights:
        right_item = item + 1
        x = 0
        while right_item in list_of_non_working_lights:
            right_item += 1
            if right_item > new_list_of_lights[-1]:
                break
            x += displacement
        if right_item not in list_of_non_working_lights and right_item <= new_list_of_lights[-1]:
            x += displacement
        else:
            x = 0
        right_dist_dict[item] = x
        right_illum_dict[item] = 3 ** (-(x / 90) ** 2)
        print(f'For light No. {item} the nearest light to the right is at the distance of {x} m')
        print(f'The illumination for the non working light {item} from the right side is: {3 ** (-(x / 90) ** 2)}')
    return right_dist_dict, right_illum_dict

a = left_side()
b = right_side()

print(a)
print(b)
print(len(new_list_of_lights))
print(new_list_of_lights[-1])
# print(new_list_of_lights)

