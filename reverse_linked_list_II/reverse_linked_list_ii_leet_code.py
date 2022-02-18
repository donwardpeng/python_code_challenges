import timeit
from copy import deepcopy


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        if not head:
            return None

        left, right = head, head
        stop = False
        def recurseAndReverse(right, m, n):
            nonlocal left, stop

            # base case. Don't proceed any further
            if n == 1:
                return

            # Keep moving the right pointer one step forward until (n == 1)
            right = right.next

            # Keep moving left pointer to the right until we reach the proper node
            # from where the reversal is to start.
            if m > 1:
                left = left.next

            # Recurse with m and n reduced.
            recurseAndReverse(right, m - 1, n - 1)

            # In case both the pointers cross each other or become equal, we
            # stop i.e. don't swap data any further. We are done reversing at this
            # point.
            if left == right or right.next == left:
                stop = True

            # Until the boolean stop is false, swap data between the two pointers     
            if not stop:
                left.val, right.val = right.val, left.val

                # Move left one step to the right.
                # The right pointer moves one step back via backtracking.
                left = left.next           

        recurseAndReverse(right, m, n)
        return head
    
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
    