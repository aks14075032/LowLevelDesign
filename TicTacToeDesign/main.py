from TicTacToeDesign.models.player import Player
from TicTacToeDesign.services.playerManager import PlayerManager
from TicTacToeDesign.models.board import Board
from TicTacToeDesign.services.gameManager import GameManager

# Can Add Check on board size and number of player to be int and greater than 1
board_size = int(input("Enter Size of playing board (default will be three: "))
number_of_players = int(input("Enter Number of players playing: "))


current_board = Board(board_size)
game_manager = GameManager(current_board)

for i in range(number_of_players):
    player_name = input(f"Player {i+1} Please Enter your name: ")
    player_piece = input(f"Player {i+1} Please Enter playing piece(Any Fav Character on keyboard): ")
    player = Player(player_name, player_piece)
    PlayerManager().add_player(player, player_name)
    game_manager.add_player(player)


status = game_manager.start_game()
print(status)
