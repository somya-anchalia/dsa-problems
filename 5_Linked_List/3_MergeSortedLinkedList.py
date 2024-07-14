                                
# Node class represents a
# node in a linked list
class Node:
    def __init__(self, data1, next1=None):
        # Data stored in the node
        self.data = data1
        # Pointer to the next node in the list
        self.next = next1

# Function to convert a list to a linked list
def convert_arr_to_linked_list(arr):
    # Create a dummy node to serve
    # as the head of the linked list
    dummy_node = Node(-1)
    temp = dummy_node

    # Iterate through the list and
    # create nodes with list elements
    for i in range(len(arr)):
        # Create a new node with the list element
        temp.next = Node(arr[i])
        # Move the temporary pointer
        # to the newly created node
        temp = temp.next

    # Return the linked list starting
    # from the next of the dummy node
    return dummy_node.next

# Function to merge two sorted linked lists
def sort_two_linked_lists(list1, list2):
    arr = []
    temp1 = list1
    temp2 = list2

    # Storing elements of both lists into a list

    # Add elements from list1 to the list
    while temp1 is not None:
        arr.append(temp1.data)
        # Move to the next node in list1
        temp1 = temp1.next

    # Add elements from list2 to the list
    while temp2 is not None:
        arr.append(temp2.data)
        # Move to the next node in list2
        temp2 = temp2.next

    # Sorting the list in ascending order
    arr.sort()

    # Converting the sorted list
    # back to a linked list
    head = convert_arr_to_linked_list(arr)

    # Return the head of the
    # merged sorted linked list
    return head

# Function to print the linked list
def print_linked_list(head):
    temp = head
    while temp is not None:
        # Print the data of the current node
        print(temp.data, end=" ")
        # Move to the next node
        temp = temp.next
    print()

# Example Linked Lists
list1 = Node(1)
list1.next = Node(3)
list1.next.next = Node(5)

list2 = Node(2)
list2.next = Node(4)
list2.next.next = Node(6)

print("First sorted linked list: ", end="")
print_linked_list(list1)

print("Second sorted linked list: ", end="")
print_linked_list(list2)

merged_list = sort_two_linked_lists(list1, list2)

print("Merged sorted linked list: ", end="")
print_linked_list(merged_list)
                                
                            