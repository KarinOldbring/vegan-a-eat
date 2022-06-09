# **Vegan-a-eat**
![Vegan-a-eat](/static/site_images/am-i-responsive.png)
# **Vegan-a-eat**
Vegan-a-eat is a recipe sharing website for people looking for a healthier lifestyle. Site users can view recipes and if they create an account they can also interact with the site, i.e share their own recipes, comment recipes and like their favorite recipes. 

## Contents
* **Introduction**
    * Planning Stage
    * Project Goals
    * User Stories
    * Design Goals
    * Design Choices
        * Font
        * Color Scheme
        * Logo Vegan-a-eat
        * Images
    * Wireframes

* **Features**
    * Design Features
    * Existing Features
    * Future Features

* **Testing**

* **Bugs**

* **Technology Used**
    * Libraries used
    

* **Deployment** 

* **Credits** 


## **Introduction**

**Planning Stage**

When initializing this project I started off by deciding what features should be included to have a good idea of what kind of site I was making. The next step was to create wireframes to start thinking about the design of the site. After that I started working on the database models. I decided to start with the backend first, to get those part up and running and then focusing on the design. I spent quite a lot of time planning and scetching out the project, before writing any code, something that I belive to have benefitted from. 

**Project Goals**

My goal for this site is to create a user friendly site for people who want to enjoy vegan food. The idea is that people can visit the site to get inspiration, and inspire other people! By creating a user account site users can interact by sharing recipes, commenting other recipes and like recipes.

**Site Owner Goals**

* Provide the user with a professional web application. 
* Connect people who are interested in vegan food. 
* Inspire more people to eat healthy food. 

**User Goals**

* Get inspiration to enjoy more vegan food by viewing recipes. 
* Ability to share their own favorite recipes. 
* Create user account to interact. 

**User Stories**

*Applies to site users with and/or without account:*
* As a site user I can see a list of recipes so that I can choose which one to view. 
* As a site user I can click on a recipe so that I can view it in full. 
* As a site user I can register an account so that I can have access to the site. 
* As a site user I can like or unlike a recipe so that I can interact with the content. 
* As a site user I can comment recipes so that I can be part of the conversation. 
* As a site user I can delete comments that I have made. 
* As a site user I can view the comments for a recipe so that I can see read the conversation.
* As a site user I can view number of likes for a specifik recipe so that I can see which recipes are more popular.
* As I site user I can read about the site to understand the benefits of plantbased food and be encouraged to visit the site again. 
* As a site user I can create, read, update and delete posts so that I can manage my content. 
* As a site user I can log in/out so that I can interact with the site.

*Applies to site Admin/SuperUser:*
* As Admin I can like or unlike a recipe so that I can interact with the content. 
* As Admin I can comment recipes so that I can be part of the conversation. 
* As Admin I can view the comments for a recipe so that I can see read the conversation.
* As Admin I can view number of likes for a specifik recipe so that I can see which recipes are more popular. 
* As Admin I can tell site users about the benefits of plantbased food so that users will be encouraged to visit the site again. 
* As Admin I can create, read, update and delete posts so that I can manage my content. 
* As Admin I can delete posts if inappropiate so that the content of the site is relevant. 

**Design Goals**

* A site that works on all devices. 
* Clean and sophisticated design to enhance user experience. 
* Easy to understand and use.
* The style aims to give the user such a good experience that they will want to visit the site again. 

**Design Choices**

* Font

As Font I chose Playfair Display for all my headings for its playful but yet stylish design. To keep the site neat I chose to use Lato for all other text on the site. 
font-family: 'Playfair Display', serif;
font-family: 'Lato', sans-serif;

![Fonts](/static/site_images/googlefonts.png)

* Color Scheme

Since the site displays images of different vegan recipes it was important to me to keep the site clean and not take focus from the food. Hence I chose not to add lots of different colors on the site, and the colors that are present should blend in well with the theme. The nav-bar and footer have a very light green that goes well with the darker green of the logo. The orange color of the carrot in the logo is used when hovering recipes. 
Besides these colors I chose to keep the background color white and the text black. 

- Light green: #e0e7cd
- Dark green: #387d2f
- Orange: #f4900c
- White: #ffffff
- Black: #000000

![Color Scheme](/static/site_images/color-scheme.png)

* Logo Vegan-a-eat

