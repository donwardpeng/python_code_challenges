# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        print('----Starting - root = ' + str(root.val))

        ret_list = []

        def recursion(root):
            if(root is None):
                return

            # leaf node
            if(root.left is None and root.right is None):
                print('left = None and right = None, appending value, ' + str(root.val))
                ret_list.append(root.val)
                return

            # go left
            if (root.left is not None):
                print('going left')
                recursion(root.left)

            # root node
            ret_list.append(root.val)
            print('left = None, appending value, ' + str(root.val))

            # go right
            if (root.right is not None):
                print('going right')
                recursion(root.right)

        recursion(root)

        return ret_list


if __name__ == "__main__":
    solution = Solution()
    # [1,null,2,3]
    threeNode = TreeNode(val=3, left=None, right=None)
    twoNode = TreeNode(val=2, left=threeNode, right=None)
    root = TreeNode(val=1, left=None, right=twoNode)

    print(f'Input = [1,null,2,3], Output = {solution.inorderTraversal(root)}')

    # [1,null,2,3]
    threeNode = TreeNode(val=2, left=None, right=None)
    twoNode = TreeNode(val=1, left=None, right=None)
    root = TreeNode(val=3, left=twoNode, right=threeNode)

    print(f'Input = [3,1,2], Output = {solution.inorderTraversal(root)}')

    # []
    root = TreeNode(val=None, left=None, right=None)

    print(f'Input = [], Output = {solution.inorderTraversal(root)}')