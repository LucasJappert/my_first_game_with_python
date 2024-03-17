from src.models.game import Game
import src.logs.profile_logs as profile_logs

profile_logs.start_profiler()

my_game = Game()

if __name__ == "__main__":
    my_game.start()
    
profile_logs.stop_profiler()

