# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret_list = []
        
        def recursion(root):
            if(root is None):
                return
            ret_list.append(root.val)
            print('here - root val ' + str(root.val))

            # base case
            if(root.left is None and root.right is None):
                print('left = None, right = None, val = ' + str(root.val))
                return

            if (root.left is not None):
                recursion(root.left)

            if (root.right is not None):
                recursion(root.right)

        recursion(root)

        return ret_list


if __name__ == "__main__":
    solution = Solution()
    # [1,null,2,3]
    threeNode = TreeNode(val=3, left=None, right=None)
    twoNode = TreeNode(val=2, left=threeNode, right=None)
    root = TreeNode(val=1, left=None, right=twoNode)

    print(f'Input = [1,null,2,3], Output = {solution.preorderTraversal(root)}')

    # []
    root = TreeNode(val=None, left=None, right=None)

    print(f'Input = [], Output = {solution.preorderTraversal(root)}')