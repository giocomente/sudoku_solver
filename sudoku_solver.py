tab=[
    [2,0,0,5,0,0,8,0,3],
    [0,0,6,0,4,9,0,0,0],
    [5,1,0,0,0,2,0,4,9],
    [4,6,0,0,0,0,9,1,5],
    [0,0,0,1,0,3,0,0,0],
    [9,2,1,0,0,0,0,8,7],
    [8,3,0,4,0,0,0,6,2],
    [0,0,0,3,7,0,5,0,0],
    [6,0,7,0,0,8,0,0,4]
    ]
start_tab = [
    [2,0,0,5,0,0,8,0,3],
    [0,0,6,0,4,9,0,0,0],
    [5,1,0,0,0,2,0,4,9],
    [4,6,0,0,0,0,9,1,5],
    [0,0,0,1,0,3,0,0,0],
    [9,2,1,0,0,0,0,8,7],
    [8,3,0,4,0,0,0,6,2],
    [0,0,0,3,7,0,5,0,0],
    [6,0,7,0,0,8,0,0,4]
    ]
def print_tab(a):
    '''Печатает таблицу'''
    print('┌──────┬──────┬──────┐')
    x_line = 1
    for row in a:
        y_line = 0
        for n in row:
            if (y_line%3) == 0: print('│', end='')
            print(n, end=' ')
            y_line += 1
        print('│')
        if ((x_line%3) == 0) and (x_line < len(a)) : 
            print('├──────┼──────┼──────┤')
        x_line += 1
    print('└──────┴──────┴──────┘')

def get_col(a, i):
    '''Возвращает столбец под номером i'''
    return [row[i] for row in a]

def get_row(a, i):
    '''Возвращает строку под номером i'''
    return a[i]

def get_indexes_first(a, n):
    '''Возвращает индексы(строка, столбец) первого вхождения n,
       если нет такого, то возвращает None'''
    for i in range(0,len(a)):
        try:
            return (i, get_row(a,i).index(n))
        except ValueError:
            continue
    return None

def get_undertab(a, i, j):
    row = i//3*3
    col = j//3*3
    ret = []
    for k in range(3):
        ret += a[row + k][col:col + 3]
    return ret

def check_value(a, i, n):
    if (n in get_row(a, i[0]) or 
        n in get_col(a, i[1]) or
        n in get_undertab(a, i[0], i[1])):
        return True
    return False

def next_back_index(start_tab, i):
    while True:
        i_row, i_col  = i
        if (i_row <= 0 and i_col <= 0):
            i = None
            break
        i_col -= 1
        if i_col < 0:
            i_col = 8
            i_row -= 1
        i = i_row, i_col
        if start_tab[i[0]][i[1]] == 0:
            break
    return i

def solve(a, start_tab, value):
    if (i_row_col := get_indexes_first(a,0)) == None:
        return
    while (value < 10):
        if (not check_value(a, i_row_col, value)):
            a[i_row_col[0]][i_row_col[1]] = value
            value = 1
            break
        else:
            value += 1
    if (value >= 10):
        i_row_col = next_back_index(start_tab, i_row_col)
        value = a[i_row_col[0]][i_row_col[1]]
        a[i_row_col[0]][i_row_col[1]] = 0
        value += 1
    solve(a, start_tab, value)


def main():
    #start_tab = tab.copy()
    solve(tab, start_tab, 1)
    print_tab(tab)
    return 0

if __name__ == "__main__":
    main()