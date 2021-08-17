# Cellular automata exploration

## Automaton 1 - Purple Chaos (with sound)
Multi-state automaton with extended Moore neighbourhood. Rules were constructed on the fly, so nothing fancy comes up.
<p align="center"><img src="img/automaton1-anim.gif" width="500px"/></p>

## Automaton 2 - Game of Life
Classical Conway's rules, i.e.
* If cell is dead and has exactly three neighbors then it will be alive in the next generation.
* If cell is alive and has less than two or more than three neighbors then it will die.
* Otherwise cell doesn't change its state.

More information can be found on [Wikipedia](https://en.wikipedia.org/wiki/Conway's_Game_of_Life).
<p align="center"><img src="img/automaton2-anim.gif" width="500px"/></p>

## Automaton 3 - Langton's Ant
Another famous chaotic system. Langton's ant performes random walk on a two-dimensional lattice that is initially empty. Each cell changes its state after the ant's visit (form 0 to 1 and vice versa). Read more on [Wikipedia](https://en.wikipedia.org/wiki/Langton's_ant).
<p align="center"><img src="img/automaton3-anim.gif" width="500px"/></p>

## Automaton 4 - Forest-fire Model
Three-state system with two parameters (probability of spontaneous ignition and probability of filling empty cell with a tree). More information can be found on [Wikipedia](https://en.wikipedia.org/wiki/Forest-fire_model).
<p align="center"><img src="img/automaton4-anim.gif" width="500px"/></p>
