# TMux cheatsheet by Ehsan Shirzadi

### Terminal commands:

| Command          | Description                         |
| ---------------- |:-----------------------------------:|
| tmux new -s name | A news session with the name 'name' |
| tmux rename-window -t number newname | Rename a pane |

### In TMux press ctrl+b+ one of these characters:

| ctrl+b+...       | Description                         |
| ---------------- |:-----------------------------------|
| %                 | Vertical split |
| "                 | Horizontal split |
| ⬆                | Move to top window |
| ⬇                | Move to bottom window  |
| ⬅                | Move to left window  |
| ➡                | Move to right window  |
| z                 | Zoom in/Zoom out  |
| c                 | Create a new tab   |
| $                 | Rename current session  |
| ,                 | Rename current tab  |
| 0..9                 | Switch between tabs  |
| w                 | Switch between tabs (choose)  |
|                  |   |


### Enable fish inside Tmux:
```
set-option -g default-shell /usr/bin/fish
```
to make fish permanently active add followings to `~/.tmux.conf`:
```
set -g default-command /usr/bin/fish/
set -g default-shell /usr/bin/fish/
```


###### Email: Ehsan.Shirzadi@Gmail.com
###### Web: www.ehsanshirzadi.com
