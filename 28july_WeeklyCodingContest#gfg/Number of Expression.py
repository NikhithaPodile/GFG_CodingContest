from typing import List


class Solution:
    def countWays(self, n : int, arr : List[int], x : int, y : int, target : int) -> int:
        def prepare(arr):
            if not arr:
                return {'-':{}, '+':{(0,0):{0:1}}}
                
            cur = 0
            used = [0, 0]
            def traverse(ind, sign):
                nonlocal cur
                if sign == '+':
                    used[0] += 1
                    cur += arr[ind]
                else:
                    used[1] += 1
                    cur -= arr[ind]
                if ind == len(arr)-1:
                    if tuple(used) not in D:
                        D[tuple(used)] = {}
                    D[tuple(used)][cur] = D[tuple(used)].get(cur, 0) + 1
                else:
                    traverse(ind + 1, '-')
                    traverse(ind + 1, '+')
                
                if sign == '+':
                    used[0] -= 1
                    cur -= arr[ind]
                else:
                    used[1] -= 1
                    cur += arr[ind]
            
            ret = {}
            D = {}
            traverse(0, '-')
            ret['-'] = D
            D = {}
            traverse(0, '+')
            ret['+'] = D
            return ret
            
        def get(side, sign, used):
            side = side[sign]
            if used in side:
                return side[used]
            return {}
            
        left = prepare(arr[:n//2])
        right = prepare(arr[n//2:])
        ans = 0
        
        for a in range(x+1):
            for b in range(y+1):
                c, d = x-a, y-b
                for s1, s2 in [('+', '-'), ('+', '+'), ('-', '+'), ('-', '-')]:
                    L = get(left, s1, (a, b))
                    R = get(right, s2, (c, d))
                    for val, freq in L.items():
                        if target-val in R:
                            ans += freq*R[target-val]
                    
        return ans