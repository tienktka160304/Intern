binary_tree_array = ['R', 'A', 'B', 'C', 'D', 'E', 'F', None, None, None, None, None, None, 'G']

def left_child_index(index):
    return 2 * index + 1

def right_child_index(index):
    return 2 * index + 2

def pre_order(index):
    if index >= len(binary_tree_array) or binary_tree_array[index] is None:
        return []
    return [binary_tree_array[index]] + pre_order(left_child_index(index)) + pre_order(right_child_index(index)) # list + list + list

def in_order(index):
    if index >= len(binary_tree_array) or binary_tree_array[index] is None:
        return []
    return in_order(left_child_index(index)) + [binary_tree_array[index]] + in_order(right_child_index(index))

def post_order(index):
    if index >= len(binary_tree_array) or binary_tree_array[index] is None:
        return []
    return post_order(left_child_index(index)) + post_order(right_child_index(index)) + [binary_tree_array[index]]

print('pre-order:', pre_order(0))       #output = pre-order: ['R', 'A', 'C', 'D', 'B', 'E', 'F', 'G']
print('in-order:', in_order(0))         #output = in-order: ['C', 'A', 'D', 'R', 'E', 'B', 'G', 'F']
print('post-order:', post_order(0))     #output = post-order: ['C', 'D', 'A', 'E', 'G', 'F', 'B', 'R']

