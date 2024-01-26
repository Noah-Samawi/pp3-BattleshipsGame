# Battleships

Welcome to the Battleships is a game of logic, with players attempting to sink each others fleet by guessing co-ordinates.
This version uses a a board generated using Python lists and incorporates a logic engine to allow the computer to fire back at the user.


![Start screen](Doks/start-screem.png)

[The live link can be found here](https://pp3-battleships-cae1b33910a6.herokuapp.com/)
## Table of Content

- [Project Goals](#project-goals)
    . [User Goals](#user-goals)
    . [Site Owner Goals](#site-owner-goals)
- [User Experience](#user-experience)
    . [Target Audience](#target-audience)
    . [User Requirements and Expectations](#user-requirements-and-expectations)
   .[User Stories](#user-stories)
- [Battlefleet Game Instructions](#Battlefleet-Game-Instructions)    
- [Libraries and Technologies Used](#libraries-and-technologies-used)
    . [Flowchart](#flowchart)
- [Technologies Used](#technologies-used)
    . [Languages](#languages)
    . [Frameworks & Tools](#frameworks-&-tools)
- [Features](#features)
- [Testing](#validation)
    . [PEP8 validation](#pep8-validation)
    . [Testing user stories](#testing-user-stories)
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

### User Stories
- To have an immersive experience.
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

### Flowchart
![Flowchart](Doks/logic-diagram.png)

## Libraries and Technologies Used

### Languages
- Python 3

### Python Libraries:

- [random](https://docs.python.org/3/library/random.html?highlight=random#module)
-random-`random.choice` is used to select arandom word for the game from a text file.
- [os](https://docs.python.org/3/library/os.html?highlight=os#module-os) 
  - `os.system` is used in order to clear the terminal when beginning a new game.

- [gspread](https://pypi.org/project/gspread/): to allow communication with Google Sheets. 
- [requests](https://pypi.org/project/requests): enables data retrieval from APIs.
- [google.oauth2.service_account](https://google-auth.readthedocs.io/en/stable/index.html):  used to validate credentials and grant access to google service accounts.
- [pandas](https://pypi.org/project/pandas/) - used for sorting and displaying leaderboard data in user-friendly format.  
- [pyfiglet](https://pypi.org/project/pyfiglet/0.7/) - for taking ASCII text and rendering it into ASCII art fonts.
- [colorama](https://pypi.org/project/colorama/) - for adding colour to terminal text.

### Programs Used

- [GitHub](https://github.com/) - used for version control.
- [Heroku](https://dashboard.heroku.com/apps) -  used to deploy the live project.
- [Lucidchart](https://lucid.app/documents#/dashboard) -  used to create the game flowchart
- [Code institute Herokuapp](https://pep8ci.herokuapp.com/) used to validate pop Issues
- [Grammerly](https://app.grammarly.com/) - used to proof read the README.md

## Features

### Welcome Message
- Shows a welcome message.
User Stories covered
<img src="Doks/welcom-message.png">

### Battleships Screen 
- Shows an ASCII art warship and logo.
User Stories covered
<img src="Doks/battleships-screen.png">

### Game Board
- Shows the generated game boards for the user and the computer.
User Stories covered
<img src="Doks/game_boards.png">

### Game Inputs
- Allows the user to input their guesses and feedsback the result.
- Shows the computer's guess.
User Stories covered: 3, 4, 5
<img src="Doks/game_inputs.png">

### Game Over
- Shows the end-of-game state to the user once a victory condition has been met.
- Allows user to retry the game or to quit the program.
User Stories covered
<img src="Doks/game_over.png">


## Testing

### PEP8 Testing
At the time of creation, the PEP8 online Python validation website was inoperative. To validate the code, a PEP8 validator that is built into the GitPod Workspace was used.

- Run the command 'pip3 install pycodestyle'. (Note that this extension may already be installed, in which case this command will do nothing.)
- In the workspace, press Ctrl+Shift+P (or Cmd+Shift+P on Mac).
- Type the word 'linter' into the search bar that appears. 
- Click on 'Python: Select Linter' from the filtered results.
- Select 'pycodestyle' from the list.
- PEP8 errors will now be underlined in red, as well as being listed in the PROBLEMS tab beside the terminal.

### Code institute Herokuapp
The python files have all been passed through [Code institute Herokuapp](https://pep8ci.herokuapp.com/#). All python files were checked with no errors reported. See screen show below:

![Code Testing](Doks/code-testing.png)

1. To have real-time feedback when playing the game.\

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Game Board. | Generates at the start of the game and refreshes after every turn. | Game board is printed and updated with user and computer inputs after each turn. | Working as implemented. |
| Game Inputs. | User inputs their choice of co-ordinates. Computer does the same. | Results are printed back to the user after each turn. | Working as implemented. |

</details>
<details><summary>Game Board</summary>
<img src="Doks/user_test_1_board.png">
</details>
<details><summary>Game Inputs</summary>
<img src="Doks/user_test_1_board.png">
</details>


2. To be able to play the game against a computer opponent.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Game Board. |  Generates at the start of the game and refreshes after every turn. | Game board is printed and updated with user and computer inputs after each turn. | Working as implemented. |
| Game Inputs. | Computer generates a shot after the user has taken a turn. | Results are updated on the board and printed back to the user after each computer turn. | Working as implemented. |

<details><summary>Game Board</summary>
<img src="Doks/user_test_2_board.png">
</details>
<details><summary>Game Inputs</summary>
<img src="Doks/user_test_2_input.png">
</details>


3. To be told when the game has been won or lost.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Game Inputs. | After a game over condition is met. | Game over condition is printed back to the user. | Working as implemented. |
| Game Over. | After a game over condition is met. | Results are updated on the board and printed back to the user after each computer turn. | Working as implemented. |

<details><summary>Game Inputs</summary>
<img src="Doks/user_test_3_inputs.png">
</details>
<details><summary>Game Over</summary>
<img src="Doks/user_test_3_game_over.png">
</details>

4. To be able to easily replay the game if wanted.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |

|-------------|------------|---------------------|-------------------|
| Game Over. | After a game over condition is met. User inputs Y or N | Input of Y re-runs the game. Input of N exits the program. | Working as implemented. |

<details><summary>Game Over</summary>
<img src="Doks/user_test_4_replay.png">
</details>



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

## Acknowledgments
I would like to take the opportunity to thank:
- My mentor Antonio Rodriguez for his feedback, advice, guidance and support.
- Jim, Sawyer, and the other fantasic members of Code Institute's community team.}
