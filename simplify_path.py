class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        
        for p in path.split('/'):
            if p in {'', '.'}:
                continue
                
            if stk and p == '..':
                stk.pop()
                
            if p != '..':
                stk.append(p)
                
        return '/' + '/'.join(stk)
