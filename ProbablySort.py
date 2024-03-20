import numpy as np

def probablySort(arr):
    if len(arr) < 2:
        return arr
    
    # Initial statistics
    min_val = min(arr)
    max_val = max(arr)
    avg_val = np.mean(arr)
    std_dev = np.std(arr)
    
    sorted_list = []
    semi_sorted_list = []
    unsorted_list = arr.copy()
    
    while unsorted_list:
        x = unsorted_list.pop(0)  # Take the first element
        
        # Update statistics
        current_min = min(x, min_val)
        current_max = max(x, max_val)
        current_avg = np.mean(sorted_list + [x] if sorted_list else [x])
        
        # Decide where to place x based on its value relative to min, avg, max
        if x <= current_avg:
            position = int(((x - current_min) / (current_avg - current_min)) * len(semi_sorted_list))
            semi_sorted_list.insert(position, x)
        else:
            position = int(((x - current_avg) / (current_max - current_avg)) * len(semi_sorted_list) + len(semi_sorted_list))
            semi_sorted_list.insert(position, x)
        
        # Update global statistics after placement
        min_val, max_val, avg_val = current_min, current_max, current_avg
    
    # Assuming semi_sorted_list is "roughly sorted", but this may not always be accurate
    sorted_list.extend(semi_sorted_list)
    
    return sorted_list

# Example usage
arr = [5, 3, 8, 6, 2, 9, 1, 7, 4]
sorted_arr = probablySort(arr)
print("Sorted array:", sorted_arr)

#print true if sorted array is sorted
print("Is sorted array sorted?", sorted_arr == sorted(arr))
