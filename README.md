# Craigslist Clone w/ API

### [Live Demo](https://cl-dhcrain.herokuapp.com/)  
### [API Documentation](https://cl-dhcrain.herokuapp.com/api/docs/)

Create a Craigslist clone from front to back.

__Learning Objectives__

- Plan a full scale project
- Translate high level feature requests into code
- Image upload and display
- Front end layout

## Features
- Login/Registration/My Account
- City selection page
- Ability to store a city preference on user profile
- Category and subcategory features
- Main page index (listing categories and sub categories)
- Implement a Search feature
- Posting a new classified
- Posting list for any given subcategory. Must include 3 different data views:
    - List
    - thumb
    - gallery
- Posting detail page. Should include:
    - Images
    - Navigation
- Sorting:
    - Newest
    - High Price
    - Low Price

## REST API features
__Learning Objectives__

Adapt an existing large project to include API endpoints that mimic existing functionality and constraints

__Base URL:__ `https://cl-dhcrain.herokuapp.com/api/`

- Retrieve a list and detail of existing Categories  
    - `/categories/`  
    - `/categories/:id/`
- Retrieve a list and detail of existing Sub-Categories  
    - `/sub_categories/`  
    - `/sub_categories/:id/`
- Retrieve a list and detail of existing Posts by Sub-category & by Category
    - `/category_listings/:id/`
    - `/sub_category_listings/:id/`
- Allow a user to create new categories and sub-categories through the API - but ONLY if they have is_superuser flag on their account.
- Retrieve a detail of a single post.
    - `/listings/:id/`
- Create a new Listing with all Foreign Key fields satisfied
    - `/listings/`
- Update an existing post. Include being able to change the Sub-Category the post belongs to.
- Allow a user to create an account through the API and return the user their API Access Token
    - `/register/`
    - `/api-token-auth/`
- A non logged in user can NEVER create or update ANY records.
- A logged in user can NEVER update a record created by another user.
- Use Basic or Token authentication to allow a user to authenticate.
