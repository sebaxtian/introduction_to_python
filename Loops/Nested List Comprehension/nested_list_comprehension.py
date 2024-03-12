string = '0123456789'

matrix = ['TODO']

for row in matrix:
    print(row)

matrix = [[c for c in string] for _ in range(len(string))]
print(matrix)
