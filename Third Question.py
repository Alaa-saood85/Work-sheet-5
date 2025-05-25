def function(string: str):
    return [(x, i) for i, x in enumerate (string)]
print (function("hello world"))