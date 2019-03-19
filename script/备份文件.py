import os
# def backup(fileName):
#     f = open(fileName,"w+")
#     shotname, extension = os.path.splitext(fileName)  # 提取文件名与后缀
#     backupFile = open("%s副本.%s" % (shotname,extension), "w")
#     backupFile.write(f.read())
#     f.close()
#     backupFile.close()
#
# backup("123.text.txt")



# oldName = input("请输入需要备份的文件名：")
# f1 = open(oldName,'r')
# index1 = oldName.rfind('.')
# f2 = open(oldName[0:index1]+'副本'+oldName[index1:],'w')
# str1 = f1.read()
# f2.write(str1)
# f1.close()
# f2.close()
