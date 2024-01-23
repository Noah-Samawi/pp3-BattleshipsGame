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
- To be able to return to the game with my username.
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
## Technical Design

### Flowchart\
<details><summary>Login</summary>
<img src="">
</details>
<details><summary>Game</summary>
<img src="">
</details>

### Data Modelling
- The data stored in the Google Spreadsheet is a combination of a username and password entered by the user on the login page.

- A new user will enter their choice of username and password which will be stored in the spreadsheet 'user_data_sheet' in the worksheet 'username'. Their password will be stored in the same spreadsheet but in the 'password' worksheet.

- A returning user will type in their username, the function will check the 'username' worksheet for a matching value and return a welcome message if true. The user will be prompted for a password and the function will, once again, check the 'password' worksheet for a matching value. If the function returns both inputs then the user will be allowed to play the game.

- If the returning user inputs do not match, the user will be taken to the start of the login function where they can try again or enter a new set of credentials.


## Technologies Used

### Languages
- Python 3

### Frameworks & Tools
- LucidChart
- Heroku
- Google Drive: Used as a cloud hosting platform for the spreadsheet.
- Google Spreadsheet: Used because Python does not have a built in library to store data in an external spreadsheet.
- pycodestyle: Used as a validation tool instead of pep8 online.
- gitHub
- Gitpod
- Git

## Features

### Welcome Message
- Shows a welcome message.
User Stories covered
<img src="">

### Username/Password Input
- Prompts a user to input a username and password.
- Returning users can have their credentials recoved from a spreadsheet.
User Stories covered
<img src="">

### Battleships Screen 
- Shows an ASCII art warship and logo.
User Stories covered
<img src="">

### Game Board
- Shows the generated game boards for the user and the computer.
User Stories covered
<img src="">

### Game Inputs
- Allows the user to input their guesses and feedsback the result.
- Shows the computer's guess.
User Stories covered: 3, 4, 5
<img src="">

### Game Over
- Shows the end-of-game state to the user once a victory condition has been met.
- Allows user to retry the game or to quit the program.
User Stories covered
<img src="">


## Validation

### PEP8 validation
At the time of creation, the PEP8 online Python validation website was inoperative. To validate the code, a PEP8 validator that is built into the GitPod Workspace was used.

- Run the command 'pip3 install pycodestyle'. (Note that this extension may already be installed, in which case this command will do nothing.)
- In the workspace, press Ctrl+Shift+P (or Cmd+Shift+P on Mac).
- Type the word 'linter' into the search bar that appears. 
- Click on 'Python: Select Linter' from the filtered results.
- Select 'pycodestyle' from the list.
- PEP8 errors will now be underlined in red, as well as being listed in the PROBLEMS tab beside the terminal.

There were no errors or warnings flagged in login.py.
There were no errors or warnings flagged in test_login.py
15 yellow warnings were flagged in run.py. These are down to the symbol combinations used in the ASCII art and logo. These are printed direct to the console and not used in any functions.

- To have an immersive experience.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Welcome Screen. | Input username. | Console prints message welcoming the user as Admiral. | Working as implemented. |
| Main Screen. | Console prints ASCII warship and game logo. | Working as implemented. |
| Game Board. | Generates upon game start. | Generates a board similar to the board game. | Working as implemented. |
| Game Inputs. | User inputs co-ordinates to fire on. | Feedback uses military terminology. | Working as implemented. |

<details><summary>Welcome Screen</summary>
<img src="">
</details>
<details><summary>Main Screen</summary>
<img src="">
</details>
<details><summary>Game Board</summary>
<img src="">
</details>
<details><summary>Game Inputs</summary>
<img src="">
</details>

- To have real-time feedback when playing the game.\

| **Feature** | **Action** | **Expected Result** | **Actual Result** |\
|-------------|------------|---------------------|-------------------|\
| Welcome Screen. | Input username and password. | Console feedsback messages to user. | Working as implemented. |\
| Game Board. | Generates at the start of the game and refreshes after every turn. | Game board is printed and updated with user and computer inputs after each turn. | Working as implemented. |
| Game Inputs. | User inputs their choice of co-ordinates. Computer does the same. | Results are printed back to the user after each turn. | Working as implemented. |

