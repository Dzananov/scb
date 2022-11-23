Foody Hamburger Resturant is A fictional resturante located in Malmö, Sweden. A app has been designed to informe the user about the resturant and what they can expect, give information about what kind of food the resturant serves, user are able to become members and reserve a table and afterwards users can manage their bookings

# Content
* [User Story](#User-Story)
  * [Goal](#Goal)
  * [User Stories](#User-Stories)
 
* [Design](#Design)
 * [Colour](#Colour)
 * [Font](#Font)
 * [Wireframe](#Wireframe)
* [Features](#Features)
 * [Existing-Features](#Existing-Features)
 * [Future-Features](#Future-Features)
* [Technology](#Technology)
 * [Testing](#Testing)
 * [Bugs](#Bugs)
* [Credits](#Credits)
* [Deployment](#Deployment)
 * [Heroku](#Heroku)
 * [Github](#Github)

# User Story
## Goal
Main Goal of the project is to provide a backend to my frontend. The backend is supposed to build up the models and the whole base of the app. App works as a post-picture-blog for horselovers where user can sign up and post pictures with content. Other users can then comment eachothers posts.

## User Stories
* User should be able to sign up and later on sign in and sign out: 
As a user I can sign up so that i can sign in, sign out and book a table
* When signed in user should se a option for watching their feed, press home, add post, sign out.
* When a post is posted: 
As a user I can edit my post so that I can make changes
As a user I can see my post so that I can manage them
<!-- As a user I can delete my post so that I dont have that post anymore
As a loged in site visiter I can add and delet comments -->





# Design

Design is maninly code Institution Boilerplate styling codes with miner changes:
I added pictures and logo
<!-- I changed colortexting and navbar -->




# Features
## Existing Features
* a Profile/user app that can take user information.
* A comment app that can take comment information
* A follower app that can take follow signals from the frontend
* A post app that take information regarding post component in the frontend.


## Future Features

* Add a rate app. As a User I want to be able to rate a post from 1-5.
* as a post owner I want to be able to se when and who rates my post.

# Technology

## Validator

* PEP8 check. I had some error regarding the to long lines in my codes. But also I got error for not having a whitespace around operator '=' on line 22,24,25,55. If I put I whitespace there my code do not work proparly.
![bild](readme.images/pep8valdiator.jpg)

* W3 HTML Validator: I got errors on all my static files. I choose to ignore them because the images worked just fine.
![bild](readme.images/htmlvali.jpg)

* Jigsaw validator for CSS o errors detected
![bild](readme.images/cssvali.jpg)

## Languages
* Python

<br>

* Frameworks
  * Python Built-in Modules

* Packages

  * cloudinary
  * dj-database-url
  * dj3-cloudinary-storage
  * Django
  * django-allauth
  * gunicorn


* Libraries
  * Allauth

* Programs
  * GitPod:
  * Gitpod was used as IDE to commit and push the project to GitHub.
  * GitHub:
  * Was used for all storing and backup of the code pertaining to the project.

## Testing
I did testing on my webpage troughout the project: Testings performed:

|Test | What to do | Status |
|----|:---------|:-------|
|Tested my database | on Herouku i clicked on resources on the navbar and than on the added postgres link. It will display a page with a succsess message  | good |
|To se if the url path workes in profile app| Open app in preview browser and wrote "/profiles" on the end of url shown i preview| good |
|To se if the url path workes in post app||Open app in preview browser and wrote "/post" on the end of url shown i preview| Open app in preview browser| good |




## Bugs
|Test | What to do | Status |
|----|:---------|:-------|
|Did not render to the URL| My Profile Url link did not work. I Typed it in on my preview url as /profiles/. Got an error. Went to the main url in app "scb" and saw a typing error insted of "...profiles" it said ".../profile".| fixed |

|

# Deployment
## Heroku

  * Logged in to my account on herouku
  * At dashboard I created a new app called "saddleclubbackend" and chose region Europe
  * In Resources I searched for PostGres in the add-ons to use as my database
  * In settings I revelde my config vars 
  * Stored seacret_key in env.py 
  * added seacret_key to config vars
  * I Connected the database from Herouku(confik vars) and past them in my env.py and I also created a secret key in env.py and copy past the same in my config vars.
  * I referenced this in settings.py
  * I added the value of 8000 and key to config vars
  * I connected cloudinary to env.py and my herouku with the same value and key
  * Added Allowed Hosts in settings
  * Went to the deploytab in herouku
  * searched for my github repo(my github was already connected)
  * Then clicked on deploy branch 

## Github
  * Log in to github
  * Go to repositaries
  * Click on relevant repositery
  * Go to settings
  * Click on pages at the sidebar
  * Choose to save on 'main'
  * Save

# Credits


* 
  * Code institutes walktrough project "Hello Rest" Was and inspiration when building the view
  * Code institut for profile app and followers app
  * Django was used for the fuctionalitis 
  * Sign in/sing up and sign out codes are from allauth and the css are from the walktrough project


## Thanks to
* Code Institution for education
* My mentor for mentroing and pushing me to always try my best
* Tutor support for all help resolving issus