I used [canva.com](https://www.canva.com/) to create my logo. I wanted a clean logo that goes well with the content of the site. 

![Logo](/static/site_images/logo-new.png)

* Images

The images on the site are chosen to go well with what ever images users upload. To keep consistency I have chosen to display images wiht mostly green palettes. 
    
**Wireframes**

Site moc-ups were designed using balsamiq wireframes. The focus was on defining the basic layout structure of the app and identifying how displays would change on different screen sizes such as mobile, tablet and larger screens.

![Home](/static/site_images/P4-home.png)

![About](/static/site_images/P4-about.png)

![Add Recipe](/static/site_images/P4-upload-recipe.png)

![View Recipe](/static/site_images/P4-view-recipe.png)

![Register](/static/site_images/P4-register.png)

![Login](/static/site_images/P4-sign-in.png)

*Please note, whilst the main features of the wireframes are a close match to the live website some deviations occur. For example, in the original wireframes the "Add Recipe" link was not included in the nav-bar. These changes have been made to improve UX and allow easier navigation.*

[Back to content](#contents)

## **Information Architecture**

* Database Models

![Entity Relationship Diagram](/static/site_images/ERD.png)

* Site Map

![Site Map](/static/site_images/P4-sitemap.png)

## **Features**

### Design Features

* Header
The header consists of a Navigation Bar that is consistent over all pages of the site. The Nav-Bar holds a conventionally placed logo in the top left corner of the site, which when clicked will take you back to the home page. Following the logo are links for the other pages of the site, which are altered depending on whether the user is logged in or not. When viewed on smaller screens the Nav-bar links are represented by a "burger-button", which when clicked will take the user to the desired page. 

* Home Page
When first visiting the site you are met by an image of various vegetables to fit the them of the site, and a short explanation of the sites purpose. Just beneath the image there is a welcome text that either will encourage you to Log in/Register, or greet you by your username if you are already logged in. 

* Footer
The footer is intentionally simple in order to complement the clean simplicity of the rest of the site. The Footer contains copyright information and social media links. 

### Existing Features

* **Header Logo** appears on every page for consistency and easy navigation, clicking the logo takes you back to the home page. 
* **Header Nav-Bar** appears on every page for consistency and easy navigation, the Nav-Bar toggles on smaller screens for better user experience. The Nav-Bar presents different links if the user is logged in or not.  
* **Home Page Image** is to greet the site user and instantly provide the purpose of the site. 
* **Home Page Welcome Text** is to give immediate guidance to the site user. If the user is logged in they will be greated by their username, if not there are links to Login/Register an account. 
* **Recipe Cards** are presented on the home page. The cards are paginated by six, i.e if there are more than six recipes on the site they will be displayed on another site. Arrows will point the user in the right direction for good user experience. The cards hold information of the recipe title, author, created on, number of likes and an image. If the user has not chosen a specifik image a placeholder image will be displayed. 
* **Recipe Form** can be used by logged in users. Here users who holds an account can add their own recipes, and also edit their own recipes. 
* **Comment Form** is displayed underneath each recipe when viewed in full. Logged in users can comment recipes, and also delete their own comments. 
* **Comment Section** is where all users, logged in or not can read all comments, who wrote them and when. 
* **Like/Unlike Button** appears on the recipe site and all logged in users can like/unlike recipes. Number of likes are also displayed for all users to see. 
* **About Page** gives the user information about the topic of the site. 
* **Recipe Page** is displayed when clicked on a recipe. Here all users, logged in or not, can view details about the recipe. This page also includes features to like and comment if you are a logged in user. If you are the author of the recipe, from here you can be redirected to edit/delete your recipe.  
* **Edit/Delete recipe** is where the author of the recipe can edit and/or delete their own recipes. 
* **Login Page** here users who already have created an account can log in. Users can also choose to be "remembered", a feature so that they do not have to enter their login credentials each time they log in. 
* **Register Page** is where new users can create a new account so that they can interact with the site. By creating a username, providing optional email and a required password an account is easily created. 
* **Logout** is a page for the user to confirm their wish to log out of their account. If the user clicks the sign out button, they are then redirected to the home page.

**Future Features**

* **My Recipes**

This feature would be a page where each user could see their own recipes in one place. A handy way to keep track of your own recipes and if you want to make adjustments. 

* **Search Recipes**

A search function so that users can search for example title or author, to find a specific recipe. 

* **Profile Page**

A profile page where each user could upload more information about themselves, for example profile picture to give a more community feel to the site. 

* **Categorize**

This feature is pretty simple and could in retrospect have been incorporated from the start. This feature would give you the option to choose a suitable category for your recipe when uploading it. 

[Back to content](#contents)

## **Testing**

[Back to content](#contents)

## **Bugs**

[Back to content](#contents)

## **Technology Used**

[Back to content](#contents)

## **Deployment**

[Back to content](#contents)

## **Credits**

[Back to content](#contents)