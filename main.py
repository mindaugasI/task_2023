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
            x = road_length
        left_dist_dict[item] = x
        left_illum_dict[item] = 3 ** (-(x/90) ** 2)
        # print(f'For light No. {item} the nearest light to the left is at the distance of {x} m')
        # print(f'The illumination for the non working light {item} from the left is: {3 ** (-(x/90) ** 2)}')
    return left_illum_dict

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
            x = road_length
        right_dist_dict[item] = x
        right_illum_dict[item] = 3 ** (-(x / 90) ** 2)
        # print(f'For light No. {item} the nearest light to the right is at the distance of {x} m')
        # print(f'The illumination for the non working light {item} from the right side is: {3 ** (-(x / 90) ** 2)}')
    return right_illum_dict

def merge_dictionaries(dict1, dict2):
    merged_dictionary = {}

    for key in dict1:
        if key in dict2:
            new_value = (dict1[key] + dict2[key])/2
        else:
            new_value = dict1[key]/2

        merged_dictionary[key] = new_value

    for key in dict2:
        if key not in merged_dictionary:
            merged_dictionary[key] = dict2[key]/2

    return merged_dictionary

a = left_side()
b = right_side()

# print(f'The illumination from the left side: {a}')
# print(f'The illumination from the right side: {b}')
print('-'*100)
result = merge_dictionaries(a, b)
print(result)
print('-'*100)

min_illumination = min(result.values())
print(f'The minimal illumination index: {min_illumination}')
print('-'*100)
min_result = [key for key in result if result[key] == min_illumination]
print("The lights with minimal illumination are: " + str(min_result))
print('-'*100)
print(f'The light with the lowest index {min_result[0]} must be changed!')
print('-'*100)
print('-'*100)
print(f'The minimal number of light bulbs, which is needed to be replaced \nto make cumulative illumination intencity'
      f'at every street light non less than 1 is: {len(list_of_non_working_lights)}')