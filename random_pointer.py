# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

# For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

# Return the head of the copied linked list.

# The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
# Your code will only be given the head of the original linked list.

# Example 1

# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

# Example 2

# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]

# Example 3

# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]


class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val  # Value of the node
        self.next = next  # Point of the next node in the list
        self.random = random  # Pointer to a random node in the list


def copyRandomList(head):
    if not head:
        return None

    hashmap = {}

    # First pass: Create copy of each node and store in hashmap
    curr = head
    while curr:
        # Creating a copy of the current node storing it
        hashmap[curr] = Node(curr.val)
        curr = curr.next

    # Second pass: Assigning next and random pointers for each copy node
    curr = head
    while curr:
        # copied from the hashmap
        copy_node = hashmap[curr]
        # Assigning pointer of copied code
        copy_node.next = hashmap.get(curr.next)
        copy_node.random = hashmap.get(curr.random)
        curr = curr.next

        return hashmap[head]

    head = Node(1)
    head.next = Node(2)
    head.random = head.next
    head.next.random = head.next

    copied_head = copyRandomList(head)

    curr = copied_head
    while curr:
        print(
            "[{},{}]".format(curr.val, "null" if not curr.random else curr.random.val)
        )
        curr = curr.next
