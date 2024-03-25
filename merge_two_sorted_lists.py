# Question

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

#_______________________________________________________________________________________________________________________

# Example 1
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # If linked 1 doesn't exist return linked list 2.
        if not l1: return l2
        # If linked 2 doesn't exist retrun linked list 1.
        if not l2: return l1

        # Ensure to return the head later and assing a ListNode inorder to create new linked list.
        current = dummy = ListNode(0)

        # Want to check if linked 1 value is less than l2 or L2 value is less than l1 value 
        while l1 and l2:
            # if l1 value is less than l2 value add to the current next node.
            if l1.val < l2.val:
                current.next = l1
                #Then increment li pointer to the next.
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            # make sure third pointer is incremented
            current = current.next

        # Once finished, need to make sure to add the rest of l1 and l2 dependeing on which one remains.
        if l1: current.next = l1
        if l2: current.next = l2

        # Return head by using dummy pointer. Needs to point to next because its pointing to a point
        # that doesn't exist on this linked list that is created since its an empty node. The one after
        # that is the head.
        return dummy.next