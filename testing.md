# Vegan-a-eat

[Main README.md file](/README.md)

[View live project here](https://vegan-a-eat.herokuapp.com/)

[View GitHub repository](https://github.com/KarinOldbring/vegan-a-eat)

***
## Contents
* Testing User Stories
* Manual Testing
* Automated Testing 
    * Code Validation
    * Browser Validation
* User Testing


***

## Testing User Stories

### User Stories 

*Applies to site users with and/or without account:*

1. As a site user I can see a list of recipes so that I can choose which one to view.
    * The list of recipes on the home page has been paginated by six. If there are more than six recipes, the remainder moves to the next page. This will continue until there are six or less recipe cards on the one page. The recipe cards show a preview of the recipe to give the user an overview of each recipe. 
2. As a site user I can click on a recipe so that I can view it in full.
    * When a site user clicks a recipe card, the recipe will be displayed in full. The user can now see full ingredients list, instructions and cooking time among other things. 
3. As a site user I can register an account so that I can have access to the site.
    * Any site user that wishes to interact with the page can easily create an account. There are links to register an account in both the navigation bar at the top of the page and in the middle of the home page. If the user tries to access a page or a function that requires Login there are links as well. 
4. As a site user I can like or unlike a recipe so that I can interact with the content.
    * All logged in site users can like or unlike recipes that they find more interesting, thereby helping others see which recipes are more popular. The number of likes is automatically incremented and the change is visible both on the recipe page and the recipe card on the home page.
5. As a site user I can comment recipes so that I can be part of the conversation.
    * All logged in site users can comment their own or other users recipes.
6. As a site user I can delete comments that I have made.
    * All logged in site users can delete their own comments. Below their own comments is a "Delete comment" button displayed. If pushed that specific comment will be deleted.
7. As a site user I can view the comments for a recipe so that I can see read the conversation.
    * Any site user can view the comments made by other users and thereby follow any conversation. 
8. As a site user I can view number of likes for a specifik recipe so that I can see which recipes are more popular.
    * Any site user can view number of likes for each recipe. Number of likes are displayed both in the recipe overview and if a recipe is viewed in detail. 
9. As I site user I can read about the site to understand the benefits of plantbased food and be encouraged to visit the site again.
    * Any site user can visit the About page to read a little more about the page and the benefits of Vegan food. 
10. As a site user I can create, read, update and delete posts so that I can manage my content.
    * All logged in site users can add new recipes, view in full, and update and delete their own recipes. If the site user is the author of a recipe viewed in full, there will be options to edit and delete that specific recipe.
11. As a site user I can log in/out so that I can interact with the site.
    * All users with an account can log in and out of the page. The navigation bar at the top will show either Login or Logout depending on whether the user is logged in or not. On the Home page the user will also be greeted by name if logged in. Ta make it even more user friendly an alert will pop ut when the user either logs in or out. 


    *Applies to site Admin/SuperUser:*

1. As Admin I can tell site users about the benefits of plantbased food so that users will be encouraged to visit the site again.
    * By using the About Page Admin can tell the site users about the benefits of plant-based food. 
2. As Admin I can create, read, update and delete posts so that I can manage my content.
    * As Admin it is important to also take part in inspiring the site users by presenting appealing recipes. 
3. As Admin I can delete recipes if inappropiate so that the content of the site is relevant.
    * Through the Admin site the Super User can delete recipe entries if they do not match the purpose of the site. 
4. As Admin I can delete comments if inappropiate so that the conversations on the site maintain a high level. 
    * It is crucial for the Super User to be able to make sure that the site does not host any hostile or offensive comments. 

[Back to content](#contents)

## Manual Testing

### Navigation Bar

#### Navigation Bar 

* Expected Outcome: The navigation bar should be visible on every page of the site. If page is rendered on smaller screens the navigation bar should toggle for better user experience. 
* Test: Visit every page of the site to check if navigation bar is visible. View the navigation bar on different size screens to check responsiveness of navigation bar and toggle function. 
* Result: The navigation bar is visible on every page of the site. When viewed on smaller screens the links are toggled for better user experience. 
* Verdict: Code functions as intented.

#### Logo

* Expected Outcome: When clicking the logo, the user should be redirected to home page. 
* Test: I tried clicking the logo from all different pages on the site, both as logged in user and not. 
* Result: Every time I clicked the logo I was redirected to home page. 
* Verdict: Code functions as intented.

#### Home Link

* Expected Outcome: When clicking on Home link, the user should be redirected to home page. 
* Test: I tried clicking the Home link from all different pages on the site, both as logged in user and not. 
* Result:Every time I clicked the Home link I was redirected to home page. 
* Verdict: Code functions as intented.

#### About Link

* Expected Outcome: When clicking on About link, the user should be redirected to About page.
* Test: I tried clicking the About link from all different pages on the site, both as logged in user and not.
* Result: Every time I clicked the About link I was redirected to About page.
* Verdict: Code functions as intented.

#### Add Recipe Link

* Expected Outcome: When clicking on Add Recipe, the user should either be redirected to Add Recipe page if logged in or Login page if not. 
* Test: I tried clicking the Add Recipe link both as logged in user and as user not logged in. 
* Result: When clicking the Add Recipe link as logged in the user is redirected to Add Recipe. If the user is not logged in the user is redirected to the Login page. 
* Verdict: Code functions as intented.

#### Register Link

* Expected Outcome: If the site user is not logged in, the Register Link will be displayed in the Navigation Bar. When clicked, the user should be redirected to Register account page. 
* Test: Enter the site as a user not logged in, then click Register link. 
* Result: When not logged in the Register link is visible, when clicked the user is redirected to Register account page. 
* Verdict: Code functions as intented.

#### Login Link

* Expected Outcome: If the site user is not logged in, the Login Link will be displayed in the Navigation Bar. When clicked, the user should be redirected to Login page. 
* Test: Enter the site as a user not logged in, then click Login link.
* Result: When not logged in the Login link is visible, when clicked the user is redirected to Login page.
* Verdict: Code functions as intented.

#### Logout Link

* Expected Outcome: If the site user is logged in, the Logout Link will be displayed in the Navigation Bar. When clicked, the user should be redirected to a Logout page to confirm they wish to log out. 
* Test: When logged in, click the Logout Link. 
* Result: When logged in the Logout link is visible, when clicked the user is redirected to Logout page. 
* Verdict: Code functions as intented.

### Footer

#### Footer

* Expected Outcome: The footer should be visible on all pages of the site and always be placed on the bottom of the page. 
* Test: Visit every page of the site to check if footer is visible. 
* Result: The footer is visible on every page of the site. 
* Verdict: Code functions as intented.

#### Footer Links

* Expected Outcome: The icons for social media in the footer are supposed to be opened up in new tabs when clicked. 
* Test: Click the social media icons in footer. 
* Result: When clicking the icons the social media is opened up in a new tab. 
* Verdict: Code functions as intented.

### Welcome Text

#### Welcome Text - not logged in

* Expected Outcome: If user is not logged in, a welcome text with clickable links to Login/Register account should be displayed on the home page. 
* Test: Enter the site when not logged in. 
* Result: When entering the site as a user not logged in, a welcome text with fully functional clickable links is displayed. 
* Verdict: Code functions as intented.

#### Welcome Text -logged in

* Expected Outcome: If user is logged in, a welcome text displaying the users username should be displayed on the home page. 
* Test: Enter the site when logged in. 
* Result: When entering the site as a logged in user, a welcome text displaying the correct username is displayed. 
* Verdict: Code functions as intented.

### Recipe List

#### Recipe Overview

* Expected Outcome: When entering the site a list of recipes are supposed to be displayed. The list should present a preview of each recipe with some basic information. 
* Test: Enter the site to check if recipes are displayed. 
* Result: When entering the site a list of recipes are presented. Each recipe cards presents a preview of an image, author, title, excerpt (if available), created date and number of likes. 
* Verdict: Code functions as intented.

#### Page Pagination

* Expected Outcome: To make the site more user friendly there should be a maximum of 6 recipes displayed at once. When there are 6 recipes on the page it should paginate and the user should be able to click to get to the next page. 
* Test: Check if page pagination is activated if there are more than 6 recipes on the site by adding a larger number of recipes. 
* Result: The seventh recipe that was added to the site was displayed on a second page, visible if the next button was clicked. 
* Verdict: Code functions as intented.

### View Recipe

#### Recipe Detail

* Expected Outcome: When a specifik recipe is clicked the recipe should open on a recipe detail page. On this page you can see an image, title, excerpt (if available), author, updated on, ingredients, instructions and created on. 
* Test: Click a recipe to check that it opens up and reveals all information. 
* Result: When a recipe is clicked it opens up and reveals information, but not the cooking time. 
* Verdict: Code functions as intended but the cooking time is missing in the template. 
* Solution: Add cooking time to recipe detail template. 
* Test 2: Click a recipe to check that it opens up and reveals all information, including cooking time. 
* Result 2: When a recipe is clicked it opens up and reveals all available information, including cooking time. 
* Verdict: Code now functions as intented.

#### Likes

* Expected Outcome: When viewing a recipe in full number of likes is supposed to be displayed and if the user is logged in the ability to like/unlike should be available. 
* Test: Open a recipe to see if likes are visible and check that the heart icon is clickable and generates a like. 
* Result: Number of likes are displayed and if the user is logged in the heart is clickable and generates another like. 
* Verdict: Code functions as intented.

#### View Comments

* Expected Outcome: When viewing a recipe in full all comments are supposed to be displayed showing the oldest one first. 
* Test: Open a recipe to see if comments are available to all users and that they are displayed oldest first. 
* Result: Comments are displayed to all users, logged in or not. The oldest comment is presented first. 
* Verdict: Code functions as intented.

#### Delete Comment

* Expected Outcome: A logged in user is supposed to be able to delete their own comments in an easy and intuitive way. 
* Test: Log in to see if my comments can be deleted by me only. 
* Result: When logged all comments are displayed and the ones created by me are presented with a "Delete Comment" button underneath. When this is clicked the comment disappears. The site user is then redirected home. 
* Verdict: The code function to delete comment works as intented, although a future version of this site would keep the site user on that specific recipe instead of being redirected to home page. This is connected to the issue with unique slugs mentioned in the Bugs section in Readme.md. 

#### Create Comments

* Expected Outcome: When viewing a recipe in full a logged in user is supposed to be presented with the option to leave a comment. If the user is not logged in a Login/Register option should be available stating that it's necessary to be logged in to be able to leave a comment. 
* Test: Log in as logged in user to leave a comment, visit page when not logged in to see options. 
* Result: When viewing a recipe in full as logged in user the option to leave a comment in presented. When a comment is entered and the user presses the "Submit" button the comment is displayed in the comments section. If the user is not logged in there is a text stating that you need to be logged in to comment, the text presents clickable links to Login/Register. 
* Verdict: Code functions as intented.

#### Manage Recipe

* Expected Outcome: When a logged in user is viewing their own recipes, an option to Edit or Delete the recipe should be presented. If the site user is not the recipe author, there should be no option to manage recipe. 
* Test: View a recipe that I am the author of, wiew another users recipe and view a recipe as not logged in user. 
* Result: When viewing my own recipe an option to Edit or Delete recipe is clearly presented. When viewing a recipe that I am not the user of, or when not not logged, there is no option to manage recipe. 
* Verdict: Code functions as intented.

#### Edit Recipe

* Expected Outcome: When wieving your own recipes you are supposed to be presented with the option to Edit your recipe. When this button is clicked an Edit Recipe view is opened and all features of the recipe can be edited. 
* Test: View my own recipe, click Edit button and edit the recipe. 
* Result: The Edit Recipe view opens when the button is clicked and all features of the recipe can be edited. After the recipe has been edited and the Submit button is clicked, the recipe is updated and the user is redirected to the home page. 
* Verdict: The code function to Edit recipe works as intented, although also here there is an issue with the unique slug as presented in the Bugs section in the Readme.md. In a future version of the site the user would have been taken back to the recipe detail instead of being redirected to the home page for better user experience. 

#### Delete Recipe

* Expected Outcome: 
* Test: 
* Result: 
* Verdict: 

#### 

* Expected Outcome: 
* Test: 
* Result: 
* Verdict: 

[Back to content](#contents)

## Automated Testing
* Code Validation
* Browser Validation

[Back to content](#contents)

## User Testing

[Back to content](#contents)