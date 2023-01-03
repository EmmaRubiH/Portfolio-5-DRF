# THE SPACE - API - Social Media

![ami](/images/amiresponsive.png)

## ABOUT:
<hr>
The space is a online blog, social media platford where users can create a profile and post their images along with a title and content. Users can also view other users profiles, comment, like and favourite them.

## Project

This repository is the backend of the application using the Django REST Framework(DRF) holding the API database for the front end part of the application.

## Technologies and Libraries
<hr>

### Language used

*Python - The Django REST Framework 

### Frameworks, libraries and programs

* Cloudinary Storage
  * storage of images
* Pillow
  * image processing capabillities
* Psycopg2
  * PostgreSQL database adapter for python
* JSON web tokens
  * Http-safety, web-tokens for kepping user logged in, authentication etc.
* Git
  * version control, committing and pushing to Github
* Github
  * storing the repository, files and images
* Gitpod
  * IDE used to code project
* Heroku
  * used to deploy the application
* Django rest auth
* PostgreSQL
* Cors headers

## Initial plan
<hr>
This project was planned in the begining as a Diary page, but it was switched to follow the walkthrough from the lessons on Rest-framework and React.

## Plan 
<hr>
The current direction for this project is to follow the walkthrough given by Code Institute and add two unique models. These are popular and Contacts in contacts. popular model (to store the most liked posts) contact(to contact another user).


## LucidChart
<hr>

![lucidchart](images/lucid.png)

## User Goals
<hr>

### User Goals:


* As a site user I can register an account
* As a site user I can delete my account
* As a site user I can create posts
* As a Site User I can Edit and Delete that Post at want
* As a Site User I can Follow and Unfollow other Users
* As a Site User I can Comment on other Users Posts
* As a Site User I can Edit and Delete the Comment I own
* As a Site User I can Like and Unlike Posts from other Users Posts

- I did this in the begining, so the Site user stories for popular and contact is not made in issues and project.

# Testing:
<hr>

I tested the API manually to ensure everything was working for my project.

* When testing my superuser administrator in my back-end I can confirm all data entered from the front end is displaying!

* checking that search feature returns correct
* Manually verified each url path created to confirm they work and open without error
* Testing that the CRUD functionality is available in: User, Post, Profile, Comments, Followers, Likes, Populars.
* testing errors (details: not found) is working.
* Creating a new item with url path
* testing if editing a post and deleting a item works.


## Bugs:
Could not get the frontend and backend to sync (with the posts). It was a spelling mistake. hade write post (so forgot the s). 

# Credits
<hr>

## Media:

images is the same from the drf walkthrough project.

## Content:

* The biggest credit has to go Code Institute, I followed the Walkthroughs given, and developed a little on top of it.
* Thanks to my mentor jubril and the slack-channel.



