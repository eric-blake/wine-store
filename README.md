# Project name -PP5

## Purpose of this site

Wine Store is a B2C e-commerce application that allows users to purchase wines

### Screenshot of Wine store

-By Eric Blake
# [Live site](https://wine-store-ci-bbef57464b33.herokuapp.com/ "Live site")

## Table of contents

- [Live site](#live-site)
  - [Table of contents](#table-of-contents)


# UX

## Targeted Users

- A user that wants to view and buy wine
- A user that wants to buy wine at a discount

### Site Goals

- To provide users with the ability to search products quickly and easily.
- To provide users with the ability to see the most popular products.
- To provide users with the ability to save products to their favourites list
- To provide users with the ability to see their order history
- To provide users with the ability to edit their saved address for quicker purchasing.
- To provide users with the ability to see the most popular products.

### Project Goals

- Create a fully functional e-commerce application that looks and feels like a professionally designed online store. The website will be responsive and user-friendly, providing the user with the ability to:
 - Register and Login
 - Reset Password
 - Update personal information
 - Browse, search and refine products for sale
 - View product stock levels
 - Add products to shopping cart
 - Apply discount codes
 - Update quantity in shopping cart
 - Delete items from shopping cart
 - Pay for items securely by using the integrated Stripe payment system
 - Save products to favourites list
 - View previous orders

### Agile Development Tool

I utilized a GitHub project and a Kanban board. [Kanban board](https://github.com/users/eric-blake/projects/14)
As I start working on each issue I move it to the 'In progress' column.  When the coding for each issue has been completed, the issue is then moved to the 'done' column.


### User Stories
I used Github Issues to record the following user stories:
1.	As a Site User I can visit the home page so that I can easily identify the purpose of the website
2.	As a Site User I can visit the home page so that I can easily identify the purpose of the website
3.	As a Site User I can view a list of all products so that so that I can choose products to purchase
4.	As a Site User I can view detailed information about a single product so that so that I can make an informed decision before purchasing
5.	As a Site User I can refine the list of all products so that I can easily find wines that match my interests
6.	As a Site User I can search for products in the shop by entering keyword so that I can quickly find products that are of interest to me
7.	As a Site User I can register for an account so that so that I can have access to all functionality
8.	As a Site User I can log in to my account so that view my account details and make purchases
9.	As a Site User I can reset my password so that I can access my account in case I forget my password
10.	As a Site User I can logout of my account so that I can keep my account and personal details secure
11.	As a Site User I can see my profile so that I can update my personal information
12.	As a Site User I can add products to my shopping cart so that I can conveniently purchase multiple items at once
13.	As a Site User I can remove products from my shopping cart so that I can adjust my order before making a purchase
14.	As a Site User I can adjust the quantity of products in my shopping so that I can control the quantity for each item I want to purchase
15.	As a Site User I can apply discount codes to my order so that I can receive savings and discounts on my purchase
16.	As a Superuser/Administrator I can add new products to the website so that I can expand the product portfolio
17.	As a Superuser/Administrator I can edit existing products on the website so that so that I can update and manage the product catalogue
18.	As a Superuser/Administrator I can delete existing products on the website so that so that I can update and manage the product catalogue
19.	As a Site User I can easily sort products by price, date and alphabetically so that I can find products that interest me
20.	As a Site User I can complete the checkout step so that I can purchase the products added to my bag
21.	As a Site User I can conveniently pay for my order so that I can complete the transaction quickly
22.	As a Site USer I can sign up for newsletters on the website so that I can keep update with the latest news and offers
23.	As a Site User I can easily find contact details and social media links so that I can contact the shop
24.	As a Site User I can easily find contact details and social media links so that I can contact the shop
25.	As a Site User I can see a custom error message so that I know why I cant access a page
26.	As a site developer I can create a Robots.txt and Sitemap.xml file so that I improve my SEO
27.	As a site developer I can connect external database storage and hosting services so that the site data is stored successfully
28.	As a Site User I can select products to add to my favourites list so that I can easily find them in future
29.	As a Site User I can leave product reviews so that I can share my feedback with the site owner and other potential buyers

All User Stories include:
* Acceptance Criteria
* Tasks
* Labels (MoSCoW Priotarization)


### Structure & Logical Flow

The database model diagram was designed using Lucid Charts
![Screenshot of flowchart](\documentation\images\features\ERD.PNG)

**Product Model**
The main model that contains all the fields needed for the products. This model is based on the "Boutique Ado" walkthrough project. Some adjustments and additions were made to fit the needs of my project. 
  Colour,Closure,Style and Grape were added.

**User Model**
This is the Django Allauth standard user model. It is connceted to the userprofile model with a one to one relationship.

**UserProfile Model**
This is a custom model to provide the user with a place to save delivery information and a record of their order history. It is connceted to the user model with a one to one relationship.

**Favourites**
This model stores products to an authenticated users favourites list. It is connected to the user and producd tables with a ForeginKey.

**Reviews**
This stores an authenticated users product reviews. It is connected to the user and product tables with a ForeginKey.

**Coupon Code**
This model allows admin to create discount codes to offer to customers. 

**Order**
This model stores all the users order details. it is connected to the userprofile table with a ForeginKey.

**Order Line Item**
This is craeted for each line item in the order. It is connected to the order and product tables with a ForeignKey.


### Wireframe

I used Mockflow to create the following wireframes for both desktop and mobile devices.

Page | Wireframe Desktop  | Wireframe Mobile
--- | --- | --- 
Home page | ![Home page image](/documentation/images/wireframes/home-page.PNG) |![Home page image](/documentation/images/wireframes/home-page-mobile.PNG)
Product Detail page | ![Post detail page image](/documentation/images/wireframes/product-detail-page.PNG) |![Post detail page image](/documentation/images/wireframes/product-detail-page-mobile.PNG)


### Colour Scheme
* The main colour used for the banner and buttons is #91033c.
* The background colour in the header and footer is #303C42.


### Fonts
In addition to Bootstrap 4 built in font family the below two fonts were used throughout the application
* Lato and Karla: These are sans-serif fonts that are part of the Google font collection. They are professional and very readable fonts.

## Features

### Existing Features

### Home Page
**Hero Section**
The home page features a hero image that shows the user what the site is about.
There is a "Shop Now" button on the home page to enable the user to start shopping immediately.
![home page](/documentation/images/features/home-page.PNG)


**Toasts**
Toasts from Bootstrap were implemented to provide users with feedback regarding their actions on the website.
![products](/documentation/images/features/toast-message.PNG)


**Latest Products**
The products displayed on the home page are the eight most recently added products. 
![products](/documentation/images/features/latest-products.PNG)


**Newsletter**
The users can sign up to a newsletter to recieve the most recent offers and discount codes. The form was integrated using MailChimp.
![newsletter](/documentation/images/features/newsletter.PNG)


**Banner**
The banner contains delivery information and current offers
![banner](/documentation/images/features/banner.PNG)

**Navbar**
* The navbar was built using bootstrap 4 and it is fully responsive.  The name of the website and logo is on the left hand side. The search bar allows the users to search for products by keywords from any page of the website. The My Account drop down gives the user the option to log in or sign up. If the user is a superuser/admin the Product Management drop down will allow the user to add new products. If the user is authenticated a favourites icon will link to the favourites page.The shopping bag icon is a link to the shopping bag and it also displays the total of the items in the bag. 
* The bottom nav has a link to the home page. The Buy Wines dropdown allows users to refine the product list by type, country, style and grape. The Champagne and Wine Gifts links allows the user to refine the list by these categories.

![Navbar](/documentation/images/features/nav.PNG)

![Mobile Navbar](/documentation/images/features/navbar-mobile.PNG)

![Mobile Navbar dropdown](/documentation/images/features/navbar-mobile-dropdown.PNG)


**Footer**
* The footer is simple layout with displaying social media options.  When an icon is clicked, it opens in a new tab so that the user still has the main site open.

![Footer](/documentation/images/features/footer.PNG)


**Register**

*  The form enables users to register for an account.

![Register](/documentation/images/features/register.PNG)


**Sign-in** 
* The form enables users to sign-in to their account.
  
![Sign-in](/documentation/images/features/sign-in.PNG)

**Sign-out**

* The form enables users to sign-out of their account.

![Sign-out](/documentation/images/features/sign-out.PNG)


**Products Page**
The all products page renders all products to the user. They have the option to sort the products by title, price, alphabetically and year. This page also displays the number of the products available. 
At the end of the products page there is pagination to help the user navigate easily through multiple pages of products.
![All products page image](/documentation/images/features/all-products.PNG)

**Product Detail Page**
The product image is displayed on the left side. The product details is on the right side. This includes the product title, description and price.
![Product details page image](/documentation/images/features/product-detail.PNG)


**Reviews**
- The product review page allows authenticated users to leave a review.
- The user can edit and delete their own reviews
![Product Reviews page image](/documentation/images/features/reviews.PNG)


**Profile**
- The profile page renders a form for the user's address and phone number. If the user has any details saved, it renders prefilled.
- The users order history is displayed.
![profile page image](/documentation/images/features/my-profile.PNG)


**Favourites Page**
This favourites page allows users to have a list of all the products they have added to their favourites page, by clicking the heart icon on each product.

![Favourites page image](/documentation/images/features/favourites.PNG)


**Shopping Bag Page**
The shopping bag page can be accessed from the nav menu. 
![Bag Image](/documentation/images/features/shopping-bag.PNG)
- The bag page shows the products a user has in their bag.
- This page allows for updating quantities, deleting products from their bag and viewing details of each product.
- The subtotals are calculated automatically.


**Stock Levels**
- Stock quantitities have been implemented into the product model. When a user adds an item or updates the quantity in the shopping bag, the add-to-bag function checks the quantity selected plus the quantity of that item in the bag and compares it to the stock levels of the product. The user cannot add to bag more items than there is in stock. 
- In the event that 2 orders for the same items go through at the same time and there is insufficient stock to fulfill both orders, the admin can cancel the status of the order and contact the customer for a refund. 
![Stock error image](/documentation/images/features/stock-error.PNG)


**Coupon Codes**
The coupon code form is on the shopping bag page. When a user enters a valid coupon code the discount is applied to the grand total. The coupon can be removed by clicking the Remove Coupon button.
![coupon code applied image](/documentation/images/features/coupon-code.PNG)

![coupon code applied image](/documentation/images/features/coupon-applied.PNG)


**Checkout Page**
- The checkout page shows the user's delivery and payment information and a summary of the user's order. if the user is logged in they can check the box to save their details for future transactions.
- Users must enter their payment information before completing the checkout and all payments are handled via Stripe.
![Checkout page Image](/documentation/images/features/checkout.PNG)


**Order Confirmation Page**
- On successful checkout, an order summary page is shown. This will include the discount if a coupon was used.
![Order summary page Image](/documentation/images/features/order-confirmation.PNG)


**Order Confirmation Email**
- On successful checkout, an order summary page is shown. This will include the discount if a coupon was used.
![Order summary page Image](/documentation/images/features/order-confirmation.PNG)


**Add products**
- This page shows the product creation form and all required fields and allows the admin to add an item to the database. 
![Add Product Image](/documentation/images/features/add-product.PNG)


**Edit products**
- The edit product page shows the product form prefilled with the existing data in the database. It allows the admin to modify all details about the products.
![Edit Product Image](/documentation/images/features/edit-product.PNG)


**Delete products**
- This allows the admin to delete a product. 
- A confirmation modal appears when the user clicks on delete. The user clicks on Confirm Delete to permanently delete the product.
![Delete Product Image](/documentation/images/features/delete-product.PNG)


**Admin Page**
* An admin area only allowing access to the site admin/superuser.
* The admin page is only accessible by typing "admin" in the url <https://wine-store-ci-bbef57464b33.herokuapp.com/admin/>.
* User name and password must be entered to access the admin page.
* The administrator can manage products, users, orders and coupons.
![Admin page Image](/documentation/images/features/admin.PNG)


### Future Features
* Send email to customers when their order changes status.
* Coupon management on product management page for superusers/admin
* Social media login.
* FAQ page, About page, Terms and conditions and privacy staement.


## Search Engine Optimization SEO and Marketing

### Business Model
This website follows a Business to Customer model - it sells wine products directly to the customer. The website has been built for quick checkout for both registered and unregistered users, with extra features available to users who have signed up to the website.

### SEO
- A sitemap was generated using [xml-sitemaps](https://www.xml-sitemaps.com/) This was generated using the deployed website. 
![Sitemap](/)
- Robots.txt file was created at the root level of the project. This file tells the search engine crawlers which URL's they can access on the website.
![Robots.txt file](/)

### Marketing
- The website has an embedded [Mailchimp](https://mailchimp.com/?currency=EUR) newsletter in the footer. This section facilitates user engagement and promotes the e-commerce store through effective email marketing.
![Newsletter](documentation\images\features\newsletter.PNG)

- A Facebook Business Page was created. The main goal of this Facebook page would be to showcase new deals on products, give coupon code discounts to followers, and have targeted ads for different times of the year - "Christmas Sale", "Valentines Specials"   etc.
![Facebook Business Page](/documentation/images/features/facebook-page.PNG)


## Technologies Used

### Coding languages used

* HTML
* CSS
* Python
* JavaScript

### Frameworks and Libraries used

**Django**
* Framework used to build this project. Provides a built in admin panel and includes many helper template tags that make writing code quick and efficient.

**Django-Allauth**
* Used for User authenticaion (register, login and logout).

**Django Crispy Forms**
* Used to control rendering of Django forms.

**ElepantSQL**
* The database used by the deployed project on Heroku.
  
**psycopg2**
* PostgreSQL database adapter for the Python programming language.

**Gunicorn**
* Python HTTP server for WSGI applications.

**Summernote**
* WYSIWYG editor. Used for comment form.

**Cloudinary**
* The cloud platform used to store static media files.

**Mockflow**
* Used for the wireframes

**Git**
* Used for version control.

**CodeAnywhere**
* Used as the IDE to code this website.

**Heroku**
* The cloud platform used to deploy the project in the live environment.

**Bootstrap**
* The front end development framework used for styling along with custom CSS.
  
**Pillow**

### Programs
- [W3C HTML Validator](https://validator.w3.org/) was used to check for errors in the HTML code.
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to check for errors in the CSS code
- [Js Hint](https://jshint.com/) was used to validate the JavaScript code.
- [CI Python Linter](https://pep8ci.herokuapp.com/) was used to validate the Python code.


## Testing

Detailed testing of the site can be found at [TESTING.md](TESTING.md)

Testing includes the following:

* Validator testing
* Responsivness & Browser Compability Testing
* Manual testing
* Browser testing
* Device testing
* Bugs


## Deployment and local development

### Deployment

The following steps were taken to deploy this website to Heroku 

1. Elephant SQL database:
    - Open [ElephantSQL](https://www.elephantsql.com/) and sign-up for a free account
    - Click on 'Create New Instance'
    - Enter a database name for the project and select Tiny Turtle (Free plan), click on continue
    - Select your region, click on 'Review' and 'Create instance'
    - Click on your instance in the list to open it
    - Copy database URL in the URL field
  
2. Heroku App:
    - Select 'Create new app' in Heroku
    - Enter an App name and select the location
    - Select 'Settings' in the menubar. Click 'Reveal Config Vars' and add the following:
      - DATABASE_URL: the DATABASE_URL copied from ElephantSQL
      - SECRET_KEY: The SECRET_KEY string you created
      - PORT: 8000
    - Click 'Deploy' and then 'GitHub' under 'Deployment method'
    - Select the repository you want to deploy and click 'Connect'
    - Scroll down and click 'Deploy Branch' to complete the process

3. Prepare the environment and settings.py file:
   - In the settings.py file within the django app, import Path from pathlib, import os and import dj_database_url
   - Insert the line if os.path.isfile("env.py"): import env
   - Remove the insecure secret key that django has in the settings file by default and replace it with SECRET_KEY = os.environ.get('SECRET_KEY')
   - Replace the databases section with DATABASES = { 'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))} ensure the correct indentation for python is used.
   - Save all files and make migrations - python3 manage.py migrate

5. Deploy 
   - In Heroku, navigate to the deployment tab and deploy the branch manually - watch the build logs for any errors.
   - Heroku will now build the app.  Once it has completed the build process you will see a 'Your App Was Successfully Deployed' message and a link to the app to visit the live site.


### AWS setup
- Log in to [AWS](https://aws.amazon.com/)
1. Create a new S3 bucket:
- Choose the closest AWS region.
- Add unique bucket name.
- Under Object Ownership select ACLs enabled to allow access to the objects in the bucket.
- Under Block Public Access settings unselect block all public access as the application will need access to the objects in the bucket.
- Click on create bucket.
2. Edit bucket settings.
- Bucket properties
  - Open the bucket page.
  - Go to properties tab and scroll down to website hosting and click on edit.
  - Enable static website hosting
  - Under the Hosting type section ensure Host a static website is selected.
  - Add Index.html to index document field and error.html to error document field and click save.
- Bucket permissions
    - Navigate and Click on the "Permissions" tab.
    - Scroll down to the "CORS configuration" section and click edit.
    - Enter the following snippet into the text box and click on save changes.

    ```
    [
    {
        "AllowedHeaders": [
            "Authorization"
        ],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    }
    ]
    ```
    - Scroll to bucket policy section and click edit. Take note of the bucket arn (Example: arn:aws:s3:::test-bucket)
    - Click on policy generator and set the following settings:

        1. Select Type of Policy - S3 Bucket Policy
        2. Effect Allow
        3. Principal *
        4. AWS Service Amazon S3
        5. Actions: GetObject
        6. Amazon arn: your arn from the previous page

    - Click on add statement and then generate policy.Copy the policy
    - Paste the policy into the bucket policy editor.
    - Add "/*" to the end of the resource key to allow access to all resources in this bucket.
    - Navigate and Click Save changes.
    - For the Access control list (ACL) section, click edit and enable List for Everyone (public access) and accept the warning box. If the edit button is disabled, you need to change the Object Ownership section above to ACLs enabled (refer to Create Bucket section above).

3. Identify and Access Management (IAM)
- Create User group
    - In the search bar, search for IAM. 
    - On the IAM page select user groups in the menu on the left.
    - Click on create user group, add a name and click create group. The users and permission policies will be added later.
- Create Permissions policy for the user group
    - Go to Policies in the left-hand menu and click create policy
    - Click on actions and import policy.
    - Search for "AmazonS3FullAccess", select this policy, and click "Import".
    - Click "JSON" under "Policy Document" to see the imported policy
    - Copy the bucket ARN from the bucket policy page and paste it into the "Resource" section of the JSON snippet. Be sure to remove the default value of the resource key ("*") and replace it with the bucket ARN.
    Copy the bucket ARN a second time into the "Resource" section of the JSON snippet. This time, add "/*" to the end of the ARN to allow access to all resources in this bucket.

    ``````
        {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "s3:*",
                    "s3-object-lambda:*"
                ],
                "Resource": [
                    "arn:aws:s3:::your-project",
                    "arn:aws:s3:::your-project/*"
                ]
            }
        ]
    }

    ``````


    - On the next page add polcity name and description and click create policy.

- Attach Policy to User Group
    - Click on User Groups in the left-hand menu.
    - Click on the user group name created during the above step and select the permissions tab.
    - Click Attach Policy.
    - Search for the policy created during the above step, select it and click attach policy.

- Create User
    - Click on Users in the left-hand menu and click on add user.
    - Enter a User name .
    - Select Programmatic access and AWS Management Console access and click next.
    - Click on add user to group, select the user group created earlier and click create user.
    - Take note of the Access key ID and Secret access key as these will be needed to connect to the S3 bucket.
    - To save a copy of the credentials click Download .csv


### Cloning the repository

The repository was cloned to my local PC. The steps to clone are as follows.

* In the Github repository, navigate to the main page of the repository.
* Click on the green Code button and copy the URL.
* Select Clone by HTTPS option.
* Open the code editor and within the terminal change the directory to the location you want to clone the repository to.
* Type git clone and paste the URL copied earlier.
* Press enter to create the local clone.


### Forking the Repository
By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log into [GitHub](https://github.com/login) or [create an account](https://github.com/join).
2. Locate the [GitHub Repository](https://github.com/eric-blake/Wild-Atlantic-Way-Blog).
3. At the top of the repository, on the right side of the page, select "Fork"
4. You should now have a copy of the original repository in your GitHub account.


## Credits
* Instructions throughout project was taken from [Code Institute](https://codeinstitute.net/ie/ "Code Institute") Boutique Ado walkthrough project.
* Django Documentation
* Responsive dropdown submenu - https://codepen.io/surjithctly/pen/PJqKzQ
* Creating a coupon system - https://www.youtube.com/watch?v=_dSCGMJcoe4
* Wine dataset from [Kaggle](https://kaggle.com/ "Kaggle"),
* Pictures are from [Pixabay](https://pixabay.com/ "Pixabay"), and [Pexals](https://pexals.com/ "Pexals"),
* Logo image https://www.pngegg.com/
* The Favicon was taken from [Icons8](https://icons8.com/ "Icons8") and [Favicon converter ](https://favicon.io/favicon-converter/ "Favicon converter") 

Stack overflow
How to limit vintage field to maximuum of 4 digits https://stackoverflow.com/questions/2470760/charfield-with-fixed-length-how
