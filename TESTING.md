# Testing
## Table of Contents
<details>
  <summary>Click to expand table of contents</summary>

1. [Testing User Stories](#testing-user-stories)
2. [Code Validation](#code-validation)
3. [Functionality Testing](#functionality-testing)
4. [Encountered Issues](#encountered-issues)
5. [Web Accessibility](#web-accessibility)
6. [Performance Testing](#performance-testing)
</details>

# Testing User Stories

Manual tests were carried out across all user stories and features:

## Test Case 1

> As a potential customer I want the ability gain understanding of the website's purpose from the home page so that I can decide will I continue browsing the site.

**Description:**
Verify that the website's purpose is clear when a user navigates to the sites homepage.

**Steps:**
1. Open internet browser of choice.
2. Navigate to [TRΛIL RUN ΛDVENTURES](https://trail-run-adventures.herokuapp.com/).
3. Read the headline and subheadline on the hero image.
3. Strategically placed headline and subheadline indicate to the user what is the website's purpose.
4. Scroll to the content beneath the website's hero image and read the main heading and paragraph.

**Expected Result**
- Strategically placed headline and subheadline on the hero image indicate to the user what is the website's purpose.
- A first section on the home page explains in more detail the website's purpose.

**Actual Result:**
- Strategically placed headline and subheadline on the hero image indicate to the user what is the website's purpose.
- A first section on the home page explains in more detail the website's purpose.

**Pass/Fail:**
Pass

*Image Test 1 A*
  <h2 align="center"><img src="readme-files/testing/test_1_a.jpg" alt="Test case 1 A" target="_blank" width="60%" height="60%"></h2>

*Image Test 1 B*
  <h2 align="center"><img src="readme-files/testing/test_1_b.jpg" alt="Test case 1 B" target="_blank" width="60%" height="60%"></h2>


## Test Case 2

> As a potential customer I want the ability to easily navigate through the site on all devices so that I can find what I am looking for with an ease.

**Description:**
Verify the website's responsiveness across different device types.

**Steps:**
1. Open internet browser of choice.
2. Navigate to [TRΛIL RUN ΛDVENTURES](https://trail-run-adventures.herokuapp.com/).
3. Test the responsiveness of the website on each available device.
4. Document the results.

**Expected Result**
 The site will be responsive across all available devices.

**Actual Result:**
- The website was primarily tested on the following devices:
    - iPhone 11
    - iPhone 7
    - Samsung Galaxy Tab A
    - Lenovo ThinkBook 13S
    - Monitor 31.5" PHILIPS 322E1C

- Other tests were performed to determine the site's responsiveness using Google Dev Tools in order to view the site on a variety of devices.

**Pass/Fail:**
Pass

  <h2 align="center"><img src="readme-files/general/project_mockup_1.jpg" alt="Test case 2" target="_blank" width="80%" height="80%"></h2>

## Test Case 3

> As a potential customer I want the ability to create an account easily so that I can purchase products.

**Description:**
Verify that the site provides the user with an ability to create an account easily.

**Steps:**
1. Open internet browser of choice.
2. Navigate to [TRΛIL RUN ΛDVENTURES](https://trail-run-adventures.herokuapp.com/).
3. Click on 'My Account' icon in the navigation bar. And click on Register tab.
4. Fill out the registration form.
5. Log in with the credentials that were created when filling out the registration form.

**Expected Result**
When the user clicks on the Register tab, a registration form will get displayed and once successfully completed and submitted the user will receive an email asking her/him to verify their account. Once the user's email has been verified the user will be able to log in with the credentials they have created.

**Actual Result:**
A registration form is displayed and once successfully completed and submitted the user receives the email asking them to verify their account. Once the user's email has been verified they are able to log inwith the credentials they have created.

**Pass/Fail:**
Pass

*Image Test 3 A*
  <h2 align="center"><img src="readme-files/testing/test_3_a.jpg" alt="Test case 3 A" target="_blank" width="60%" height="60%"></h2>

*Image Test 3 B*
<h2 align="center"><img src="readme-files/testing/test_3_b.jpg" alt="Test case 3 B" target="_blank" width="30%" height="30%"></h2>

## Test Case 4
> As a potential customer I want the ability to the ability to have an option to search for products by the name so I can find what I am looking for.

**Description:**
Verify search feature works as expected.

**Steps:**
1. Open internet browser of choice.
2. Navigate to [TRΛIL RUN ΛDVENTURES](https://trail-run-adventures.herokuapp.com/).
3. Locate the search bar located at upper center of navbar on desktop. On mobile and tablet devices it is located under the hamburger menu.
4. Search for 'sweatshirt' to confirm that displayed products have 'sweatshirt' in their name.

**Expected Result**
Only products that contain 'sweatshirt' in their name will get displayed to the user.

**Actual Result:**
Only products that contain 'sweatshirt' in their name will get displayed to the user.

**Pass/Fail:**
Pass

  <h2 align="center"><img src="readme-files/testing/test_4.jpg" alt="Test case 4" target="_blank" width="60%" height="60%"></h2>

## Test Case 5

> As a potential customer I want the ability to view product details so I can decide will I make the purchase.

**Description:**
Verify product detail page works as expected.

**Steps:**
1. Open internet browser of choice.
2. Navigate to [TRΛIL RUN ΛDVENTURES](https://trail-run-adventures.herokuapp.com/).
3. Click on the 'Shop' tab and select (click on) 'MALE T-SHIRT ORANGE'
4. Confirm the product detail page with 'MALE T-SHIRT ORANGE' opens as expected.

**Expected Result**
The product detail page for the selected product gets displayed to the user.

**Actual Result:**
The product detail page for the selected product gets displayed to the user.

**Pass/Fail:**
Pass

  <h2 align="center"><img src="readme-files/testing/test_5.jpg" alt="Test case 5" target="_blank" width="60%" height="60%"></h2>

## Test Case 6

> As a potential customer I want the ability to read insightful blog posts so I can get an opportunity to learn something new.

**Description:**
Verify blog and blog post pages works as expected.

**Steps:**
1. Open internet browser of choice.
2. Navigate to [TRΛIL RUN ΛDVENTURES](https://trail-run-adventures.herokuapp.com/).
3. Click on the 'Blog' tab. Click on the blog post of your choice.
4. Confirm the blog page and blog post page open as expected.

**Expected Result**
The blog page and blog post page gets displayed to the user.

**Actual Result:**
The blog page and blog post page gets displayed to the user.

**Pass/Fail:**
Pass

  <h2 align="center"><img src="readme-files/testing/test_6_a.jpg" alt="Test case 6" target="_blank" width="60%" height="60%"></h2>
  <h2 align="center"><img src="readme-files/testing/test_6_b.jpg" alt="Test case 6" target="_blank" width="60%" height="60%"></h2>

## Test Case 7

> As a shopper user I want the ability to view products by categories so I can I know where to search when I look for a specific product.

**Description:**
Verify 

**Steps:**
1. Open internet browser of choice.
2. Navigate to [TRΛIL RUN ΛDVENTURES](https://trail-run-adventures.herokuapp.com/).
3. Click on the 'Shop' tab.
4. Confirm category options are available from the dropdown menu.

**Expected Result**
Shop product categories get displayed to the user.

**Actual Result:**
Shop product categories get displayed to the user.

**Pass/Fail:**
Pass

## Test Case 8
> As a shopper user I want the ability to view product details so I can know the product price, size, and description.

## Test Case 9
> As a shopper user I want the ability to get purchase confirmation so I can ensure the purchase was confirmed.

## Test Case 10
> As a shopper user I want the ability to register on the site so I can create my personal account.

**Description:**
Verify that the website provides the user with an opportunity to create a personal account.

**Steps:**
1. Open internet browser of choice.
2. Navigate to [TRΛIL RUN ΛDVENTURES](https://trail-run-adventures.herokuapp.com/).
3. Click on the 'My Account' icon located in the top navigation and click on the 'Register' tab. 
4. Fill out the registration form.
5. Verify the email address.
6. Log in with the credentials that the user created when filling out the registration form.

**Expected Result**
A registration form will be displayed and once successfully completed and submitted the user will receive an email asking them to verify their account. Once the user's email has been verified they will be able to log in easily with the credentials they have created.

**Actual Result:**
A registration form is provided and once successfully completed and submitted the user receives an email asking them to verify their account. Once the user's email has been verified they are able to log in easily with the credentials they have created.

**Pass/Fail:**
Pass

  <h2 align="center"><img src="readme-files/testing/test_10_a.jpg" alt="Test case 10" target="_blank" width="60%" height="60%"></h2>

  <h2 align="center"><img src="readme-files/testing/test_10_b.jpg" alt="Test case 10" target="_blank" width="60%" height="60%"></h2>

  <h2 align="center"><img src="readme-files/testing/test_10_c.jpg" alt="Test case 10" target="_blank" width="60%" height="60%"></h2>

  <h2 align="center"><img src="readme-files/testing/test_10_d.jpg" alt="Test case 10" target="_blank" width="60%" height="60%"></h2>

  <h2 align="center"><img src="readme-files/testing/test_10_e.jpg" alt="Test case 10" target="_blank" width="60%" height="60%"></h2>

## Test Case 11
> As a shopper user I want the ability to easily view the shopping cart at any time so I can easily proceed to the checkout page.

## Test Case 12
> As a shopper user I want the ability to view items I have added to my shopping cart at any time so that I can identify the subtotals and the total cost of my purchase.

## Test Case 13
> As a shopper user I want the ability to be able to adjust quantity of a particular item in the shopping cart so that I can make changes before the checkout.

## Test Case 13
> As a shopper user I want the ability to go through an orderning process in a simple way so that I can have a great user experience.

## Test Case 14
> As a site admin/superuser I want the ablity to add new products easily so that new products can be added to sell.

## Test Case 15
> As a site admin/superuser I want the ablity to edit and update products so that products are up to date in terms of price, description, etc.

## Test Case 16
> As a site admin/superuser I want the ablity to delete products so that products can be removed from the site in case out of stock or not availbale anymore.

## Test Case 17
> As a site admin/superuser I want the ablity to create blog posts so that the website users are informed on interesting stories from the base camp.

## Test Case 18
> As a site admin/superuser I want the ablity to delete blog posts so that the blog post is removed in case it becomes outdated.

**Description:**
Verify that the admin user can delete the blog post and that he/she will be prompted with a modal notification when 'Delete' link is clicked to make sure this is the correct action. 

**Steps:**
1. Open internet browser of choice.
2. Navigate to [TRΛIL RUN ΛDVENTURES](https://trail-run-adventures.herokuapp.com/).
3. Login as admin user (superuser)
4. Click on the 'Blog' tab. 
5. Click on 'Delete' link located at the bottom of a blog post.
6. Modal notification window appears notifying that you are about to delete a blog post and does the user wish to proceed.

**Expected Result**
A delete link will be displayed when the user logins with the admin permission. Once the delete link is clicked a notification modal will appear asking the admin user does she/he wants to delete a blog post. Once the delete button is clicked the blog post will be deleted from the site. 

**Actual Result:**
A delete link gets displayed when the user logins with the admin permission. When the delete link is clicked a notification modal appears asking the admin user does she/he wants to delete a blog post. Wheb the delete button is clicked the blog post is deleted from the site. 

**Pass/Fail:**
Pass

  <h2 align="center"><img src="readme-files/testing/test_18_a.jpg" alt="Test case 18" target="_blank" width="50%" height="50%"></h2>

  <h2 align="center"><img src="readme-files/testing/test_18_b.jpg" alt="Test case 18" target="_blank" width="60%" height="60%"></h2>

  <h2 align="center"><img src="readme-files/testing/test_18_c.jpg" alt="Test case 18" target="_blank" width="60%" height="60%"></h2>


# Code Validation

- The website was validated by the [W3C Markup Validation Service](https://validator.w3.org/) to ensure there were no syntax errors or issues. 
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) was used to validate CSS code.
- [JSHint](https://jshint.com/) was used for JavaScript code validation was used for validation of JavaScript.
- [PEP8 Online](http://pep8online.com/) was used for Python PEP8 compliance.

## [W3C Markup Validation Service](https://validator.w3.org/) - Markup Validation

### Home Page (`index.html`)
- There were several Duplicte ID errors and warnings which were fixed

<h2 align="center"><img src="readme-files/testing/validation_markup_home.jpg" alt="Markup Validation" target="_blank" width="60%" height="60%"></h2>

### Our Story Page (`our_story.html`)
- There are no errors

<h2 align="center"><img src="readme-files/testing/validation_markup_our_story.jpg" alt="Markup Validation" target="_blank" width="60%" height="60%"></h2>

### Our Team Page (`our_team.html`)

- There were several Duplicte ID errors and warnings which were fixed. Also, unecessary type attribute was removed for JavaScript resources. 

<h2 align="center"><img src="readme-files/testing/validation_markup_our_team.jpg" alt="Markup Validation" target="_blank" width="60%" height="60%"></h2>

### Products Page (`all_products.html`)

- There were several Duplicte ID errors and warnings which were fixed.

<h2 align="center"><img src="readme-files/testing/validation_markup_products.jpg" alt="Markup Validation" target="_blank" width="60%" height="60%"></h2>

### Product Detail Page (`product_detail.html`)

- There was an 'Unclosed element div' error on `row` element which was fixed.

<h2 align="center"><img src="readme-files/testing/validation_markup_product_detail.jpg" alt="Markup Validation" target="_blank" width="60%" height="60%"></h2>


### Basecamp Blog Page (`basecampblog.html`)

- There were several Duplicte ID errors and warnings which were fixed.

<h2 align="center"><img src="readme-files/testing/validation_markup_blog.jpg" alt="Markup Validation" target="_blank" width="60%" height="60%"></h2>

### Blog Post Page (`blog_post.html`)

- There are no errors
- There is one warrning which can be ignorred

<h2 align="center"><img src="readme-files/testing/validation_markup_blog_post.jpg" alt="Markup Validation" target="_blank" width="60%" height="60%"></h2>

### Contact Page (`contact.html`)
- There are no errors

<h2 align="center"><img src="readme-files/testing/validation_markup_contact.jpg" alt="Markup Validation" target="_blank" width="60%" height="60%"></h2>

### Log in Page (`login.html`)
- There are no errors

<h2 align="center"><img src="readme-files/testing/validation_markup_login.jpg" alt="Markup Validation" target="_blank" width="60%" height="60%"></h2>

### Register Page (`signup.html`)
- There are no errors

<h2 align="center"><img src="readme-files/testing/validation_markup_register.jpg" alt="Markup Validation" target="_blank" width="60%" height="60%"></h2>


## [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) - CSS Validation

### base.css

- There are no errors
- There are several warnings about the vendor prefixes which can be ignored

<h2 align="center"><img src="readme-files/testing/validation_base_css.jpg" alt="CSS Validation" target="_blank" width="60%" height="60%"></h2>

### blog.css

- There are no errors
- There are several warnings about the vendor prefixes which can be ignored

<h2 align="center"><img src="readme-files/testing/validation_blog_css.jpg" alt="CSS Validation" target="_blank" width="60%" height="60%"></h2>

### checkout.css

- There are no errors
- There are several warnings about the vendor prefixes which can be ignored

<h2 align="center"><img src="readme-files/testing/validation_checkout_css.jpg" alt="CSS Validation" target="_blank" width="60%" height="60%"></h2>

### products.css

- There are no errors
- There are several warnings about the vendor prefixes which can be ignored

<h2 align="center"><img src="readme-files/testing/validation_products_css.jpg" alt="CSS Validation" target="_blank" width="60%" height="60%"></h2>

### profile.css

- There are no errors
- There are several warnings about the vendor prefixes which can be ignored

<h2 align="center"><img src="readme-files/testing/validation_profile_css.jpg" alt="CSS Validation" target="_blank" width="60%" height="60%"></h2>


## [JSHint](https://jshint.com/) - JavaScript Validation

### script.js
- There are no errors
- There is one warning showing for a missing semicolon which doesn't make sense since the semicolon was added

<h2 align="center"><img src="readme-files/testing/validation_script_js.jpg" alt="JS validation for script.js file" target="_blank" width="60%" height="60%"></h2>

### team.js
- There are no errors
- There are no warnings

<h2 align="center"><img src="readme-files/testing/validation_team_js.jpg" alt="JS validation for team.js file" target="_blank" width="60%" height="60%"></h2>

### stripe_elements.js

- There are no errors
- There are no warnings

<h2 align="center"><img src="readme-files/testing/validation_stripe_elements_js.jpg" alt="JS validation for stripe_elements.js file" target="_blank" width="60%" height="60%"></h2>

### countryfield.js

- There are no errors
- There is one warning for unneccessary semicolon

<h2 align="center"><img src="readme-files/testing/validation_countryfield_js.jpg" alt="JS validation for countryfield.js file" target="_blank" width="60%" height="60%"></h2>

## [PEP8 Online](http://pep8online.com/) - Python PEP8 Compliant

All files were passed through the [PEP8](http://pep8online.com/) validator and the results were all found to be PEP8 Compliant


# Functionality Testing
A comprehensive testing was executed. Further elaborated in more details below:

- The website was physically tested on the following devices with different screen sizes:
  - iPhone 7 (Safari & Google Chrome)
  - iPhone 8 (Safari & Google Chrome)
  - iPhone 11 (Safari & Google Chrome)
  - Samsung GTI9505 Galaxy S4 (Chrome for Android)
  - Samsung Galaxy 9 (Chrome for Android & Samsung Internet)
  - Samsung Galaxy S20 (Chrome for Android & Samsung Internet)
  - Nokia Lumia 640 LTE (Windows 10) (Microsoft Edge)
  - HUAWEI P30 lite (Chrome for Android)
  - Samsung Galaxy Tab A (Chrome for Android & Samsung Internet)
  - Lenovo ThinkBook 13S (Chrome, Microsoft Edge & Firefox)
  - external monitor 31.5" PHILIPS 322E1C

The results were consistent, the website is platform-cross compatible and responsive. Furthermore, using DevTools I checked responsiveness for different screen sizes for mobile and tablet devices. Several issues were found and fixed all described under Encountered Issues section.

# Encountered Issues

Several bugs were encountered during the coding process:

- I had and issue to render static images in the browser on the production website. 

- **Fixed** by adding below code under the settings.py file under the templates section:
  ```
  'django.template.context_processors.static',
  ```

# Performance Testing

Performance was tested using [Lighthouse](https://developers.google.com/web/tools/lighthouse) tool.

## Desktop

