# The Interactive Startup File

You can ue Python interactively. It is a nice functionality.<br>
To do so you just need to invoke qhe *python* shell from the command line. You will realize that it is handy to have some standard commands executed every time the interpreter is started. You can do this by setting an environment variable named PYTHONSTARTUP to the name of a file containing your start-up commands. This is similar to the .profile feature of the Unix shells.

## Here you have a startup sample file !
Here an example file *python_startup.py* with some usefull commands for the *interactive python shell*.  It has worked fine for me on several python versions as python 2 and 3.

You will put this in your profile file, for example ``` $HOME/.bash_profile ``` file:

```console
# Python Startup (autocompleted enabler)
export PYTHONSTARTUP=$HOME/.python_startup.py
```

And this would by your *python_startup.py* file:

Includes:
- Tab completion during shell
- History file recording shel session

```python
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
```
## Enjoy !
And don't hesitate to send me comments or ideas to improve it. Thanks !
