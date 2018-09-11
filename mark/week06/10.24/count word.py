f = open('C:/\\Users\\10649\\Desktop\\1.txt', 'rb')
s = f.read()
f.close()
#print(s)

a = s.decode()

dic = {}
for i, v in enumerate(a):
    for x in v:
        if x.isalpha():
            dic[v] = 1
    #if v not in dic:
    #if x not in dic:
        #dic[v] = 1
    #dic[v] += 1
print(dic)
