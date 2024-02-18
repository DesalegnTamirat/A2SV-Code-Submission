class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.replace("//", "/").strip("/").split("/")
        stack = []
        print(paths)
        for path in paths:
            if path == "..":
                if stack:
                    stack.pop()
            elif path != "." and path:
                stack.append(path)

        return "/" + "/".join(stack)
              