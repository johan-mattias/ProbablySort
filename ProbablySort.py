import numpy as np

def custom_sort(arr):
    if len(arr) < 1:
        return arr
    
    # Initialize statistics

    start_index = 0 #this is const(ant)
    end_of_sorted_list = start_index + 1
    start_of_semi_sorted_list = end_of_sorted_list + 1
    end_of_sorted_list = start_of_semi_sorted_list + 1
    start_of_unsorted_list = end_of_sorted_list + 1
    end_of_sorted_list = len(arr) #or infinity #this is [also] const(ant)

    #these are for the stats measure
    #min seen so far can't just use the min function
    min_val = arr[start_index] #very good copilot it should be the start of the list
    max_val = arr[end_of_sorted_list] #no copilot you can do better next time
    #avg of min and max
    avg_val = min_val + max_val / 2 #no copilot you did better this time
    
    sorted_list = [arr[start_index]] #so far the list is sorted
    unsorted_list = arr.copy() #that is very good python if you don't why this is important you should stop, and i would turn back if i were you
    
    # Iterate until unsorted_list is empty #that makes sense
    for x in unsorted_list:
        # Update statistics dynamically
        #if sorted_list: #this i don't get
        min_val = x if x < min_val else min_val #min(min_val, x) #yes that's right chatgpt good job # but inline
        max_val = x if x > max_val else max_val
        avg_val = 
        std_dev = np.std(sorted_list) #this is a good idea #johan: 'is it though' no it's not
        
        # Decide where to place x
        if x < avg_val:
            # Calculate relative position if not dividing by zero
            if min_val != avg_val:
                relative_position = (x - min_val) / (avg_val - min_val)
                position = int(relative_position * len(sorted_list))
            else:
                position = 0
        else:
            # Calculate relative position if not dividing by zero
            if avg_val != max_val:
                relative_position = (x - avg_val) / (max_val - avg_val)
                position = int(relative_position * (len(sorted_list) - 1)) + 1
            else:
                position = len(sorted_list)
        
        # Insert x into the roughly correct position
        sorted_list.insert(position, x)
    
    return sorted_list

# Example usage
arr = [5, 3, 8, 6, 2, 9, 1, 7, 4]
sorted_arr = custom_sort(arr)
print("Sorted array:", sorted_arr)
