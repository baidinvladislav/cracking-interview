def simplifyPath(path: str) -> str:
    stack = []

    # Split the path by '/'
    components = path.split('/')

    for component in components:
        if component == '' or component == '.':
            # Skip empty components and current directory references
            continue
        elif component == '..':
            # Move up one directory level if possible
            if stack:
                stack.pop()
        else:
            # Valid directory name, push onto stack
            stack.append(component)

    # Join the stack to form the simplified path
    simplified_path = '/' + '/'.join(stack)

    return simplified_path


# Examples
print(simplifyPath("/home/"))  # Output: "/home"
print(simplifyPath("/home//foo/"))  # Output: "/home/foo"
print(simplifyPath("/home/user/Documents/../Pictures"))  # Output: "/home/user/Pictures"
print(simplifyPath("/../"))  # Output: "/"
print(simplifyPath("/.../a/../b/c/../d/./"))  # Output: "/.../b/d"
