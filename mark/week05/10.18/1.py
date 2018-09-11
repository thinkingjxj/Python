__author__ = 'thinking'


s1 = 'abcdef'
s2 = 'defabcdef'

def findit(str1, str2):
    matrix = []
    xindex = 0
    xmax = 0
    for i,x in enumerate(str2):
        matrix.append([])
        for j,y in enumerate(str1):
            if x != y:
                matrix[i].append(0)
            else:
                if x == 0 or y == 0:
                    matrix[i].append(1)
                else:
                    matrix[i].append(matrix[i-1][j-1] + 1)
                if matrix[i][j] > xmax:
                    xmax = matrix[i][j]
                    xindex = j
                    xindex += 1
    return str1[xindex - xmax : xindex]

print(findit(s1,s2))
