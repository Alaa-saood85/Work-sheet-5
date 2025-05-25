def function (strings_list:list):
    text = ' '.join(string for string in strings_list)
    l = text.split(' ')
    result = []
    done_items = []
    for x in l:
        if x in done_items:
            pass
        else:
            result.append((x, l.count(x)))
            done_items.append(x)
    return result
strings = ["hello world", "python is awesome", "hello python"]
print (function(strings))