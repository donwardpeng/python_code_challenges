"""
Given the head of a singly linked list and two integers left and right where left <= right, 
reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]

Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
 

Follow up: Could you do it in one pass?
"""
import timeit
from copy import deepcopy

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        # print('** Starting **')
        if not head.next or (left == right):
            return head
        list_of_vals = []
        while True:
            list_of_vals.append(head.val)
            if not head.next:
                break
            head = head.next
        if len(list_of_vals) == 2:
            list_of_vals = list_of_vals[::-1]
        else:
            new_list_of_vals = list_of_vals[:left-1:]
            # print(f'start of new list of vals = {new_list_of_vals}')
            # if (right - left) > 1:
            middle_list_of_vals = list_of_vals[right-1:left-2:-1]
            if (left == 1):
                middle_list_of_vals = list_of_vals[right-1::-1]
            # print(f'middle of new list of vals = {middle_list_of_vals}')
            end_list_of_vals = list_of_vals[right::]
            # print(f'end of new list of vals = {end_list_of_vals}')
            list_of_vals = new_list_of_vals + middle_list_of_vals + end_list_of_vals
            # print(f'list_of_vals = {list_of_vals}')
        new_list_of_nodes = [ListNode(val=list_of_vals[-1], next=None)]
        for i, item in enumerate(list_of_vals[-2::-1]):
            new_list_of_nodes.insert(0, ListNode(val=item, next=new_list_of_nodes[0]))
        return new_list_of_nodes[0]


    def traverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        print('Traversing List')
        while True:
            print(head.val)
            if not head.next:
                break
            head = head.next


if __name__ == "__main__": 
    solution = Solution()
    print('Input: head = [1,2,3,4,5], left = 2, right = 4')
    fifth = ListNode(5, None)
    fourth = ListNode(4, fifth)
    third = ListNode(3, fourth)
    second = ListNode(2, third)
    head = ListNode(1, second)
    starttime = timeit.default_timer()
    new_head = solution.reverseBetween(head, 2, 4)
    solution.traverseList(new_head)

    second = ListNode(5, None)
    head = ListNode(3, second)
    new_head = solution.reverseBetween(head, 1, 1)
    solution.traverseList(new_head)
    new_head = solution.reverseBetween(head, 1, 2)
    solution.traverseList(new_head)
    new_head = solution.reverseBetween(head, 2, 2)
    solution.traverseList(new_head)

    third = ListNode(3, None)
    second = ListNode(2, third)
    head = ListNode(1, second)
    new_head = solution.reverseBetween(head, 1, 2)
    solution.traverseList(new_head)

    third = ListNode(3, None)
    second = ListNode(2, third)
    head = ListNode(1, second)
    new_head = solution.reverseBetween(head, 2, 3)
    solution.traverseList(new_head)
