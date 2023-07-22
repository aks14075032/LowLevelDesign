class GameManager:

    def __init__(self, board):
        self.board = board
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def start_game(self):
        no_winner = True
        player_turns = self.players

        while no_winner:
            self.board.print_board()
            if not self.board.is_free_space():
                no_winner = False
                break

            current_player = player_turns.pop(0)
            print(f'{current_player.get_name()} please play you turn, Enter row, column')

            # Can add check on below input and add functionality to re-enter
            x = int(input("Please Enter your row number: "))
            y = int(input("Please Enter your column number: "))

            check = self.board.add_piece_to_board(x, y, current_player.get_playing_piece())
            if not check:
                print("No valid move enter again")
                player_turns.insert(0, current_player)
                continue
            if self.is_there_winner(self.board, x, y):
                print(f'Congratulation {current_player.name} you are the winner !!')
                no_winner = False
                return 'Success'
            player_turns.append(current_player)

        print("This match is tied")
        return 'Tie'

    @staticmethod
    def is_there_winner(board, current_row, current_column):
        board = board.get_board()
        first_ele = board[current_row][current_column]
        is_winner = True
        for i in board[current_row]:
            if first_ele != i:
                is_winner = False

        if is_winner:
            return True
        is_winner = True

        first_ele = board[0][current_column]
        for j in range(len(board)):
            if first_ele != board[j][current_column]:
                is_winner = False
        if is_winner:
            return True
        is_winner = True

        for i in range(len(board)):
            if board[i][i] != first_ele:
                is_winner = False
        if is_winner:
            return True
        is_winner = True

        for i in range(len(board)):
            if board[i][len(board) - 1 - i] != first_ele:
                is_winner = False
        if is_winner:
            return True

        return False
