#using stack
class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for c in s:
            if c != "]":
                stack.append(c)
            else:
                repeatSubstring=""
                multiplier=""
                while stack and stack[-1] !='[':
                    repeatSubstring = stack.pop() + repeatSubstring
                stack.pop() #remove '['
                while stack and stack[-1].isnumeric():
                    multiplier=stack.pop() + multiplier
                stack.append(repeatSubstring*int(multiplier))
        return "".join(stack)
        