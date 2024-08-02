# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        cur = dummy

        while list1 and list2:
            if list1.val > list2.val:
                cur.next = list2
                list2 = list2.next
            else:
                cur.next = list1
                list1 = list1.next
            
            cur = cur.next
        
        if list1:
            cur.next = list1
        else:
            cur.next = list2
        
        return dummy.next

    # Function to print the linked list
    def print_linked_list(self, head):
        temp = head
        while temp is not None:
            # Print the data of the current node
            print(temp.val, end=" ")
            # Move to the next node
            temp = temp.next
        print()

# Example Linked Lists
list1 = ListNode(1)
list1.next = ListNode(3)
list1.next.next = ListNode(4)
list1.next.next.next = ListNode(5)

list2 = ListNode(2)
list2.next = ListNode(4)
list2.next.next = ListNode(6)
list2.next.next.next = ListNode(7)

print("Linked list 1: ", end="")
Solution().print_linked_list(list1)

print("Linked list 2: ", end="")
Solution().print_linked_list(list2)

merged_list = Solution().mergeTwoLists(list1, list2)

print("Merged sorted linked list: ", end="")
Solution().print_linked_list(merged_list)

