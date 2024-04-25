class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasPathSum(root, targetSum):
    """
    :type root: TreeNode
    :type targetSum: int
    :rtype: bool
    """

    if not root:
        return False

    if not root.left and not root.right:
        return targetSum == root.val

    left_sum = hasPathSum(root.left, targetSum - root.val)
    right_sum = hasPathSum(root.right, targetSum - root.val)

    return left_sum or right_sum


hasPathSum()
