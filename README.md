# Tic-Tac-Toe and Friends game implementation

This is a small project that took about 5-6 hours to develop 

NOTE on use of AI: I did some boilerplating from Claude.ai, however no AI was used in the generation of any of the code in tictactoe other than some of the unittests using Claude.ai.


This is an exercise that demonstrates a very simple CG goal searching algorithm.
Board has logic for a 3x3 straight line of 3 positions goal (i.e., tic-tac-toe)
VariableBoard has logic for an NxM straight line of Z positions goal (i.e., 5 straight variants)
SnakeBoard allows for a victory for any connected path of length Z for a goal in any 2d rectangle board configuration.

Other easy to create configurations:
- Multi-player: This should actually work without any modifications as well as a "battle-mode" async version, because why not lol.
- TunnelBoard - Which would "win" if there are paths from one edge to the same or different edge (the primary changes would be the `winner()` scan would just run the edges of the board and the goal would be touching an edge instead of a length.
- ContinuousBoard - Which would allow gaps in paths of a given error tolerance with the twist that opposing players could cut off paths through gaps.  The goal could be securing a percentage control of the board (a la Go style) or N paths to edges of length Z.  The search algorithm would change here to fan out for links and be blocked by opponents that are closer than the next link.

## The Logic
The idea was really to model a search space with given heuristic goals masked as a tic-tac-toe exercise :)

Some variations I considered trying (that also informed my design):
- Transforming players into agents that decide their next moves based on the board configuration (or randomly)
- Creating teams of players and agents
- Allowing barriers, voids, and variable square occupation costs (some squares might cost three turns to fill, for example) in the board configuration
- Creating a "Visitor" that holds the actual goal logic (rather than the board), and would have a way to convey values such as, distances to goals for all players, etc. that could help agents make decisions on moves.

## The Project
`dev` - The setup and developer support for the project
`api` - The game server implementation
`tictacbattle` - Probably what the React frontend directory will be called
`deploy` - The terraform support for deploying on AWS
`tictactoe` - The python "brains" library

## Next steps
### Interaction
- I want to build a React frontend and then build out to a very large grid format ContinuousBoard in my free time
- Get the Docker, Terraform, GitHub Actions, and Backend moving parts dialed in a little better, they are very proposed, untested at this point.
- Build out the game logic for:
  - Normal tic-tac-toe, synchronous, 2-player
  - Multi-player, sync
  - Battle tic-tac-toe, async, N-player

### Hosting
- Put the initial site up under my DNS https://autumnpat.com/tictacbattle with let's encrypt certificates using

### Deployment for QA
- Change the TF to allow a blue-green deployment strategy

## HOWTO
For development, I created a directory `dev` with a [readme](dev/prereqs/README.md) to get started (if you're on mac, sorry if you're not).
