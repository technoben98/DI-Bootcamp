matrix_string = "7iiTsxh%?i #sM $a #t%^r!"
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz! '
matrix = []
new_matrix = []
description = ""
matrix_string = matrix_string.replace("$", " ")
def bulding_matrix(matrix_string):
    num_rows = 8
    num_columns = 3
    count = 0
    for i in range(num_rows):
        row = []
        for j in range(num_columns):
            element = matrix_string[count]
            row.append(element)
            count +=1
        matrix.append(row)
    for j in range(num_columns):
        for i in range(num_rows):
            element = matrix[i][j]
            if matrix[i][j] in alphabet:
                new_matrix.append(element)
    description ="".join(new_matrix)
    description = description.replace("  ", "")
    return description
print(bulding_matrix(matrix_string))