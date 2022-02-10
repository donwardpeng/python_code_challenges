'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
'''
import timeit
import copy


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: 
            return None
        new_list_last_node = ListNode(val=head.val, next=None)
        list_of_nodes = [new_list_last_node]
        while True:
            head = head.next
            new_node = ListNode(val=head.val, next=list_of_nodes[-1])
            list_of_nodes.append(new_node)
            if not head.next:
                break
        return list_of_nodes[-1]

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
    print('Input: head = [1,2,3,4,5]')
    fifth = ListNode(5, None)
    fourth = ListNode(4, fifth)
    third = ListNode(3, fourth)
    second = ListNode(2, third)
    head = ListNode(1, second)
    starttime = timeit.default_timer()
    new_head = solution.reverseList(head)
    print(f'new head val = {new_head.val}')
    next_node = new_head.next
    print(f'next_node.val = {next_node.val}')
    next_node = next_node.next
    print(f'next_node.val = {next_node.val}')

    solution.traverseList(new_head)

    # print(f'Result = {solution.reverseList(head)}')
    print("The time difference is :", timeit.default_timer() - starttime)