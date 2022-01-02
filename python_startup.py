import atexit
import os
import rlcompleter
import readline

# tab ompletion
if os.uname()[0] == "Darwin":
    readline.parse_and_bind("bind ^I rl_complete")
else:
    readline.parse_and_bind("tab: complete")

# History file
histfile = os.path.join(os.environ['HOME'], '.python_history')
try:
    readline.read_history_file(histfile)
except IOError:
    pass

atexit.register(readline.write_history_file, histfile)
del os, histfile, readline, rlcompleter
