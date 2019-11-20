main_tab=[
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

def print_tab(tab):
    '''Печатает таблицу'''
    print('┌──────┬──────┬──────┐')
    x_line = 1
    for row in tab:
        y_line = 0
        for value in row:
            if (y_line%3) == 0: print('│', end='')
            print(value, end=' ')
            y_line += 1
        print('│')
        if ((x_line%3) == 0) and (x_line < len(tab)) : 
            print('├──────┼──────┼──────┤')
        x_line += 1
    print('└──────┴──────┴──────┘')

def get_col(tab, i):
    '''Возвращает столбец под номером i'''
    return [row[i] for row in tab]

def get_row(tab, i):
    '''Возвращает строку под номером i'''
    return tab[i]

def get_indexes_first(tab, value):
    '''Возвращает индексы(строка, столбец) первого вхождения n,
       если нет такого, то возвращает None'''
    for i in range(0,len(tab)):
        try:
            return (i, get_row(tab,i).index(value))
        except ValueError:
            continue
    return None

def get_undertab(tab, i):
    '''Возвращает подтаблицу 3х3'''
    row = i[0]//3*3
    col = i[1]//3*3
    ret = []
    for k in range(3):
        ret += tab[row + k][col:col + 3]
    return ret

def check_value(tab, i, value):
    '''Проверяет есть ли в строке, в столбце и подтаблице
        элемент со значение value
    '''
    if (value in get_row(tab, i[0]) or 
        value in get_col(tab, i[1]) or
        value in get_undertab(tab, i)
        ):
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

def solve(main_tab, start_tab, value):
    if (i_row_col := get_indexes_first(main_tab,0)) == None:
        return
    while (value < 10):
        if (not check_value(main_tab, i_row_col, value)):
            main_tab[i_row_col[0]][i_row_col[1]] = value
            value = 1
            break
        else:
            value += 1
    if (value >= 10):
        i_row_col = next_back_index(start_tab, i_row_col)
        value = main_tab[i_row_col[0]][i_row_col[1]]
        main_tab[i_row_col[0]][i_row_col[1]] = 0
        value += 1
    solve(main_tab, start_tab, value)


def main():
    solve(main_tab, start_tab, 1)
    print_tab(main_tab)
    return 0

if __name__ == "__main__":
    main()