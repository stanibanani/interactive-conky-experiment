##ASCII game interactive conky demo

This is a demo of interactive conky.

It is a game in which you move your character on a 2 dimensional grid.
It uses a python3 script to get and update the state of the game.

### Setup
After cloning this repo add this to your i3 config file

    set $game /path/to/cloned/repo/conkygame
    mode "conkygame"{
        bindsym Up exec --no-startup-id $game/main.py session1 up
        bindsym Down exec --no-startup-id $game/main.py session1 down
        bindsym Left exec --no-startup-id $game/main.py session1 left
        bindsym Right exec --no-startup-id $game/main.py session1 right

        bindsym Escape exec --no-startup-id pkill conky; mode "default"
    }
    bindsym $mod+Ctrl+a exec --no-startup-id cd $game && conky -c $game/conkyrc; mode "conkygame"

After this you can go to an empty workspace press $mod+Ctrl+a and play the *game* using arrow keys.

### Explanation
The state of the game is stored in a game session file which you can create using

    python main.py new [session name] [width] [height]

This repo comes with a session file named *session1* which is a 10x10 grid.

To move the player run

    python main.py [session name] up|down|left|right

this will move the player and save the session file.

To display the state of the game run
    
    python main.py [session name] show

this is the output which is then piped into the simple conkyrc.

Have fun!
