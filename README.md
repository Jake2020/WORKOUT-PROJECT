# JAKE'S WORKOUT PROJECT - CS50 FINAL PROJECT

#### Video Demo: https://www.youtube.com/watch?v=tGV3E-3xHKE

#### DESCRIPTION: My project is a website which allows the user to create an account, then create and save full body Push, Pull, Legs workout plans. This is achieved by prompting the user to chose from a selection of exercises and rep ranges which will generate a workout plan. This plan will be saved to a database so the user can come back and repeat the workout in future. There is also the option to view workouts created by other users and do one of their workouts instead.

###### ######################################################################
## Quick Start Guide:

###### Launching Website:
In "project" folder execute "flask run" and follow link to launch website.

Viewing Database (If required - Not needed to launch website):
In "project" execute "sqlite3 project.db" to launch database

###### ######################################################################

I have taken the CS50 Finance project and used it as a starting point for creating my own website and database project. I have done this so that I can start with something I know can be run and modified through CS50's instilation of VSCode. This allows me to focus on creating the specific webpages and structure I want for my website and to focus on the coding for the back end.

The webpages are coded in HTML, CSS, and JavaScript.

The back end is coded in Python.

As with the CS50 Finance problem set the website runs on a Flask server and used a SQLite database

###### ######################################################################

#### Pages:

Login & Register - These 2 pages and their functionality are lifted directly from Finance. I didnt see any reason to change them.

Index/home - This is a very simple web page with just 2 buttons to navigate to the useful parts of the website. You can either "Start Workout" or "Create New Workout"

Create New Workout - This page allows the user to create a workout by selecting from the options available. The options are currently quite limited but I have got the site to a functioning state and may expand it in future. Once the options are selected the users workout is saved in the "workout" database where it can be pulled up and followed by any user in future.

Start Workout - This page give the user the option to select any workout in the database presenting their choice as "[workout name] made by [username]". Once selected the full workout is generated and displayed in the users browser so they can follow along.

#### app.py:

This is the Python code for the project that control all of the functionality such as what happens with GET or POST requests and which pages to render.

#### project.db:

This is the SQLite database that holds info on the users and workouts. It contains 2 tables. The first is users which is the same as in CS50's Finance and the second is a custom table to hold info about the users created workouts.

###### ######################################################################

#### Reflections:

I spent a decent amount of time on this project and didn't really have the time to spend any more. I would have liked to have spent some time on the styling to make the Create Workout form and the display of the workout nicer. I would also, if I would have had more time, have included a much larger selection of exercises and maybe even split the exercises into days e.g. Cardio, Arms. As it stand now I am happy I have produced a functional website that can be build upon in future.

###### ######################################################################