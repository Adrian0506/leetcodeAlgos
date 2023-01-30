from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return None
        res = []
        quene = deque([(root, 0)])
        hashMap = {}
        while quene:
            curNode, depth = quene.popleft()
            if depth not in hashMap:
                hashMap[depth] = True
                res.append(curNode.val)
            if curNode.right:
                quene.append([curNode.right, depth + 1])
            if curNode.left:
                quene.append([curNode.left, depth + 1])
        return res
