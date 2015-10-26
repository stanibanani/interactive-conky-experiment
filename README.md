#A simple tic-tac-toe game for Conky

For the purpose of demonstrating an interactive conky.

It uses a simple python3 script to get or update the state of the game.

I recommend i3 for this because it is easy to configure the keymap.
But other window mangers would do.

Add this to your i3 config file:

    set $tictac /path/to/the/tictactoe/folder
    mode "tictactoe"{
        bindsym Mod1+1 exec python $tictac/tictactoe.py place 2 0
        bindsym Mod1+2 exec python $tictac/tictactoe.py place 2 1
        bindsym Mod1+3 exec python $tictac/tictactoe.py place 2 2

        bindsym Ctrl+1 exec python $tictac/tictactoe.py place 1 0
        bindsym Ctrl+2 exec python $tictac/tictactoe.py place 1 1
        bindsym Ctrl+3 exec python $tictac/tictactoe.py place 1 2

        bindsym Shift+1 exec python $tictac/tictactoe.py place 0 0
        bindsym Shift+2 exec python $tictac/tictactoe.py place 0 1
        bindsym Shift+3 exec python $tictac/tictactoe.py place 0 2

        bindsym $mod+r exec python $tictac/tictactoe.py new
                                 
                                 
        # exit with esc
        bindsym Escape exec pkill conky; mode "default"
    }

    bindsym $mod+Ctrl+g exec cd $tictac && conky -c $tictac/conkyrc; mode "tictactoe"

Go to an empty workspace, press $mod+Ctrl+G and play using Alt (bottom row), Ctrl (middle row), Shift (top row) and 1, 2 and 3 for the columns.

Have a nice day!
