class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        temp = path.split("/")
        for i in temp:
            if(i==".."):
                if(stack):
                    stack.pop()
            elif(i == "." or i ==""):
                continue
            else:
                stack.append(i)
        return "/" + "/".join(stack)
