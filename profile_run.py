import cProfile
import pstats
from main import cli

if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.runcall(cli)

    stats = pstats.Stats(profiler)
    stats.sort_stats("tottime")
    stats.print_stats(20)  # show top 20 slowest functions
