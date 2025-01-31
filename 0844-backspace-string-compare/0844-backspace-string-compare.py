class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build_string(st: str) -> list:
            stack = []
            for c in st:
                if c == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(c)
            return stack

        return build_string(s) == build_string(t)
                