def display(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for row_index in range(rows):
        a_row_string = ""
        for col_index in range(cols):
            a_row_string = f'{a_row_string}{matrix[row_index][col_index]:^5}'
        print(a_row_string)
    
def transpose(matrix):
    matrix_t = []
    rows = len(matrix)
    cols = len(matrix[0])
    for col_index in range(cols):
        column = []
        for row_index in range(rows):
            item = matrix[row_index][col_index]
            column.append(item)
        matrix_t.append(column)
    return matrix_t

def main():
    matrix = [['A','B'], ['C','D'], ['D','F']]
    display(matrix)
    matrix_t = transpose(matrix)
    display(matrix_t)
if __name__ == '__main__':
    main()