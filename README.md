<h1 align="center">PY Chatbot</h1>

[View the live project here.](https://py-centi-chatbot.herokuapp.com/)

The goal of this web application is to provide a virtual chat bot to users. The bot can be used just for entertainment.

PS: The application is running on a free tier on heroku. When the application is not used for a certain of time, Heroku tends to shut down the server. So if you get an error page the first time opening the application, just wait a few minutes and try to lunch the appliction again.


## User Experience (UX)

-   ### User stories

    -   #### Visitor Goals

        1. As Visitor, I want to be able to ask a question to the bot
        2. As Visitor, I want to be able to see the reaction from the bot and have a chat conversation


-   ### Design
    -   #### Colour Scheme
        -   The two main colours used are light blue, and black and pink.
    -   #### Typography
        -   The Shanti font is the main font used throughout the whole application with Sans Serif as the fallback font in case for any reason the fonts aren't being imported into the site correctly.
    -   #### Imagery
        -   Images are not really widely used in this project.

## Features

-   Interactive elements

-   Natural language processing

-   Form on the page for the chat conversation with the bot

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [PYTHON](https://www.python.org/)
-   [FLASK](https://flask.palletsprojects.com/en/2.2.x/)
-   [DOCKER](https://www.docker.com/)

### Frameworks, Libraries & Programs Used

1. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
1. [Heroku:](https://www.heroku.com)
    - Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.
1. [NLTK:](https://www.nltk.org/)
    - NLTK is a leading platform for building Python programs to work with human language data. It provides easy-to-use interfaces to over 50 corpora and lexical

## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

-   [W3C Markup Validator](https://validator.w3.org/#validate_by_input) - [Results] No errors were found
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results] No errors were found
-   [PYTHON](https://extendsclass.com/python-tester.html) - [Results] No errors were found

### Testing User Stories from User Experience (UX) Section

-   #### Visitor Goals

    1. As Visitor, I want to be able to ask a question to the bot

        1. Upon entering the site, there is a form with a text input field and a button
        2. Fill in any one setence question you have and press on the send button
        3. The answer to your question will be displayed shorted after the bot has it processed

### Further Testing

-   The Website was tested on Google Chrome, Microsoft Edge and Safari browsers.
-   The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhoneX.
-   A large amount of testing was done to ensure that all pages were linking correctly.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

### Known Bugs

-  

## Deployment

### Heroku

The project was deployed to Heroku using the following steps...

1. A docker file was created with instructions on how to create a docker image for this project
2. from the docker file a docker image was built and sent to the docker hub repository
3. Using Heroku cli, the docker image was pulled from docker hub, tagged and push to the Heroku containers registry
4. With Heroku cli a container was created from the docker image
5. From the container, the application was launched and Heroku assigned the application a port number to maake it accessible

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/miguel-moukimou/miguel-moukimou.github.io)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/miguel-moukimou/war-facts-quiz)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Credits

### Code


-   [MDN Web Docs](https://developer.mozilla.org/) : For Pattern Validation code. Code was modified to better fit my needs and to match an Irish phone number layout to ensure correct validation. Tutorial Found [Here](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/tel#Pattern_validation)

### Content

-   All content was written by the developer.

### Media

### Acknowledgements

-   My Mentor for continuous helpful feedback.

-   Tutor support at Code Institute for their support.