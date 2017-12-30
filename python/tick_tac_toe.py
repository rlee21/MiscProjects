#!/usr/bin/python


def create_board(positions):
    board = dict()
    for position in positions:
        board[position] = ' '

    return board


def update_board(board, position, value):
    return board.update({position: value})


def print_board(board):
    print('_' + board['top-L'] + '_|_' + board['top-M'] + '_|_' + board['top-R'] + '_\n' +
          '_' + board['mid-L'] + '_|_' + board['mid-M'] + '_|_' + board['mid-R'] + '_\n' +
          ' ' + board['low-L'] + ' | ' + board['low-M'] + ' | ' + board['low-R'] + ' \n')



if __name__ == '__main__':
    positions = ['top-L', 'top-M', 'top-R',
                 'mid-L', 'mid-M', 'mid-R',
                 'low-L', 'low-M', 'low-R']
    values = ['X', 'O']
    board = create_board(positions)
    print('valid positions:\n', positions, '\nvalid values:\n', values)
    print_board(board)
    for _ in range(9):
        position = input('Enter position: ')
        if position not in positions:
            print('ERROR: not a valid position, enter one of the valid positions below \n', positions)
        value = input('Enter value: ')
        if value not in values:
            print('ERROR: not a valid value, enter one of the valid values below \n', values)

        update_board(board, position, value)
        print_board(board)
