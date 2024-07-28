from typing import List

class Solution:
    def longestSubarray(self,n, arr: List[int]) -> int:
        # n = len(arr)
        max_len = -1
        prefix_sum = 0
        prefix_map = {0: -1}  # Initialize with sum 0 at index -1 to handle edge cases

        for i in range(n):
            prefix_sum += arr[i]
            # Check if we have seen this (prefix_sum - current index) before
            target_sum = prefix_sum - (i + 1)
            if target_sum in prefix_map:
                max_len = max(max_len, i - prefix_map[target_sum])
            if target_sum not in prefix_map:
                prefix_map[target_sum] = i

        return max_len