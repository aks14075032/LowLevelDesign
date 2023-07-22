from threading import Lock


class PlayingPiece:
    playing_piece_instance = None
    mtx = Lock()

    def __init__(self, p):
        self.playing_piece = p

    @staticmethod
    def get_playing_piece_instance():
        if not PlayingPiece.playing_piece_instance:
            with PlayingPiece.mtx:
                if not PlayingPiece.playing_piece_instance:
                    PlayingPiece.playing_piece_instance = PlayingPiece()
        return PlayingPiece.playing_piece_instance

    def get_playing_piece(self):
        return self.playing_piece
