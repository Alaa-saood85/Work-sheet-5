def function(text):
    result = text.split(' ')
    return result[0][0] + '.' + result[1][0]
test1 = 'Batoul Shamaly' #B.S
test2 = 'Fatema Yousef' #F.Y
print (function(test1))
print (function(test2))