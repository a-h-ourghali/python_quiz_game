# PythoN Quiz Game
A simple quiz game builtwith python
## Tabele of contents

- [PythoN Quiz Game](#python-quiz-game)
- [Tabele of contents](#tabele-of-contents)
- [Feature](#feature)
- [Projects](#projects)
- [Requirments](#requirments)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [Licence](#licence)
- [Author](#author)



## Feature
- Quiz system
  - Asks the player multiple question
  - Checks the answers automaticlly
  - Calculate the fanal score
- Results storeage
    - Saves quiz results in `resultstxt`
- Admin Mode
  - asks for admin password
  - checks if the password is corect
  - keeps the privte inforamtion outside the main python file
  - Loads the assword form '.env'


```txt

python_quiz_game/
| main.py
| question.py
| requirements.txt
| .env example
| .gitignore 
| READ.md
```
### File Description
- `main.py` - main file used to run quiz game
- `question` - stores questions and answers
- `requirments.txt` - lists the python packages needed for the project
- `.env.example` - shows the envoirment variables needed by project
- `gitignore` - tells git wich files and folders shold notbe tracked
- `README.md`

## Requirments
before runnin the project, make sure you have:
- `python 3`
- `python-dotenv`

## Installation
1. open a terminal in the project folder.
2. check that python is installed:
```bash
pip install -r requirements.txt
```
## Envoirment Setup
1. create a `.env` file from `.env.example`:
```bash
cp .env.example . env
```
2. open the new `.env` file
3. replace the example value with your own password
```text
QUIZ_ADMIN_PASSWORD=your_password_here
```
4. save the file

> Do not commit your `.env` file because it may contaain private information
> 
## Usage
1. open a terminal in the project folder
2. run the quiz game
```bash
python main.py
```
3. choose `yes` or `no` for admin mode
4. if you chose `yes`, enter the password from your `.env` file
5. enter your name
6. answer the questions
7. see your final score and massage
8. your result is saved in `result.txt` 

## Example
```text
do u want to open admin mode? yes/no: no
whats your name? alex
welcome

what language are we using? c++
wrong

what command starts a git? git init
correct

what command shows git status?git --oneline
wrong

your score is: 1 out of 3
keep practicing alex
```


## Roadmap
 - [x] add multiple quiz question
 - [x] calculate the finale score 
 - [x] save results to a file
 - [x] add admin mode
 - [ ] add more quiz questions
 -  [ ] add difficulty levels
 - [ ] adda timer
## Contributing 

## Licence

## Author
create by [Amir hossein](https://github.com/A_H_sourghali)