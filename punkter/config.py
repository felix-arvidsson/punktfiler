#gå igenom alla values
#kolla först om folder, annars behandla som en fil.
#om folder, ta bort '/' så link check funkar

scripts_folder = "/home/flip/.local/bin/scripts"

#skapar symlink i ~/config
config_dir = [
    "i3/",
    "kitty/",
    "nvim/",
    "ranger/",
]

#skapar symlink på grejer i ./scripts folder
scripts = [
    "mp3"
]

aliases = [
    "ls='lsd'",
    "ll='lsd -lav'",
    "htop='btop'",
    "top='btop'",
]

#skapar symlink i ~/
custom = {
    "tmux/tmux.conf": "~/.tmux.conf"
}
