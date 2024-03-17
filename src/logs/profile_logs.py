"""
    Run "snakeviz -H localhost -p 7777 src/logs/my_profile.prof" to see the generated profile in a web browser
"""   

import cProfile

profiler = cProfile.Profile()

def start_profiler():
    profiler.enable()

def stop_profiler():
    profiler.disable()
    profiler.dump_stats('src/logs/my_profile.prof')
