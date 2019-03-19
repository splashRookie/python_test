file = open("dictionary.txt","r")

# alist = [{'name': 'Jack', 'age': '18'}]
# s = str(alist)
#
# file.write(s)
# file.close()

blist = []

openFile = file.read()
# content = dict(openFile)
# blist.append(openFile)
# print(blist)
# print(openFile)
content1 = eval(openFile)
print(type(content1))
print(content1)
blist.append(content1)
print(blist)