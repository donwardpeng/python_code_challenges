'''
Given the head of a singly linked list, return true if it is a palindrome.
Example 1:
Input: head = [1,2,2,1
Output: true
Example 2:


Input: head = [1,2]
Output: false

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 

Follow up: Could you do it in O(n) time and O(1) space?
'''
import timeit
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        list_as_string = str(head.val)
        while True:
            if not head.next:
                break
            head = head.next
            list_as_string += str(head.val)
        return list_as_string == list_as_string[::-1]
        
if __name__ == "__main__": 
    solution = Solution()
    print('Input: head = [1,2,2,1]')
    fourth = ListNode(1, None)
    third = ListNode(2, fourth)
    second = ListNode(2, third)
    head = ListNode(1, second)
    starttime = timeit.default_timer()
    print(f'Result = {solution.isPalindrome(head)}')
    print("The time difference is :", timeit.default_timer() - starttime)
        

        