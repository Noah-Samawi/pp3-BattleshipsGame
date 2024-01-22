# Battleships

Welcome to the Battleships is a game of logic, with players attempting to sink each others fleet by guessing co-ordinates.
This version uses a a board generated using Python lists and incorporates a logic engine to allow the computer to fire back at the user.

(Developer: Stuart Wall)
![Start screen]()

[The live link can be found here](https://pp3-battleships-cae1b33910a6.herokuapp.com/)
## Table of Content

- [Project Goals](#project-goals)
    . [User Goals](#user-goals)
    . [Site Owner Goals](#site-owner-goals)
- [User Experience](#user-experience)
    . [Target Audience](#target-audience)
    . [User Requirements and Expectations](#user-requirements-and-expectations)
    . [User Stories](#user-stories)
_ [Battlefleet Game Instructions](#Battlefleet-Game-Instructions)    
- [Technical Design](#technical-design)
    . [Flowchart](#flowchart)
- [Technologies Used](#technologies-used)
    . [Languages](#languages)
    . [Frameworks & Tools](#frameworks-&-tools)
- [Features](#features)
- [Testing](#validation)
    . [PEP8 validation](#pep8-validation)
    . [Testing user stories](#testing-user-stories)
- [Bugs](#Bugs)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgments](#acknowledgments)

## Project Goals 
The project goal is to create a logic game using Python.
### User Goals
The application user wants to play a logic game.

### Site Owner Goals
The Battleships game is played on grids on which each player's fleet of battleships are marked. The locations of the fleets are concealed from the other player. Players call shots at the other player's ships, and the objective of the game is to destroy the opposing player's fleet.
The application provides a working battleships game for a single user to play against the computer.

## User Experience

### Target Audience
- Younger users who like playing games.
- Users who are looking for a game to pass time on during a break.
- Older users who are looking for a logic challenge.

### User Requirements and Expectations

### User Stories
- To create a personal username.
- To be able to return to the game with my username and password.
- To have an immersive experience.
- To have real-time feedback when playing the game.
- To be able to play the game against a computer opponent.
- To be told when the game has been won or lost.
- To be able to easily replay the game if wanted.

## Battlefleet Game Instructions

Welcome to Battlefleet, Admiral! Your mission is to lead your fleet against the enemy and sink all their warships before they sink yours. The game is played on a 9x9 grid, with each square identified by a letter (A-I) and a number (1-9). Your fleet consists of 8 warships strategically placed on the grid. The enemy fleet is also positioned randomly.

### Main Screen
When you start the game, you'll be greeted with the main screen, featuring an ASCII art dashboard and instructions to start the game. Take a moment to review the fleet and prepare for battle.

### Game Board
The game board consists of two main components:

User Board: Displays your fleet's positions.
Target Board: Tracks your shots and enemy hits.

### Game_Play

User Turn: You have a limited number of missiles (32) to target enemy warships. Enter the coordinates where you want to launch a missile. For example, input "A" and "5" to target the square in the first row and fifth column.

Hit or Miss: The game will inform you whether your shot hit an enemy warship or missed. If you hit, the enemy warship is sunk. Keep an eye on your remaining missiles.

Enemy Turn: After your turn, the enemy will retaliate. The computer will randomly target one of your squares. The game will notify you if the enemy hit one of your warships.

Victory or Defeat: The game continues until either you sink all enemy warships (Victory) or the enemy sinks all of your warships (Defeat). If you run out of missiles, the enemy fleet escapes.

Game Over
When the game concludes, a "Game Over" message will appear. You'll be prompted to play again or exit. Enter 'Y' to restart and 'N' to exit the game.

Have Fun Admiral!
Now that you know the rules, it's time to lead your fleet to victory! Good luck, Admiral, and may the seas be in your favor!







