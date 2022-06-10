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