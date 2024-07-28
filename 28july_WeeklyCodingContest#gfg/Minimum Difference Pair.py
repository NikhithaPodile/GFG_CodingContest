from typing import List
from collections import defaultdict


class Node:
    def _init_(self, idx):
        self.left = None
        self.right = None
        self.max_idx = idx


class Trie:
    def _init_(self, x):
        self.root = Node(0)
        self.x = x

    def find(self, idx, val):
        x = self.x
        curr = self.root
        ans = float('inf')
        for i in range(31, -1, -1):
            if (x >> i) & 1:
                if (val >> i) & 1:
                    if curr.right:
                        ans = min(ans, idx - curr.right.max_idx)
                    if curr.left:
                        curr = curr.left
                    else:
                        return ans
                else:
                    if curr.left:
                        ans = min(ans, idx - curr.left.max_idx)
                    if curr.right:
                        curr = curr.right
                    else:
                        return ans
            else:
                if (val >> i) & 1:
                    if curr.right:
                        curr = curr.right
                    else:
                        return ans
                else:
                    if curr.left:
                        curr = curr.left
                    else:
                        return ans
        if curr:
            return min(ans, idx - curr.max_idx)
        return ans

    def insert(self, idx, val):
        curr = self.root
        for i in range(31, -1, -1):
            if (val >> i) & 1:
                if not curr.right:
                    curr.right = Node(idx)
                curr = curr.right
            else:
                if not curr.left:
                    curr.left = Node(idx)
                curr = curr.left
            curr.max_idx = max(idx, curr.max_idx)
        return


class Solution:
    def minDifference(self, n: int, arr: List[int], x: int) -> int:
        t = Trie(x)
        ans = float('inf')
        t.insert(0, arr[0])

        for i in range(1, n):
            res = t.find(i, arr[i])
            ans = min(ans, res)
            t.insert(i, arr[i])
        if ans == float('inf'):
            return -1
        return ans