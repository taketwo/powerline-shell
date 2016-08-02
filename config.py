# This is the configuration file for your powerline-shell prompt
# Every time you make a change to this file, run install.py to apply changes
#
# For instructions on how to use the powerline-shell.py script, see the README

# Add, remove or rearrange these segments to customize what you see on the shell
# prompt. Any segment you add must be present in the segments/ directory

SEGMENTS = [

# Show the current git branch and status
    'git',

# Show the current mercurial branch and status
    'hg',

# Show the machine's hostname. Mostly used when ssh-ing into other machines
    'hostname',

# Show current python virtualenv
    'virtual_env',

# Show the current directory. If the path is too long, the middle part is
# replaced with ellipsis ('...')
    'cwd',

# Show number of running jobs
    'jobs',

# Shows a '#' if the current user is root, '$' otherwise
# Also, changes color if the last command exited with a non-zero error code
    'root',
]

# Change the colors used to draw individual segments in your prompt
THEME = 'mcf'
