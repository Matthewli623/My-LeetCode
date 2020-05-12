class Solution:
    def isValid(self, s: str) -> bool:
        if not s :
            return True
        if  len(s)%2 ==1:
            return False
        stack = []
        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
            else:
                if not stack:
                    return False
                right=i
                left = stack.pop()
                if left =="(" and right ==")":
                    continue
                elif left =="{" and right=="}":
                    continue
                elif left == "[" and right =="]":
                    continue
                else:
                    return False
                
        if stack:
            return False
        return True
             