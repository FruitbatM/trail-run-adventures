# TRΛIL RUN ΛDVENTURES

<h2 align="center"><img src="static/images/logo_trail.png" target="_blank" width="30%" height="30%"></h2>

*Developed and designed as part of Milestone Project 4: Full Stack Frameworks
with Django*

<!-- [Please view the live project here](https://trail-run-adventures.herokuapp.com/) -->

## Table of Contents

<details>

  <summary>Click to expand table of contents</summary>

1. [Overview](#overview)
2. [User Experience UX](#user-experience-ux)
    - [User Stories](#user-stories)
    - [Strategy](#strategy)
    - [Scope](#scope)
    - [Structure](#structure)
    - [Skeleton](#skeleton)
    - [Design](#design)
    - [Color Scheme](#color-scheme)
    - [Fonts](#fonts)
    - [Imagery](#imagery)
    - [Logo](#logo)
    - [Icons](#icons)
3. [Features](#features)
    - [Existing Features](#existing-features)
    - [Future Implementation](#future-implementation)
4. [Database](#database)
5. [Technologies](#technologies)
6. [Testing](#testing)
7. [Deployment](#deployment)
    - [GitHub pages](#github-pages)
    - [Forking the Repository](#forking-the-repository)
    - [Local Deployment](#local-deployment)
8. [Credits](#credits)
    - [Code](#code)
    - [Media](#media)
    - [Content](#content)
9. [Acknowledgements](#acknowledgements)
10. [Disclaimer](#disclaimer)

</details>

# Overview

The project was created as a **Milestone Project 4** as a part of **Diploma in Full Stack Software Development** with **Code Institute**. The project is developed using Django, a high-level Python web framework, JavaScript, HTML, CSS, and Bootstrap framework.

**TRΛIL RUN ΛDVENTURES** is a multi-page eCommerce web application for trail running enthusiasts and everyone who enjoys being outdoors.

Trail running is simply defined as going for a run at the heart of nature. It's an extremely all-round non-stadia sport that and you don't need to be high in the mountains to go trail running. You simply need to be in nature.

<h2 align="center"><img src="readme-files/general/project_mockup_1.jpg" alt="my account" target="_blank" width="70%" height="70%"></h2>

**Please note, this project is for educational purposes only and provided information is fictional. Nevertheless, all the website functionalities work.**

Test transaction details:

credit card: 4242 4242 4242 4242 <br>
expiration date: 04 / 24 <br>
CVC: 424 <br>
ZIP: 42424 <br>

# User Experience (UX)

## User Stories

|      As a/an...      |                         I want the ability to...                         | So that...                                      |
|:--------------------:|:------------------------------------------------------------------------:|:-----------------------------------------------:|
|                      |                                                                          |                                                 |
|                      |                                                                          |                                                 |
| Anonymous user       | easily navigate through the site on all devices                          | find what I am looking for with an ease         |
| Anonymous user       | gain understanding of the website's purpose from the home page           | decide will I continue browsing the site.       |
| Anonymous user       | read about the company details, goals and aims;                          | gain confidence that I am supporting a viable   |
| Anonymous user       | search for projects;                                                     | quickly browse which projects are available to support                |
|          ---         |                                    ---                                   |                              --                 |
| Shopper user         | view products by categories                                              | I know where to search when I look for a specific product                |
| Shopper user         | view product details                                                     | I know the product price, size description      |
| Shopper user         | search for a product by a keyword(s)                                     | I can find a specific product                   |
| Shopper user         | get purchase confirmation                                                | I can ensure the purchase was confirmed         |
| Shopper user         | register on the site                                                     | I can create my personal account                |
|          ---         |                                    ---                                   |                              --                 |
| Site admin/superuser | add new products                                                         | new products can be added to sell               |
| Site admin/superuser | edit and update products                                                 | products are up to date in terms of price, description, etc.                   |
| Site admin/superuser | delete products                                                          | products can be removed from the site in case out of stock or not availbale anymore            |
| Site admin/superuser | create blog posts                                                        | the website users are informed on interesting stories from the base camp     |
| Site admin/superuser | delete blog posts                                                        | the blog post is removed in case it becomes outdated |


## Strategy
### Project Goals


## Page Structure

<h2 align="center"><img src="readme-files/general/page_structure.jpg" alt="Page structure" target="_blank" width="90%" height="90%"></h2>

I've used [Lucidchart](https://www.lucidchart.com/) to draw Page Structure


# Features
## Existing Features

- Navbar
    - responsive on all devices
    - the logo is located in the top left corner on large devices (desktop) and in the center on the smaller devices (tablets and mobile phones). When logo is clicked it redirects a user to the home page. On smaller devices (tablet, mobile) the navbar is collapsed into a toggler.
    - a search box is a part of the top navigation loacted at upper center of navbar where a user can search for products. On mobile and tablet devices it is located under the toggler.
    - navbar contains as well my account and cart icons. The cart icon with grand total will be displayed if there are items assed to the cart. It changes colour to the green when a product is added to the cart to catch the user's attention. Clicking the cart icon redirects a user to the shopping cart page.
    - the difference in My Account display is for a regular user and for admin (super user).<br>
    

    For **Admin user** it contains Product Management, Add New Blog, My Profile, and Logout links. Under the Product Management page, the admin can add new products <br>

    <h2 align="center"><img src="readme-files/features/admin_user.jpg" alt="my account" target="_blank" width="30%" height="30%"></h2>

    For a **Regular user** it contains My Profile, Logout and Order History (only if order was placed) links. <br>

    <h2 align="center"><img src="readme-files/features/regular_user.jpg" alt="my account" target="_blank" width="30%" height="30%"></h2>

- Search Functionality
    - as previously mentioned, a search box is part of the top navigation and is, therefore, accessible on all pages.
    - it is collapsed under the hamburger menu on tablet and mobile devices as shown in the image below.
    - it allows customers to enter keywords associated with the products they wish to purchase.
    - the search results show the number of products found for the search query, as well as inform the user if no products were found.
    
    <br>

    <h2 align="center"><img src="readme-files/features/search_bar.jpg" alt="my account" target="_blank" width="50%" height="50%"></h2>

- Footer
    - the footer is standard across all pages on the website.
    - it contains fast access links, contact details and social media. There is also a copyright information.
    
    <br>

    <h2 align="center"><img src="readme-files/features/footer.jpg" alt="footer screenshot" target="_blank" width="60%" height="60%"></h2>


- Home App

- About App

- Blog App

- Contact App

- Products App

- Cart App

- Checkout App

- Profiles App


- Toasts
    - alert messages to site visitors divided into 4 categories: `toast_success`, `toast_info`, `toast_warning`, and `toast_error`
    - toasts appear on every page whenever a certain action has been done by the user.
    - their purpose is to give feedback on the action a user has just performed, such as logging in, logging out, adding a product to the cart, etc

- Django allauth
    - `django-allauth` is a Python package. According to the [django-allauth](https://django-allauth.readthedocs.io/en/latest/) docs, it is an "integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication."
    - it provides a set of features such as signup, login, logout and password change
    - after register, a verification e-mail is sent to the registered e-mail to confirm it. Once confirmed, the user can log in with their credentials and access the profile

- Interactive
    - back to top arrow button will appear on the lower right of the page when the user starts to scroll down the page
    - animate on scroll library (AOS)

- Social media
    - social media icons will be located in the footer section
    - allow users to find more information on TRΛIL RUN ΛDVENTURES on the social media

- Responsiveness
    - the website is fully responsive on all devices

- 404 and 500 error pages
    - if a user navigates to a page which does not exist or if they do not have permission to access, they will be directed to a 404 error page
    - if there are an internal problems with the server, a 500 error page will appear

## Future Implementation

- Wishlist
    - a feature that allows authenticated users to save (wishlist) items for later purchase.

- Product reviews
    - the idea would be to implement ratings and product reviews on product pages.

- Pagination

- Real time chat


# Django Apps

TRΛIL RUN ΛDVENTURES consists of 8 Django applications listed below. 
As explained in Django's documentation - a Django application describes a Python package that provides some set of features. Applications may be reused in various projects.

* `about`
* `contact`
* `home`
* `blog`
* `products`
* `cart`
* `checkout`
* `profiles`

# Information Architecture

## Database

During the development phase I worked with sqlite3 database which is installed with Django. For deployment(production), a PostgreSQL database is provided by Heroku as an add-on.

## Apps and Data Models

### **About app**

**INSTRUCTOR**
- Stores information about adventure holidays 

### **Blog app**

**BLOG POST**
- Stores information about the Blog posts.

**COMMENT**
- Stores information used in the Comment Form. It uses Django's auth's User model as a Foreign Key to allow only Registered users to post comments.

### **Checkout app**

**ORDER**
- Stores information about each placed order.

**ORDER LINE ITEM**
- Stores inormation from the order, used in the calculation in Order model. 

### **Products app**

**CATEGORY**
- Stores information about the product categories.

**LEVEL**
- Stores information about holiday products difficulty levels.

**ITINERARY**
- Stores information about holiday product itinerary

**ITINERARY DAY**
- Stores information about holiday product itinerary data, classified into days.

**PRODUCT MODEL**
- Stores product information, both shop products and holiday products.

**FAQ**
- Stores information about holiday products frequently asked questions.

### **Profiles app**

**USER PROFILE**
- Stores information about registered users and order history.

### Model Relationship Data Schema

I've used [DBDiagram](https://dbdiagram.io/home) to draw up a Database Schema.

<h2 align="center"><img src="readme-files/general/trail_run_adventures_schema.png" alt="data schema" target="_blank" width="95%" height="95%"></h2>

## Technologies
## Languages

- [HTML5](https://en.wikipedia.org/wiki/HTML5) was used to complete the structure of the website.
- [CSS3](https://en.wikipedia.org/wiki/CSS) was used to style the website.
- [Python](https://www.python.org/) was used was used for the backend of the website.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) was used to make webpage interactive.

## Frameworks, Libraries and Programs

- [Bootstrap v.5.1](https://getbootstrap.com/docs/5.1/getting-started/introduction/) was used to aid in responsive, mobile-first website design. I used Bootstrap to create grid layouts, navbar, cards, forms, buttons and other features.
- [SQLite](https://www.sqlite.org/index.html) Django built-in database as a database in development mode.
- [PostgreSQL](https://landing.aiven.io/en/aiven-for-postgresql/) (Heroku built-in) as a database in production mode.
- [Django](https://www.djangoproject.com/) 
- [Stripe](https://stripe.com/)
- [AWS](https://aws.amazon.com/) (Amazon Web Services) for hosting static files and images for the website
- [jQuery](https://jquery.com/) was used to simplify DOM manipulation.
- [Figma](https://www.figma.com/) was used to create the wireframes for the website.
- [Font Awesome](https://fontawesome.com/) icons were used throughout the website for better user experience.
- [Google Fonts](https://fonts.google.com/) was used to import the fonts to the website.
- [Favicon](https://favicon.io/favicon-converter/) was used to create the favicon for the website.
- [CSS Tricks](https://css-tricks.com/) was used as a general source.
- [W3School](https://www.w3schools.com/) was used as a general source.
- [Stackoverflow](https://stackoverflow.com/) was used as a general source.
- [GitHub](https://github.com/) was used for repository hosting and for storing the source code.
- [Gitpod](https://gitpod.io/) was used as the development environment for writing the code.
- [Git](https://git-scm.com/) was used as version control system to add, commit and push code to GitHub.
- [Adobe Photoshop Express](https://photoshop.adobe.com/) was used for resizing and cropping the images used on the website.
- [TinyJPG](https://tinyjpg.com/) was used for compressing images while preserving transparency.
- [Techsini](http://techsini.com/multi-mockup/index.php) was used to create the responsive mockup image.
- [Paint 3D](https://www.microsoft.com/en-us/p/paint-3d/9nblggh5fv99?activetab=pivot:overviewtab) was used to modifiy couple of images.
- [Coolors](https://coolors.co/) was used for colour palette used on the website.
- [CSS Autoprefixer](https://autoprefixer.github.io/) was used for adding CSS vendor prefixes.
- [Google Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools) was used to test and debug the code.
- [Animate On Scroll Library](https://michalsnik.github.io/aos/) was used to integrate animate on scroll effect on home page.
- [Randomkeygen](https://randomkeygen.com/) was used to generate random passwords and keys.
- [Canva](https://www.canva.com/) was used to design and create the brand logo and favicon


# Testing

Testing process was written in a separate file. 
Please click [here](TESTING.md) for the testing process.


## Version Control

[Git](https://git-scm.com/) as a local repository and [GitHub](https://github.com/) as a remote repository were used for this project. Detailed elaboration please find below:

1. Create a remote repository in GitHub by clicking **"New"** green button or **"New repository"** on the main page.<br>

<h2 align="center"><img src="readme-files/general/new_repository.jpg" alt="New repo button" target="_blank" width="60%" height="60%"></h2>

2. Use **Code Institute Template**, put the repository name and click Create Repository making sure to select public.<br>

<h2 align="center"><img src="readme-files/general/new_repository_create.jpg" alt="New repository" target="_blank" width="60%" height="60%"></h2>

3. Open the repository with [Gitpod](https://www.gitpod.io/). By using Code Institue Template, initialisation including initial commit is done. `gitignore` file, which is very important for the project including some confidential information, is created with Code Institute template so not necessary to create it.<br>

<h2 align="center"><img src="readme-files/general/repo_gitpod_button.jpg" alt="New repository" target="_blank" width="60%" height="60%"></h2>

**Commits**
- When a section or even a group of work is completed, it is committed in git and pushed into GitHub to make sure to keep the history of the work logged properly. Below commands are used for this:

```
git status = to check the status of new/modified folders, files, and documents
git add . = to put all new and updated work on the stage in git
git add <specific file> = used when different types of work are done but do not want to commit everything on the same commitment
git commit -m "Example commit" = commit the work on the stage in git before pushing it to GitHub
git push = update the repository in GitHub for main / master branch
```

## Deployment
TRΛIL RUN ΛDVENTURES project is hosted on the [Heroku](https://www.heroku.com/) platform with static files and user-uploaded images being hosted on [AWS S3 Basket](https://aws.amazon.com/). Heroku Postgres is used for the database. 

Below is the process of deploying the website to Heroku and setting up static files & images in AWS.

### **HEROKU**

1. Crate a new app in Heroku. Click on **New** --> **Create new app**

<h2 align="center"><img src="readme-files/deployment/heroku_new_app.jpg" alt="Heroku new app" target="_blank" width="60%" height="60%"></h2>

2. Then put the App name and select the region. Finally click 'Create app' button to create a new app.

<h2 align="center"><img src="readme-files/deployment/heroku_create_app.jpg" alt="Heroku new app" target="_blank" width="60%" height="60%"></h2>

3. Add Heroku Postgres for the database

<h2 align="center"><img src="readme-files/deployment/heroku_postgres.jpg" alt="New repository" target="_blank" width="60%" height="60%"></h2>

4. Install `dj_database_url` and `psycopg2-binary` to use Heroku Postgres, and run `pip3 freeze > requirements.txt` command to add them on requirments.txt.

<h2 align="center"><img src="readme-files/deployment/dj_database.jpg" alt="dj_database_url" width="60%" height="60%"></h2>

<h2 align="center"><img src="readme-files/deployment/psycopg2.jpg" alt="psycopg2-binary" width="60%" height="60%"></h2>

5. Update `settings.py` file located under the project directory trail_run_adventures. Import `dj_database_url`, comment out sqlite databases and add dj databases variable temporary while the database is transferred to Heroku Postgres.

<h2 align="center"><img src="readme-files/deployment/databases.jpg" alt="settings.py" target="_blank" width="60%" height="60%"></h2>

6. Run `python3 manage.py showmigrations` command to see the status of migrations (currently not migrated). Run `python3 manage.py migrate` command to migrate.

7. Import all products data. Run `python3 manage.py loaddata` command to load the **categories** first, next **levels**, **itinerary**, **itinerary_days**, **faq**  and the **products** the last. The order of loading is important as all the products are associated with categories, levels, itinerary, itinerary days and faq (frequently asked questions). Afterwards import **team** data.

8. Create a superuser with `python3 manage.py createsuperuser` command.

9. Install `gunicorn` which acts as the webserver, and freeze it into requirements file with the command `pip3 freeze > requirements.txt`

10. Create a **Procfile** which specifies the commands that are executed by the app on the startup

<h2 align="center"><img src="readme-files/deployment/procfile.jpg" alt="settings.py" target="_blank" width="60%" height="60%"></h2>

11. Temporary disable collectstatic by setting `heroku config:set DISABLE_COLLECTSTATIC = 1` and host name of Heroku to allowed hosts in `settings.py`

12. Initialise Heroku in git with `heroku: git:remote -a trail-run-adventures` and put git into Heroku with `git push heroku main`

13. Set up the automatic deployment when git is pushed to GitHub. Go to Deployment on [Heroku](https//:heroku.com), search the GitHub repository, connect and click Enable Automatic Deploys.

<h2 align="center"><img src="readme-files/deployment/heroku_deploy.jpg" alt="automatic deployment" target="_blank" width="60%" height="60%"></h2>

14. Generate a new secret key, set it in Heroku and update `settings.py` file. Change the setting of Debug mode that only True in Development mode.

<h2 align="center"><img src="readme-files/deployment/settings_debug.jpg" alt="settings.py" target="_blank" width="60%" height="60%"></h2>

15. Check the Activity Feed in Heroku to see Build in Progress to confirm automatic deployment is working.


### **AWS (Amazon Web Services)**

1. Open AWS S3 and create a new bucket, which stores the files, by completing the name and the region.

<h2 align="center"><img src="readme-files/deployment/aws_create_bucket.jpg" alt="Create bucket in AWS S3" target="_blank" width="60%" height="60%"></h2>

2. Set up the basic settings. Enable static website hosting so that it gives a new endpoint for accessing from the internet. Put index.html and error.html as default values.

<h2 align="center"><img src="readme-files/deployment/aws_hosting.jpg" alt="AWS bucket basic settings" target="_blank" width="60%" height="60%"></h2>
<h2 align="center"><img src="readme-files/deployment/aws_index_document.jpg" alt="AWS bucket basic settings" target="_blank" width="60%" height="60%"></h2>

3. Set up CORS configuration which is the access between Heroku and AWS S3 Bucket.

<h2 align="center"><img src="readme-files/deployment/aws_cors.jpg" alt="AWS bucket CORS" target="_blank" width="60%" height="60%"></h2>

4. Set up a **Bucket Policy**. Generate a policy with AWS policy generator. Add **/*** at the end of Resource to allow access to all resources in the bucket.

<h2 align="center"><img src="readme-files/deployment/aws_policy.jpg" alt="AWS bucket policy" target="_blank" width="60%" height="60%"></h2>

5. Create a user to access the bucket. Go to IAM (Identity and Access Management) and create a group for the user. Then, create a policy by importing pre-built policy.

<h2 align="center"><img src="readme-files/deployment/aws_iam.jpg" alt="AWS IAM" target="_blank" width="60%" height="60%"></h2>
<h2 align="center"><img src="readme-files/deployment/aws_iam_policy.jpg" alt="AWS IAM" target="_blank" width="60%" height="60%"></h2>

6. Attach the policy to the group

<h2 align="center"><img src="readme-files/deployment/aws_permissions_policies.jpg" alt="AWS permissions policies" target="_blank" width="60%" height="60%"></h2>
<h2 align="center"><img src="readme-files/deployment/aws_policy_name.jpg" alt="" target="_blank" width="60%" height="60%"></h2>

7. Create a user and add it to the group. When the user is added to the group, it creates csv file containing Access Key ID and Secret access key which are used to authenticate them from Django app. *It is very important to download the file and save it as you cannot download it again.*

<h2 align="center"><img src="readme-files/deployment/aws_user.jpg" alt="AWS add user" target="_blank" width="60%" height="60%"></h2>

### **Connecting to DJANGO** 

1. Install two new packages, `pip3 install boto3` and `pip3 install django-storages`, and run `pip3 freeze > requirements.txt` command to add them to the requirments.txt file.

2. Update `settings.py` file to tell Django which bucket it should be communicating with. *It is very important to keep AWS access keys secrets as these can be used to store or move data in the bucket and you will be charged by Amazon for it*

<h2 align="center"><img src="readme-files/deployment/settings_aws.jpg" alt="settings.py file" target="_blank" width="60%" height="60%"></h2>

3. Add AWS keys to Heroku and set USE_AWS = True under the app 'Settings' tab --> 'Config Vars'

<h2 align="center"><img src="readme-files/deployment/heroku_aws.jpg" alt="aws keys" target="_blank" width="60%" height="60%"></h2>
<h2 align="center"><img src="readme-files/deployment/heroku_use_aws.jpg" alt="aws" target="_blank" width="60%" height="60%"></h2>

4. Create `custome_storages.py` to tell Django to use S3 to store static files and upload images when it is in production

<h2 align="center"><img src="readme-files/deployment/custom_storages.jpg" alt="custom_storages.py file" target="_blank" width="60%" height="60%"></h2>

5. Add `AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'` to tell Django where the static files come from in production and add some settings for Static and Media files to settings.py file.

<h2 align="center"><img src="readme-files/deployment/aws_settings.jpg" alt="aws settings" target="_blank" width="60%" height="60%"></h2>

6. Add all the updates in git, commit it and push it to GitHub. Heroku runs `python3 manage.py` to collectstatic during the process which also searches through all the apps and project folders looking for static files. Then, it uses S3 domain settings in conjunction with the custom storage classes that tell the location at the URL where the things should be saved when it is in production. This can be checked in S3 bucket.

<h2 align="center"><img src="readme-files/deployment/s3_bucket.jpg" alt="s3 bucket folders" target="_blank" width="50%" height="50%"></h2>

7. Add Cache control to `settings.py` as static files do not change often and to improve the performance for users.

<h2 align="center"><img src="readme-files/deployment/cache_control.jpg" alt="aws cache control" target="_blank" width="60%" height="60%"></h2>

8. Upload product images via S3. Create a folder, and upload images.

<h2 align="center"><img src="readme-files/deployment/s3_upload_images.jpg" alt="aws cache control" target="_blank" width="50%" height="50%"></h2>

9. Verify a superuser's email address on Heroku Postgres. Login admin and check the VERIFIED and PRIMARY boxes

<h2 align="center"><img src="readme-files/deployment/admin_user.jpg" target="_blank" width="50%" height="50%"></h2>

10. Add Stripe keys to Heroku Config Vars and create a new webhook endpoint.

<h2 align="center"><img src="readme-files/deployment/heroku_stripe.jpg" target="_blank" width="50%" height="50%"></h2>

<h2 align="center"><img src="readme-files/deployment/stripe_webhook.jpg" alt="stipe webhook" target="_blank" width="50%" height="50%"></h2>

11. Create Gmail account, add email host pass & user to Heroku Config Vars and add code to `settings.py` file.

<h2 align="center"><img src="readme-files/deployment/heroku_email.jpg" alt="email settings" target="_blank" width="50%" height="50%"></h2>
<h2 align="center"><img src="readme-files/deployment/settings_email.jpg" alt="email settings" target="_blank" width="50%" height="50%"></h2>


# Credits

## Code
- Back to top arrow code with small modification was sourced from [w3schools](https://www.w3schools.com/howto/howto_js_scroll_to_top.asp)

## Media

### Images

### Icons
- All icons were sourced from [Font Awesome](https://fontawesome.com/)


## Content

Below website was used for a general layout inspiration:
TBA


# Acknowledgements

- My mentor, Mr. Spencer Barriball, for the helpful feedback and guidance.
- [Code Institute](https://codeinstitute.net/) for all course materials and ongoing support.
- Fellow Code Institute students for their feedback and suggestions.
- My family and friends for testing and useful feedback.

# Disclaimer

The information provided on this website is for educational purposes only.

# Support

For any issue resolution or assistance, please email  Marina Pavlovic at mar.pavlovic@gmail.com

> [Back to Top](#table-of-contents) 