<details><summary>Welcome Screen</summary>
<img src="">
</details>
<details><summary>Game Board</summary>
<img src="">
</details>
<details><summary>Game Inputs</summary>
<img src="">
</details>


5. To be able to play the game against a computer opponent.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Game Board. |  Generates at the start of the game and refreshes after every turn. | Game board is printed and updated with user and computer inputs after each turn. | Working as implemented. |
| Game Inputs. | Computer generates a shot after the user has taken a turn. | Results are updated on the board and printed back to the user after each computer turn. | Working as implemented. |

<details><summary>Game Board</summary>
<img src="">
</details>
<details><summary>Game Inputs</summary>
<img src="">
</details>


- To be told when the game has been won or lost.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Game Inputs. | After a game over condition is met. | Game over condition is printed back to the user. | Working as implemented. |
| Game Over. | After a game over condition is met. | Results are updated on the board and printed back to the user after each computer turn. | Working as implemented. |

<details><summary>Game Inputs</summary>
<img src="">
</details>
<details><summary>Game Over</summary>
<img src="">
</details>

7. To be able to easily replay the game if wanted.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |

|-------------|------------|---------------------|-------------------|
| Game Over. | After a game over condition is met. User inputs Y or N | Input of Y re-runs the game. Input of N exits the program. | Working as implemented. |

<details><summary>Game Over</summary>
<img src="">
</details>

## Bugs

| **Bug** | **Fix** |
| ----------- | ----------- |
| New and Old User functions activated twice. | Moved the function calls to the Login function if/elif statements. |
| Missile counter decreased by two each round. | Seperated missile variable into two; one for the user and computer. |
| Check Login function would not validate user input. | Changed syntax of the Login function if/elif statements. |

## Deployment
Use the following steps to deploy the poject to Heroku:
- Use the "pip freeze -> requiremnts.txt" command in the gitPod terminal; to save any libraries that need to be installed to the project files in Heroku.
- Login or create a Heroku account.
- Click the "New" button in the upper right corner and select "Create New App".
- Choose an app name and your region and click "Create App". Note: the app name must be unique.
- Go to the "Settings" tab, add the python build pack and then the node.js build pack. This is to ensure the project functions correctly with the Code Institute pre-installed template.
- Create a "Config VAR" with the 'CREDS' key and the enter the value of the creds.json file.
- Create a second "Config VAR" with the key of 'PORT' and value of '8000'
- Go to the "Deploy" tab and pick GitHub as a deployment method.
- Search for a repository to connect to.\
- Click enable automatic deploys and then deploy branch.
- Wait for the app to build and then click on the "View" link.

You can fork the repository by following these steps:
- Go to the GitHub repository.\
- Click on the Fork button in the upper right-hand corner.

You can clone the repository by following these steps:
- Go to the GitHub repository.
- Locate the Code button above the list of files and click it.
- Select if you prefer to clone using HTTPS, SSH, or Github CLI and click the copy button to copy the URL to your clipboard.
- Open Git Bash.
- Change the current working directory to the one where you want the cloned directory.
- Type git clone and paste the URL from the clipboard ($ git clone https://github.com/Noah-Samawi/pp3-BattleshipsGame.git.
- Press Enter to create your local clone.

## Credits

### Media
- ASCII art: https://asciiart.website/index.php?art=transportation nautical

### Code
- Code Institute Python lessons.
- Code Institute Love Sandwiches project.
- Knowledge Mavens https://www.youtube.com/watch?v=xz9GrOwQ_5E
- Corey Schafer https://www.youtube.com/watch?v=1Lfv5tUGsn8&t=334s

## Acknowledgments
I would like to take the opportunity to thank:
- My mentor Antonio Rodriguez for his feedback, advice, guidance and support.
- Jim, Sawyer, and the other fantasic members of Code Institute's community team.}






