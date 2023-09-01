# Initial information:
road_length = 2000000
displacement = 20
y = 0
light_index = 0
list_of_lights = [0]
# Finding list of all lights:
while y < road_length:
    y += displacement
    light_index += 1
    list_of_lights.append(light_index)
new_list_of_lights = list_of_lights
# Getting list of NON-working lights:
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

def left_side():
    """
    Function for calculation of the illumination of non-working lights from the left side (or beginning) of the street
    :return: dict of illumination from the left side (or beginning) of the street.
    """
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
        left_illum_dict[item] = 3 ** (-(x/90) ** 2)
    return left_illum_dict

def right_side():
    """
    Function for calculation of the illumination of non-working lights from the right side (or the end) of the street
    :return: dict of illumination from the right side (or the end) of the street.
    """
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
        right_illum_dict[item] = 3 ** (-(x / 90) ** 2)
    return right_illum_dict

def merge_dictionaries(dict1, dict2):
    """
    Function for evaluation of two dicts - left side and right side (or beginning and the end)
    :param dict1: left side (or beginning) dict
    :param dict2: right side (or the end) dict
    :return: full calculated illumination for non-working lights dict
    """
    merged_dictionary = {}
    for key in dict1:
        if key in dict2:
            new_value = (dict1[key] + dict2[key])/2
        else:
            new_value = dict1[key]/2
        merged_dictionary[key] = round(new_value, 3)
    for key in dict2:
        if key not in merged_dictionary:
            merged_dictionary[key] = round(dict2[key]/2, 3)
    return merged_dictionary
# Calling functions of left and right side illumination
a = left_side()
b = right_side()
print('-'*100)
# Calling function of merged dictionaries
result = merge_dictionaries(a, b)
print("This is the dict of non-working lights with their illumination from the working lights:")
print(result)
print('-'*100)
# Finding minimal intensity of illumination
min_illumination = min(result.values())
print(f'The minimal illumination intensity: {min_illumination}')
print('-'*100)
# Finding non-working lights with minimal intensity of illumination
min_result = [key for key in result if result[key] == min_illumination]
print("The lights with minimal illumination are: " + str(min_result))
print('-'*100)
# Finding non-working light with the lowest index
print(f'The light with the lowest index {min_result[0]} must be changed!')
print('-'*100)
print('-'*100)
# Finding the number of non-working lights to be changed to reach illumination intensity equal to 1
print(f'The minimal number of light bulbs, which is needed to be replaced \nto make cumulative illumination intensity'
      f'at every street light non less than 1 is: {len(list_of_non_working_lights)}')
