# Ekdatha Arramreddy

def isValidParantheses(s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for char in s:
            if char in "([{":
                stack.append(char)
            elif len(stack) == 0:
                return False
            elif char == "}":
                if stack.pop() != "{":
                    return False
            elif char == ")":
                if stack.pop() != "(":
                    return False
            elif char  == "]":
                if stack.pop() != "[":
                    return False
            else:
                return False
        return len(stack) == 0