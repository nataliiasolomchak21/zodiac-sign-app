# Zodiac Sign App

Zodiac Sign App is an interactive Python terminal program, which runs in the Code Institute mock terminal on Heroku and provides a variety of information related to your zodiac sign. When you open the Zodiac Sign App, you will be greeted and asked to enter your name. The program will then prompt you to provide your birth date, and use this to determine your zodiac sign. You can also choose from several other options to see predictions for your zodiac sign, check compatibility with other signs, see your sign's description, etc.

View the live project [here](https://zodiac-sign-app-7fd49a0a9ccc.herokuapp.com/)

![Screenshot of the website on mobile, tablet, laptop and desktop from Am I Resonsive website.](README-images/am-i-responsive.png)

## User Experience

### Target Audience

* People interested in astrology and zodiac signs - Those who follow horoscopes and believe planetary positions at birth impact personality.
* Casual astrology fans - Those who may not fully believe in astrology but think zodiac signs are fun and enjoy reading horoscopes.
* Teenagers and young adults - Astrology and zodiac signs are popular among young demographics. This type of app could appeal to them.

### Key Project Goals

* Provide accurate zodiac sign information - Ensure astrological data and predictions meet quality criteria.
* Develop an engaging, interactive experience - Allow users to explore and learn about signs through a conversational interface.

### User Stories

* As a program creator, I want to:

1. Build an interactive app for the users to learn more about their zodiac signs.
2. Make the app easy to navigate.

* As a new visitor, I want to be able to:

1. Understand the purpose of the program.
2. Get feedback at all times.
3. Navigate easily through the program.

## Design Stage

### Flowchart
![Flowchart](README-images/flowchart.png)

This flowchart illustrates the overall program logic and user experience of navigating through the various features. It demonstrates how the user can easily access each feature from the main menu, which reappears after completing each one.

### Colours
* The colours for the project were added using [Python Colorama](https://pypi.org/project/colorama/)

#### Consistency

* Instructions/Explanation

Instructions or explanation for the user have white colour throughout the program. 

Example: Instructions before username input

![Instructions](README-images/instructions-explanation-colorama.png)

* Input

User input have green colour throughout the program. 

Example: Enter your name input

![User Input](README-images/input-colorama.png)

* Output

Every feature output have blue colour throughout the program. 

Example: Welcome message

![Output](README-images/output-colorama.png)

* Menu

Menu has yellow colour throughout the program. 

Example: Menu with 5 options

![Menu](README-images/menu-colorama.png)

* Errors

Errors have red colour throughout the program. 

Example: Invalid menu option choice

![Errors](README-images/error-colorama.png)

The colours compliment each other well and promote a positive emotional response in users.

### ASCII Art
![ASCII art](README-images/output-colorama.png)

This ASCII Art was created using [Text to ASCII Art Generator](https://patorjk.com/software/taag/#p=display&h=2&f=Avatar&t=Zodiac%0ASign%20APP%20). 

* Font: Big
* Character Width: Fitted
* Character Height: Fitted

## Features

### Existing Features

* __Instructions and Name Input__

  * The user is met with instructions before entering their username.
  * This feature will allow user to enter their username to start a program.
  
   ![Instructions and Name Input](README-images/instructions-and-name-input-feature.png)

* __Welcome Message__

  * The user is greeted with the ASCII Art appearing in the terminal.
  
   ![Welcome Message](README-images/output-colorama.png)

* __Menu__

  * The menu has 5 different options, each giving the user a feedback.
  * This feauture will allow the user to choose any of the given options in any order.
  
   ![Menu](README-images/menu-colorama.png)

* __1. Choose your zodiac sign__

  * The feature has two input fields, one for birth day and one for birth month.
  * This feauture will allow the user to find out their zodiac sign and gives them a little description about it.
  
   ![Choose your zodiac sign](README-images/choose-your-zodiac-sign-feature.png)

* __2. Choose a sign for compatibility__

  * The feature has two input fields, one for user sign and one for the sign the user wants to check compatibility with.
  * This feature will allow the user to find out how compatible or not they are with other zodiac signs.
  * There are three types of output for the user: "very compatible", "slightly compatible" or "not compatible". 
  * The percentage rate goes from 70 to 100% for high compatibility and from 50 to 69% for average compatibility.
    
   * High compatibility

   ![Choose a sign for compatibility](README-images/compatibility-two-feature.png)

   * Average compatibility

   ![Choose a sign for compatibility](README-images/compatibility-three-feature.png)

   * Zero compatibility
   
   ![Choose a sign for compatibility](README-images/compatibilty-feature.png)

* __3. See predictions for your zodiac sign__

  * The feature has one input field for the user to enter their zodiac sign.
  * This feature will allow the user to see 2-3 predictions for their zodiac sign.

   ![See predictions for your zodiac sign](README-images/predictions-feature.png)

* __4. See your lucky number for today__

  * The feature has one input field for the user to enter their zodiac sign.
  * This feature will allow the user to get their random number between 1 and 25 and show them the current date.

   ![See your lucky number for today](README-images/lucky-number-feature.png)

* __5. Exit program__

  * This feature will allow the user to exit the program.

   ![Exit program](README-images/exit-feature.png)

### Error Handling

1. Username input

   ![Error handling for username input](README-images/error-handling-username-input.png)

   The user is required to enter their username with letters only, starting with capital letter. Entering any other values will result in an error.
2. Menu choice

   ![Error handling for menu choice](README-images/error-handling-menu-choice.png)

   The user is required to enter numbers between 1 and 5 to choose an option from the menu. Entering any other values will result in an error.
3. Choose your zodiac sign (Option 1)

   ![Error handling for option 1](README-images/error-handling-choice-one.png)

   The user is required to enter numbers between 1 and 31 for the birth day and between 1 and 12 for the birth month. Entering any other values will result in an error.
4. Choose a sign for compatibility (Option 2)

   ![Error handling for option 2](README-images/error-handling-choice-two.png)

   The user is required to enter valid zodiac sign that starts with a capital letter. Entering any other values will result in an error.
5. See predictions for your zodiac sign (Option 3)

   ![Error handling for option 3](README-images/error-handling-choice-three.png)

   The user is required to enter valid zodiac sign that starts with a capital letter. Entering any other values will result in an error.
6. See your lucky number for today (Option 4)

   ![Error handling for option 4](README-images/error-handling-choice-four.png)

   The user is required to enter valid zodiac sign that starts with a capital letter. Entering any other values will result in an error.

This program offers a flexible user experience, adapting based on the user's knowledge. The user is not forced to navigate through irrelevant menu options. Instead, the flow adjusts to provide a tailored interaction:

If the user is unsure of their zodiac sign, they will be prompted to enter their birth date. The program will then determine and reveal their sign. However, if the user already knows their sign, they can simply enter it upfront to immediately receive customized feedback.

### Future Features

* Birth chart generator - Create more detailed astrological birth charts based on user input.
* Numerology calculator - Calculate numerology numbers and meanings based on birthday.
* Retrograde tracker - Track current and upcoming retrograde planets and their effects.

## Storage Data

For this project, I used Google Spreadsheet to store the data for the user. The username and user sign once entered for predictions are stored in a "zodiac-sign-app" spreadsheet. To achieve this, I used Google Drive and Google Spreadsheet API. When I was deploying my project, I added CREDS to the Config Vars. The creds.json file with a sensitive information is .gitignore to make sure that my credentials are not pushed to the repository.

![Zodiac Sign App Spreadsheet](README-images/spreadsheet.png)

### Code to connect to Google Spreadsheet
![Zodiac Sign App Spreadsheet Code](README-images/spreadsheet-code.png)

## Data Model

* The main entities are User and Zodiac Sign
* User has a name, birth day and birth month
* Zodiac Sign has name, description, compatibility rate, predictions and lucky number
* Compatibility, predictions and descriptions are stored in dictionaries
* User name and sign entered for predictions are stored in Google Spreadsheet
* Main operations:

  * Lookup user's sign
  * Get compatibility between different signs
  * Get predictions for each sign#
  * Generate lucky number
  * Save user data

## Testing

### Validator Testing

* No errors were returned from [CI Python Linter](https://pep8ci.herokuapp.com/)

   * Main python file (run)

  ![CI Python Linter](README-images/run-py-validation.png)

   * Signs file
  ![CI Python Linter](README-images/signs-py-validation.png)

   * Descriptions file
  ![CI Python Linter](README-images/descriptions-py-validation.png)

   * Compatibility
  ![CI Python Linter](README-images/compatibility-py-validation.png)

   * Predictions file
  ![CI Python Linter](README-images/predictions-py-validation.png)

### Manual Testing

I have manually tested this program in:

* VSCode terminal
* Codeanywhere terminal
* Code Institute Heroku terminal

Manual Testing results: 

![Manual testing](README-images/manual-testing.png)

## Bugs

### Remaining Bugs

1. I was getting this application error when I tried to open my program day after deploying:

![Applicaton Error](README-images/application-error.png)

#### Things I've tried to fix it:

* I've manually deployed once again after that and now it's working.
* Although, I still went through Build-Logs in Heroku to see what was causing the problem.
* The only suspicious thing I've found was that there are 4 vulnerabilities (1 moderate, 1 high, 2 critical).
* I asked Tutor Support for help and they said that there was nothing to worry about. 
* I sent the link to my project to our facilitator Marko Tot and he said that it worked fine, so hopefully, it will work for others.

![Tutor Support](README-images/tutor-support-one.png)
![Tutor Support](README-images/tutor-support-two.png)
![Tutor Support](README-images/tutor-support-three.png)

2. If the user enters two signs for compatibility(f.e Virgo and Leo) and then enters these same signs again, the compatibility rate will be different as it is randomized between 70 and 100 or 50 and 69. I couldn't find a better way to show compatibility, so I just left it as it was. Same goes for lucky number as it is also randomised.

3. For the spreadsheet, I wanted to save two user signs and their compatibility rate but I couldn't do it, so I stick with saving user name and a sign entered for predictions.

4. I thought that get_zodiac_sign function was too long so I was thinking about how to make it more concise. My mentor advised me to create a dictionary and iterate through it which I've tried but it wasn't successful.

### Solved Bugs

* When I was creating error handling for username input, everytime I pressed space key, it was showing "Name must start with a capital letter" instead of "Name cannot contain spaces". I fixed that by moving space error handling before capital letter error handling.

## Technologies Used

### Languages

* Python

### Additional

* [Gspread](https://pypi.org/project/gspread/) - is a Python API for Google Spreadsheet and was used to save user data in a "zodiac-sign-app" spreadsheet.
* [Time](https://docs.python.org/3/library/time.html) - defines time sleep and was used for style function.
* [Random](https://docs.python.org/3/library/random.html?highlight=random#module-random) - retuns a random number and was used to show compatibility rate between zodiac signs as well as to generate a lucky number.
* [Pyfiglet](https://pypi.org/project/pyfiglet/#:~:text=pyfiglet%20is%20a%20full%20port,the%20'block'%20font) - was used for ASCII art.
* [Colorama](https://pypi.org/project/colorama/) - makes lines in a terminal appear in different colours.
* [Datetime]() - returns today's full date and was used to show today's lucky number for user's zodiac sign.
* [google.oauth2.service_account](https://google-auth.readthedocs.io/en/stable/index.html) - is the Google authentication library for Python and was used to validate credentials and give access to Google service accounts
* [Heroku](http://www.heroku.com/) - was used to deploy the project
* [Github](https://github.com/) - was used to store the code
* [draw.io](https://app.diagrams.net/) - was used to create a flowchart

## Deployment

This project was deployed using Code Insitute's mock terminal for Heroku.

### Heroku

1. Go to Heroku and create a profile if you don't have one.
2. Click New in the upper right corner and choose "Create New App" from the menu.
3. Enter a unique application name and pick your region (Europe), then click Create App.
4. Navigate to the Settings tab and scroll down to Config Vars.
5. Click Reveal Config Vars, then add "PORT" to Key and "8000" to Value. Click Add.
6. Then, also add "CREDS" to Key and your credentials to Value if you used them.
7. Under Buildpacks, click Add Buildpack, select Python, and click to save it.
8. Repeat to add Node.js in the proper order.
9. Go back up and select the Deploy tab.
10. Choose GitHub as the deployment method and authorize the connection.
11. Search for your repo and connect it.
12. At the bottom, pick your deploy type.
13. Enable Automatic Deploys to deploy automatically on GitHub pushes, or deploy manually.



