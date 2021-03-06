# How to Make the Dungeon

Use pseudo code to explain a dungeon engine. 

# Dungeon State Model
There are two or three models I can think of using which I'll
speculate about below and list in order of perceived difficulty.
The Appendixie project under Evennia 0.6 was closest to the second
option - purely permanent. 

## Pure instanced D. (like Dungeon Robber)
Nothing is saved. Each room or passage is randomly created and disapears
as soon as a character moves through it. Getting back to the entrance or
getting lost is purely abstracted. There is no need to build rooms at all
as I belive EvMenu could handle all navigation. Only treasure and loot 
objects would be added to the database.

## Pure Permanant Building
Every room the player creates remains.  When they choose to 'backtrack' they
must use their own memory to find their way back. If they leave and return
to the dungeon the rooms and passages are just as they left them. (Though 
optionally contents and features might re-spawn).  If other players attend
they will find the same dungeon. 

One think I learned from the Appendixie it's relatively easy to build random
dungeons in tree pattern where branches never merge with each other. However 
to have logical dungeons that could exist in cartesian geometry... would be
more difficult. I have thought that if you don't care about logic, you could
build arbitrary links between branches at random intervals.

## Temporary Built Dungeons
Dungeon's persist for the length of a Dungeon run or delve. Returning to 
town wipes out the instancce. It's less clear to me how to do this. Maybe 
each room added to the DB would be tagged based on the player and or dungeon
run that created it. At the end of the run, all rooms and exits with those 
tags are deleted, but the player could keep their loot. This could lead to other
interesting results if players are allowed to team up.

# Generation algorithm for pure instanced Dungeons
Dungeons have two coordinates only distance and depth.
Distance refers to number of rooms away from the entrance or last known
stairway up. Depth is number of stairs up to get to surface (town).

## Dungeon Routine (applies to most Pure instanced)
I suspect this entire thing can be implemented with Evmenu.
1. ENTRANCE - Starts at dungeon 
    * safe place; player choosed to "explore" or "leave"
1. "leave" exit to surface or town
1. "explore" cmd 
    * distance increases by 1 and player moves to a new random location type
        - "room"
        - "passage"
        - "junction" 
1. "room" place
    * May contain
        - "nothing"
        - "monster"
        - "treasure"
        - "trap"
        - "stairs"
    * generate contents, resolve contents with a fight or saving throw
    * once resolved room reverts to "nothing"
    * generate exits; player can choose to "explore" or "backtrack"
1. "passage" place
    * May contain
        - nothing
        - monster
        - trap
1. "backtrack" cmd
    Attempt to return to Dungeon Entrance. Diffilculty affected by "distance"
    * May result in:
        - success = return to entrance
        - failure = getting lost, option to 'back track' is removed and 
            replaced with "wander"
1. "wander" cmd 
    Attempt to get unlost.
    * May result in:
        - success = able to attempt to backtrack
        - failure = remain lost automatically "explore"
1. "junction" place
    Player is offered 1-3 choices instead of "explore" in addition to 
    "backtrack". 
    * choices May contain features:
        - nothing
        - clue
        - door
        - stairs
1. "nothing" feature
    a room with nothing has 0-3 exits which the player may choose in addition
    to "backtrack". An exit is either a passage->"explore" or a "door" feature
1. "monster" encounter
    * A monster will attack unless player neutralizes it or escapes. Typical
    choices (some are dependent on skills or equipment):
        - sneak past
        - run away
        - parlay
        - attack
1. "trap" feature
    traps have random chance of causing an effect, or damaging the player
    * if survived or avoided, player may:
    	- "explore" or 
    	- "backtrack"
1. "stairs" feature
    * Stairs appear to go "up" or "down" one level. 
    	- Up reduces "depth" and sets "distance" to max of the higher level.
    	- Down increases "depth" sets "distance" to zero;
    	- distance "zero" always contains stairs up.
1. "clue" feature
    A clue is a bit of enticing or ominous text attached to a choice of passage
    choosing the passage with a "clue" results in a random "effect".
1. "door" feature/exit
    A door is a feature and a choice. A player can always choose to ignore the
    door and either continue/explore (unless dead end) or backtrack/wander 
    * Otherwise the player may try to:
        - "force door" it open
        - "unlock door" with key or thief tools
        - "listen door" 

