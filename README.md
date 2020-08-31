# Django Milestone Project 4

[![Build Status](https://travis-ci.org/amosborn/django-msproject.svg?branch=master)](https://travis-ci.org/amosborn/django-msproject)

This e-commerce website is created for the Code Institute Milestone 4 project, using Django 1.11.
The site is for an art gallery which sells works of art as well as periodically holding auctions.
When testing this app, the following details can be used:


## User Experience (UX)
The site is designed for people who love art and are looking for somewhere to purchase a piece.
It provides a place for the gallery to display the works the have for sale and gives the user the opportunity to purchase or join in an auction and bid on original pieces.

### User Stories

### Customer:
* As a customer I want to be able to access the website on all devices.
* As a customer I want to read details about the business and how to contact them.
* As a user I want to view the products on sale.
* As a user I want to view the auction lots on sale.
* As a user I want to be able view details of the auction.
* As a user I want to be able to add products to my shopping cart.
* As a user I want to be able to update quantites or delete products from my cart.
* As a user I want to be able to search the products or auction lots. 
* As a user I want to register and create an account.
* As a registered user I want to save and update my delivery details for future purchases.
* As a registered user I want to be able to bid on current auction lots.
* As a registered user I want to be able to checkout securely for products and auctions.

### Business owner:
* As the business owner I want to be able to add, edit and delete products in the database.
* As the business owner I want to add auction lots to the database and run the auction.

## Design
The design is simple so as not to distract from the images of art on display.

### Fonts
* Google Fonts Robot and Raleway 

### Colour scheme
* The blues and purple are a neutral background for displaying the product images.
* The black navbar adds sophistication for a business like an art gallery.

### Icons
* FontAwesome icons used for social media links and for visual clues on buttons.

### Wireframes

## Features

### Existing Features

#### Navbar

* Logo on top left links to home page
* Navbar collapses on small screens
* Navbar links register or login if customer not logged in
* Navbar links profile and logout if customer is logged in
* Shopping cart icon showing number of products in cart

#### Footer

* Social media links, open in new window

#### Home Page

* Background image of the business
* Heading and short welcome message
* Links to auction or shop

#### About Page

* Address and contact details
* Google map of location

#### Current Auction

* List of current auction lots
* Button to click to view auction details
* Auction detail page with link to bid if logged in
* If user not logged in, Login button displayed

#### Shop

* List of products on sale
* Each has form to select quantity and button to add to cart

#### Cart

* List of all items and quantities in cart
* Form to adjust quantity of a product
* Total cost of order displayed at the bottom with checkout button

#### Checkout

* Contains forms for delivery details and payment details of user
* Total cost of order is displayed
* Stripe processes secure checkout

#### Register and Login

* Form for new users to register
* Form for existing users to login

#### Profile

* Displays current auctions with button back to bid form to increase bid
* Dispalys auctions won with checkout button if not yet paid
* Profile form for saving user delivery details

### Future Features

* Complete the bid functionality, to allow bids to be saved to the database
* Allow registered users to leave reviews
* Allow user to delete account if no outstanding auction to pay or current bids
* Profile to show users order summaries and bid history
* Email bidders if they have been outbid
* Pagination for larger number of products and lots
* Customise error pages
* Improve message feedback to user

## Technologies

### Languages
* HTML5
* CSS3
* JavaScript
* Python
* Jinja templating language

### Frameworks
* Django1.11.29
* Bootstrap 4
* FontAwesome
* Jquery
* Google Fonts

### Tools
* Gitpod - code editor
* Git - for version control
* Github - repository
* Travis - integrated testing
* Heroku - for hosting application
* AWS S3 - to store static files and media
* Boto3 - for AWS services
* Stripe - for processing payments
* SQlite3 - development database
* PostgreSQl - production database

## Testing

During development I used Chrome Developer Tools to check how the app appeared on different devices.
Debug wasset to True in Django, so I could use the errror messages to find problems with the code.
The app was tested on different browsers: Chrome, Edge and Firefox.

### Manual Testing

#### Navbar
* Each navbar link opens the correct page
* Logo opens the home page
* The navbar collapses on smaller devices
* Each link in the collapsed navbar return the correct page Tools

#### Footer
* Social media icons open correct websites

#### Home page
* Links to auction and shop return the right pages
* Check responsiveness on different device sizes

#### About page
* Goole Map loads correctly

#### Currect auction
* All lots in current auction display
* Button to lot detail opens the right page
* Search bar returns auction results for current auction

#### Lot detail page
* Creates and displays the right auction
* Repsonsive on different screen sizes
* Button to bid displays to logged in users only
* Bid button links to bid with the right auction

#### Past auctions
* All expired auctions displayed with correct details

#### Shop page
* Displays list of all products for sale
* Form only takes numbers 1-5 and gives error message if number or letter not within range
* Add button places the correct quantity of chosen product in cart
* Search bar return results from product list

#### Cart
* Number of products in cart is displayed on navbar link
* Correct number of products in cart
* Correct total of product number x quantity
* Form only accepts numbers 1-5 and gives error message for letter or number not within the range
* Product quantity changed to 0 and item is removed from cart
* Checkout button links to checkout page if user logged in
* Checkout button redirects to login page if user not logged in

#### Checkout page
* Checkout page displays correct order total
* Delivery information fields are pre-populated if user has created a profile
* If required delivery form fields are left blank, error message displayed
* Test payment using Stripe test details:
  - card number: 4242424242424242
  - cvv: any 3 digits
  - expiry month and year: any future month and year
* Invalid or missing card number or past date returns error message
* Checkout success message

#### Profile
* Navbar option for users who have registered and are logged in
* Form to store delivery details is prepopulated once created, and can be edited and saved
* Auctions bid on are displayed with button to increase bid
* Auctions won are displayed with checkout button if not yet paid for

#### Registration page
* Registration form for valid email and username and password

#### Login page
* Form to login with username or email and password
* Link to reset password if user has forgotten item

### Validation

* W3C HTML valdator
* W3C CSS validator
* PEP8 online

### Errors and bugs

* Import env in settings.py is unused and fails Travis integrated testing. However when I remove it the app won't run, with SECRET_KEY error in settings.py, which is fixed by reinstating import env.
* Some Python lines of code too long, but unsure how to split them to the next line.  

## Deployment

This project was created using the GitPod IDE for development and GitHub repository to store the code.

### Run this project locally
* Using GitPod IDE

The following must be installed:
* PIP3
* Python
* Git
Free accounts to be created with:
* Stripe
* AWS 3

Instructions:
1. Clone the repository with the following command in your IDE terminal
    git clone https://github.com/amosborn/django-msproject
2.  Set up virtual environment with the command
    python3 -m venv environment
3. Activate the environment
4. Install the required packages with
    pip3 install -r requirements.txt
5. Create env.py files and add it to .gitignore file
6. Set environment variables in env.py
    import os
    os.environ["SECRET_KEY", "yoursecretkey"]
    os.environ["STRIPE_SECRET_KEY", "stripesecretkey"]
    os.environ["STRIPE_PUBLISHABLE", "stripepublishablekey"]
    os.environ["DATABASE_URL", "postgresdatabaseurl"]
    os.environ["AWS_ACCESS_KEY_ID", "awsaccesskeyid"]
    os.environ["AWS_SECRET_ACCESS_KEY", "awssecretaccesskey"]
7. Set up database with command
    python3 manage.py migrate
8. Create a superuser for access to the admin panel and follow instructions after the command
    python3 manage.py createsuperuser
9. To run the application use
    python3 manage.py runserver

### Deploy to Heroku 

1. Create a requirements.txt file with the command 
    pip freeze > requirements.txt
2. Create a Procfile with the command 
    echo web: gunicorn django-msproject.wsgi:application > Procfile
3. Git add, git commit and git push the Procfile to 
4. Create a new app in Heroku
5. In Add-ons find Postgres and click Provision to provision the database
6. In settings add environment variables from env.py to Heroku
7. Set up new database with command
    python3 manage.py migrate
8. Create superuser with the command
    python3 manage.py createsuperuser
9. Click Deploy on the Heroku dashboard to deploy the project.

## Credits

* Development was based on the Code Institue course lesson videos.
* Slack was very useful as other students has usually had the same queries as I did.
* Django documentation was also used
* StackOverflow was very helpful for finding solutions
* The images are all copyright free from Unsplash.com
* The names and titles were from namegenerator.org.uk and artsnova.com
* The countdown and search bar were copied from W3Schools examples
