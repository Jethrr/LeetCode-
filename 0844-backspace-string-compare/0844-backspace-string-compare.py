class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def evaluateStr(string):
        
            stack = []


            for char in string:
                if char == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)   


            return ''.join(map(str, stack))
        
        return evaluateStr(s) == evaluateStr(t) 
        
    
            