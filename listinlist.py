
"""
mat = [
    [1,2,3], #linha 0 
    [4,5,6], #linha 1
    [7,8,9]  #linha 2 
]

print("Elementos da primeira linha:")
for elem in mat[0]:
    print(elem, end=" ")
print()

for linha in mat:
    for elem in linha:
        print(elem, end=" ")
    print()

"""

mat = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

print("Dados da tabela", mat[0][3])