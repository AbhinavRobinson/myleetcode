'''
Runtime: 44 ms, faster than 78.91% of Python3 online submissions for Regular Expression Matching.
Memory Usage: 14.4 MB, less than 34.99% of Python3 online submissions for Regular Expression Matching.
'''

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
#       if no special charachters
        if ("." not in p) and ("*" not in p):
            if s == p:
                return True
            return False

#       add to cache  
        cache = {}
        
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i,j)]
#           both strings are traversed
            if i >= len(s) and j >= len(p):
                return True
#           only pattern is traversed but string is left ... not possiable to match
            if j >= len(p): return False
#           match condition  
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
#           if * present                                
            if (j+1) < len(p) and p[j+1] == "*": 
#                              dont use *     use *
                cache[(i,j)] = dfs(i, j+2) or (match and dfs(i+1, j)) 
                return cache[(i,j)] 
#           move forward after match  
            if match: 
                cache[(i,j)] = dfs(i+1, j+1)
                return cache[(i,j)] 
            cache[(i,j)] = False
#           no match  
            return False
        
        return dfs(0,0)