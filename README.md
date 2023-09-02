# labyrinth
## 2017 project to create 2 types of labyrinth (Prims and hunt and kill) and model how a human would walk in.  Which type and size of labyrinth can a human exit in 8h?

The goal was to create 2 types of labryinths and find the caracterisitics of a labyrinth a human is unlikely to get our in 8h of walking.
This can be applicable to amusement park, mall, and other public space path creation.

The 2 labyrinths are:
- Prims: Considers all frontier to the labyrinth as option for the next path during creation. Leads to lots of deadends, mostly small paths and little change of direction before the exit.
- Hunt and Kill:
    - Hunt: Considers only the frontier to the last added path as an option for the next path during creation until no options are left.
    - Kill: Then, the algo goes through the labyrinth row by row, and stops at the first row with a non-explored cell. It takes the first cell connected to the labyrinth as the start of the next path, and then starts the Hunt algorithm again.
  Leads to not many deadends, a lot of longer paths, and a higher number of direction changes to get the exit.

Modeling human would walk a labyrinth (if no strategy deployed):
- generally prefers to keep going straight,
- bias towards going right more than left (cf relevant studies),
- rarely goes back if not at a deadend
- average of 2sec / cell

Results: over a sample of 100 labryinth of size ranging from 5x5 to 35x35, Prim's labryinth has an overall higher probability of exit than Hunt and Kill.

Limitations: 
- We put entry and exit diagonally opposed, which has an impact on results, leading generally to shorter path than other options.
- We selected a perfect labyrinth (no islands), which is not a realistic modeling of life
- The path the "human" takes has no memories, so it tends to repeat the same path multiple time because of skwed probalities on directions before getting out. Future iterations would add a memory aspect.







