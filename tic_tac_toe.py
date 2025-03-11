from nicegui import ui

board = [None] * 9
current_player = 'X'
game_over = False


def check_winner():
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]               # Diagonals
    ]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] is not None:
            return board[combo[0]]
    if all(cell is not None for cell in board):
        return 'Tie'
    return None


def button_click(index):
    global current_player, game_over
    if board[index] is None and not game_over:
        board[index] = current_player
        buttons[index].text = current_player
        winner = check_winner()
        if winner:
            game_over = True
            if winner == 'Tie':
                ui.notify('It\'s a Tie!')
            else:
                ui.notify(f'Player {winner} wins!')
        else:
            current_player = 'O' if current_player == 'X' else 'X'
            turn_label.text = f'Current turn: {current_player}'

    elif game_over:
        ui.notify('Game is over. Please restart.')

    else:
        ui.notify('That cell is already taken.')


def reset_game():
    global board, current_player, game_over
    board = [None] * 9
    current_player = 'X'
    game_over = False
    turn_label.text = f'Current turn: {current_player}'
    for button in buttons:
        button.text = ''


with ui.row():
    turn_label = ui.label(f'Current turn: {current_player}')

with ui.row():
    buttons = []
    for i in range(9):
        button = ui.button(text='', on_click=lambda i=i: button_click(i))
        buttons.append(button)
        button.style(width='50px', height='50px')

with ui.row():
    reset_button = ui.button('Reset Game', on_click=reset_game)

ui.run()
