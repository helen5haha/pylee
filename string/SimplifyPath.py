'''
Given an absolute path for a file (Unix-style), simplify it.
For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
Corner Cases:
Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as"/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
'''

def simplifyPath(path):
    stack = []
    toks = path.split("/")
    stack.append(toks[0])
    toks = toks[1:]
    for tok in toks:
        if tok in ("","."):
            continue
        elif ".." == tok:
            # root / should not be poped to distinguish abs path and rel path
            if len(stack) > 0 and "" != stack[len(stack) - 1]:
                stack.pop()
            #else:
            #    return ""  #/home/../../..
        else:
            stack.append(tok)
    len_stack = len(stack)
    if len_stack > 1:
        return "/".join(stack) if "" == stack[0] else "/" + "/".join(stack)
    elif (1 == len_stack and "" == stack[0]) or 0 == len_stack:
        return "/"


simplifyPath("/../")
simplifyPath("/home/")
simplifyPath("/a/./b/../../c/")
simplifyPath("/home//foo/")
simplifyPath("/usr/local")