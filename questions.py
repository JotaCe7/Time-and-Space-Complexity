
# Question 1

def missing_elements(list1, list2):
    # Create a dictionary from list2
    my_dict = dict()
    for element in list2:
      my_dict[element] = 1
    # Create a new list with elements from list1 thar are not keys of my_dict dictionary
    return [ element for element in list1  if element not in my_dict.keys() ]

# Lets assume a length of "n" for list1 and length of "m" for list2
# Creating the dictionary takes time complexity of O(m)
# Then for every element in list1 we check if it is a key of the created dictionary, This takes time complexity of O(n)
# Finally, the overall time complexity for the 2 steps is: O(n+m)


# Question 2
def remove_zeros(list):
    # Initialize a new index
    ouput_index = 0
    # Iterate over the elements of list
    for index in range(len(list)):
        # If value of list at position index is different from zero
        if list[index] != 0:
            # update the value of list at position output_index and increments output_index
            list[ouput_index] = list[index]
            ouput_index += 1
    return list[:ouput_index]

