binary_tree_array = ['R', 'A', 'B', 'C', 'D', 'E', 'F', None, None, None, None, None, None, 'G']

def left_child_index(index):
    return 2 * index + 1

def right_child_index(index):
    return 2 * index + 2

def get_data(index):
    if 0 <= index < len(binary_tree_array):
        return binary_tree_array[index]
    return None

right_child = right_child_index(0)  #right child of R
left_child_of_right_child = left_child_index(right_child)   #left child of R's right child
data = get_data(left_child_of_right_child)  #get data

print(get_data(right_child))