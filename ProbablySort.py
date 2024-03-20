import numpy as np

def custom_sort(arr):
    if len(arr) < 1:
        return arr
    
    # Initialize statistics

    start_of_sorted_list = 0 #this is const(ant)
    end_of_sorted_list = start_of_sorted_list
    start_of_semi_sorted_list = end_of_sorted_list + 1
    end_of_semi_sorted_list = start_of_semi_sorted_list
    start_of_unsorted_list = end_of_semi_sorted_list + 1
    end_of_sorted_list = len(arr) #or infinity #this is [also] const(ant)
    index = start_of_unsorted_list + 1 

    #these are for the stats measure
    #min seen so far can't just use the min function
    min_val = min(arr[start_of_sorted_list], arr[start_of_semi_sorted_list]) #no copilot you can do better next time, no that was actually exactly what i wanted
    max_val = max(arr[start_of_sorted_list], arr[start_of_semi_sorted_list]) # you did better this time


    sorted_list = [] #so far the list is sorted yeah when it's empty
    semi_sorted_list = [] 

    #so right now i need to compare the two lists, or two indexes and then add the smaller one to the sorted list, no problem
    sorted_list.append(min_val)
    semi_sorted_list.append(max_val)
    #copy but skip the first two elements
    unsorted_list = arr.copy() #that is very good python if you don't why this is important you should stop, and i would turn back if i were you
    
    #TODO remove first two elements from unsorted list
    unsorted_list = unsorted_list[2:] #this is a good idea #johan: 'is it though

    min_val_sorted = min_val #not sure if these are right start values
    max_val_sorted = min_val #not sure if these are right start values
    #avg of the semi sorted list is just the max_cal
    avg_val = max_val
    count_of_numbers_in_avg = 1 #len(unsorted_list) #(this is a good idea #johan: 'is it though' no it's not) - this was all a suggestion, it was actually good

    #maybe i should start unrolled and then roll it up

    #then update the statistics variables
    #min is new max, but what does min mean here min in the semi sorted list, or the sorted list do we need both ill comment it out for now
    #min_val = max_val

    #now what, we need a new max value, this is okay the sample is small here we'll get to the meat of it in a while
    x = unsorted_list[index] # later on this can be x+1 (index)   #take the next element at the 2 position from the unsorted list, 'that's right'
    #we used index so increment is
    index+=1

    #always pull to the left first, just a quick cheat might never happen really, but it's unknown
    if x < sorted_list[0]: #or the min value in sorted i think
        #then we put x at the front of the list
        sorted_list.insert(0, x)
        #this is exploiting the fact that when we find a new min we know where it goes
        #so the more new values we find the better
        #but then we have to divude and conquer sort the list again maybe when it gets bigger
    #maybe elif bigger than the max value in the sorted list
    
    #else: maybe we didn't need an else
    #then we put x at the end of the list
    #sorted_list.append(x) #no bad copilot this was wrong
    #then we add it to the semi sorted list
    semi_sorted_list.append(x)
    #here i think we might be able to do this in parellet maybe somehow
    # becuase in the meantime in another thread we could be sorting the semi sorted list
    # so it's like a producer conumber problem,

    #okay so now sort the semi sorted list and take a new x at the same time

    #now we need a new x yeah? go debug and find out

    #so the question is how far do you semi sort the list before actually sorting
    # so let's just zip through the list and see what happens


    #we will need to recalculate the average now
    #and maybe update the count
    #update the max value in the semi_sorted list, do we need a max value in the sorted list?
    
    #so far we have seen 3 numbers so the index should point to 4
    _=1 # check where index is, yes it is

    #check to see if the semi sorted list is sorted if it is then append all of it to sorted
    # that's a big checkpoint, we can probably visualize to see if this ever happens in practice which might be never, but this is just a theory exercise
    is_list_sorted = True
    for i in range(len(semi_sorted_list)-1):
        if semi_sorted_list[i] > semi_sorted_list[i+1]:
            is_list_sorted = False
            break
    if is_list_sorted:
        sorted_list.extend(semi_sorted_list)
        semi_sorted_list = []
    else:
        # that's fine don't need an else 
        pass

    #TODO: START HERE okay now we take the next x and figure it out from there

    # the problem is we don't know if the semi sorted list the value we just added is lower than the sorte dlist so we check that first

    # Iterate until unsorted_list is empty #that makes sense
    for x in unsorted_list:
        # Update statistics dynamically
        #if sorted_list: #this i don't get
        min_val = x if x < min_val else min_val #min(min_val, x) #yes that's right chatgpt good job # but inline
        max_val = x if x > max_val else max_val
        #needs to be updated but first adjust the average
        avg_val = (avg_val * count_of_numbers_in_avg) + x / (count_of_numbers_in_avg + 1) #'very good completion copilot' 
        
        count_of_numbers_in_unsorted_list += 1 #is this right? i think so becuase were in a loop right

        
        # Decide where to place x in the semi sorted list
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

        #std_dev = np.std(sorted_list) #this is a good idea #johan: 'is it though' no it's not


        # Insert x into the roughly correct position
        sorted_list.insert(position, x)
    


    return sorted_list

# Example usage
arr = [5, 3, 8, 6, 2, 9, 1, 7, 4]
sorted_arr = custom_sort(arr)
print("Sorted array:", sorted_arr)
