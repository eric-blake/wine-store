# Wine Store Testing

## Table of contents

  - [Manual Testing](#manual-testing)
    - [Navbar and Footer (base.html)](#navbar-and-footer-basehtml)
      - [Sidebar](#sidebar)
      - [Pagination](#pagination)
      - [Post Detail Page (User signed in)](#post-detail-page-user-signed-in)
      - [Post Detail Page (User signed out)](#post-detail-page-user-signed-out)
      - [Register Page](#register-page)
      - [Login Page](#login-page)
      - [Logout Page](#logout-page)
      - [Create Post Page](#create-post-page)
      - [Update Post Page](#update-post-page)
      - [Delete post Page](#delete-post-page)
    - [About page (User signed out)](#about-page-user-signed-out)
    - [About page (User signed in)](#about-page-user-signed-in)
    - [Admin panel](#admin-panel)
  - [Browser Testing](#browser-testing)
  - [Device Testing](#device-testing)
  - [Bugs](#bugs)

## Validator Testing
### validate

### HTML


### CSS


### JavaScript


### Python


### Lighthouse


## Manual Testing

<details>
  <summary>Click me</summary>

### Home page (index.html & base.html)
| Feature | Action| Expected Result | Actual Result | Pass/Fail |
|---------|--------|--------|--------|-----------|
| Logo      | Click on logo            | When user clicks on logo they should be redirected to home page   | User is redirected to the home page      |    Pass  |
| Home         | Click on home           | When user clicks on home they should be redirected to home page| User is redirected to the home page      |   Pass    |
| Register      | Click on register             | Register link available to all signed out users, when user clicks on register they should be redirected to register page      | User is redirected to the register page      |   Pass   |
| Login            | Click on login       | Login link available to all signed out users, when user clicks on login they should be redirected to login page       | User is redirected to the login page      |   Pass   |
| Product Management  | Click on Product Management| When user clicks on Product Management they should be redirected to Product Management page       | User is redirected to the Product Management page    |   Pass   |
| Search Bar | Type keywords and Click on search | When user searches for keywords the correct results are returned   | Correct seaarch results are returned      |    Pass  |
| Buy Wines dropdown  | Click on dropdown link | Each dropdown links to the correct products page   | User is redirected to the selected products page      |    Pass  |
| Champagne button  | Click on Champagne button  | When user clicks on Champagne button they should be redirected to Champagne products page   | User is redirected to the Champagne products page      |    Pass  |
| Wine Gifts dropdown  | Click on Wine Gifts dropdown link   | Each dropdown links to the correct products page   | User is redirected to the selected products page      |    Pass  |
| Shop Now button     | Click on Shop Now button              | When user clicks on Shop Now button they should be redirected to all products page   | User is redirected to to all products page      |    Pass  |
| Logout      | Click on logout              | Logout link available to all signed in users, when user clicks on logout they should be redirected to logout page      | User is redirected to the logout page      |   Pass   |
| Facebook link (icon)   | Click on Facebook icon   | Facebook icon available to all users, when user clicks on icon it opens Facebook in a new tab | User is redirected to Facebook website on a new tab  |   Pass   |
| Instagram link (icon)   | Click on Instagram icon | Instagram icon available to all users, when user clicks on icon it opens Instagram in a new tab   | User is redirected to Instagram website on a new tab  |   Pass   |
| Youtube link (icon) | Click on Youtube icon    | Youtube icon available to all users, when user clicks on icon it opens Youtube in a new tab  | User is redirected to Youtube website on a new tab  |   Pass   |
| Newsletter| Enter valid email address and click submit | Thank you for subscribing message appears   | As expected   |   Pass   |
| Hamburger menu | Open site on mobile device | Hamburger menu available to users on small screens   | Hamburger menu is present      |   Pass   |
| Hamburger menu | Toggle hamburger menu to open and closed| Hamburger menu can be toggled to open and closed position    | Hamburger menu is responsive      |   Pass   |
</details>

<details>
  <summary>Click me</summary>


### Products page (products.html)
| Feature | Action| Expected Result | Actual Result | Pass/Fail |
|---------|--------|--------|--------|-----------|
| Products per page on products page  |  Open products page and count products     |  There should be 8 products per page           |   There are 8 products per page     |      Pass     |
| Next button | Click on Next button | When user click on next button they are redirected to the next page| User is redirected to the next page      | Pass|     
| Previous button | Click on Previous button | When user click on previous button they are redirected to the previous page | User is redirected to the previous page      | Pass|     
</details>

<details>
  <summary>Click me</summary>

  
#### Product Detail Page (User signed in)
| Feature | Action| Expected Result | Actual Result | Pass/Fail |
|---------|--------|--------|--------|-----------|
| Product detail page  |   Click on product image    | When the user clicks on the product image, they should be redirected to the detailed view for the selected Product          |    As expected      |  Pass |
|    Product details   |   Click on a Product   |  All product details should be visible      |    All details are present   |     Pass      |
|    Add to favourites  |  Click on the heart icon  |   Ensure the page reloads, a flash message is displayed with confirmation and the icon changes to full heart   | As expected     |     Pass      |
|   Remove favourites  |  Click on the heart icon again  |   Ensure the page reloads, a flash message is displayed with confirmation and the icon changes to regular heart   | As expected     |     Pass      |


#### Product Detail Page (User signed out)
| Feature | Action| Expected Result | Actual Result | Pass/Fail |
|---------|--------|--------|--------|-----------|
|    Add to favourites button |  Click on the heart icon |    The page redirects to the login page   |  As expected    |     Pass      |
|    Add to bag button |  Click on the add to bag button |    When clicked the product is added to the shopping bag  |  As expected    |     Pass      |
|    Update quantity |  Click on the + and - buttons |    The quantity is incremented and decremented   |  As expected    |     Pass      |
|    Stock levels|  Select higher quantity than stock level and attenmp to add to bag |   When clicked error message is displayed not enough stock   |  As expected    |     Pass      |



#### Product Detail Page (Superuser)
| Feature | Action| Expected Result | Actual Result | Pass/Fail |
|---------|--------|--------|--------|-----------|
|    Edit product |  Click on the edit button |    The page redirects to the edit product page, the product details can be updated and the changes saved   |  As expected    |     Pass      |
|    Delete product |  Click on the delete button |    The page redirects to the edit product page   |  As expected    |     Pass      |
|    Edit review |  Click on the edit button |    The page redirects to the edit review page, the product review can be updated and the changes saved   |  As expected    |     Pass      |
|    Delete review |  Click on the delete button |    The review is deleted   |  As expected    |     Pass      |
</details>

<details>
  <summary>Click me</summary>


### Shopping Bag
| Feature | Action| Expected Result | Actual Result | Pass/Fail |
|---------|--------|--------|--------|-----------|
| Shopping bag     |  Add product to bag     |    Product appears in shopping bag correctly   |  As expected    |     Pass      |
| Update quantity |  Click on the + and - buttons |    The quantity is incremented and decremented   |  As expected    |     Pass      |
| Remove product   |  Click on the remove button   |  Product is removed from the shopping bag   |  As expected    |     Pass      |
| Add discount |  Add a valid dicount code   |  Docount is applied and grand total updated   |  As expected    |     Pass      |
| Add discount  |   Add an invalid dicount code    |  Error message appears and grand total is unchanged   |  As expected    |     Pass      |
| Remove discount  | Click on remove coupon    |  Discout is removed and grand total is updated   |  As expected    |     Pass      |

</details>

<details>
  <summary>Click me</summary>


### Checkout (User signed in)
| Feature | Action| Expected Result | Actual Result | Pass/Fail |
|---------|--------|--------|--------|-----------|
| Checkout button | Click on secure checkout button    |  The page redirects to the checkout page  |  As expected    |     Pass      |
| Adjust bag button  | Click on adjust bag   |  The page redirects to the shopping bag page   |  As expected    |     Pass      |
| Complete order   |   Click on complete order button  |  The purchase is successful. Order confirmation is displayed   |  As expected    |     Pass      |
| Verify order on stripe   | Go to stripe payments dashboard and verify order succeeded     |  Payment succeeded   |  As expected    |     Pass      |
| Save delivery information   |   Select save this delivery information to profile when placing order |  Delivery information is saved to profile   |  As expected    |     Pass      |


### Checkout (User signed out)
| Feature | Action| Expected Result | Actual Result | Pass/Fail |
|---------|--------|--------|--------|-----------|
|   Delivery information   |  Place order   |  Delivery information not saved   |  As expected    |     Pass      |
</details>

<details>
  <summary>Click me</summary>


### My Profile Page 
| Feature | Action| Expected Result | Actual Result | Pass/Fail |
|---------|--------|--------|--------|-----------|
|    Profile |   Fill in the form and click update  |  Profile is updatd  |  As expected    |     Pass      |
|    Order history | Go to My profile   | A list of all previous orders is visible   |  As expected    |     Pass      |
| Order history details    |  Click on the order number   |  The order details page is displayed   |  As expected    |     Pass      |
</details>

<details>
  <summary>Click me</summary>


### Favourites Page 
| Feature | Action| Expected Result | Actual Result | Pass/Fail |
|---------|--------|--------|--------|-----------|
| Favourites page   |  Go to my favourites page   |   List of favourite products are visible  |  As expected    |     Pass      |
</details>

<details>
  <summary>Click me</summary>