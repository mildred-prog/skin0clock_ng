# Testing

Testing file for skin0clock_ng [README.md](README.md).

## Testing User Stories

### Developer Stories

- [x] Frontend & Backend of the project created.
- [x] Database is connected to the project.
- [x] App deployed on Heroku.

### User Stories

- [x] Register an account
- [x] Login & logout of account
- [x] Manage user accounts
- [x] View all skincare products
- [x] View products details individually
- [x] Add featured items
- [x] Persistent access to shopping basket
- [x] Update items in cart
- [x] Integrate stripe for payment
- [x] Order summary display
- [x] Order management
- [x] Writing a review
- [ ] Add items to wishlist
- [ ] Faq for questions and informative answers
- [ ] Subscribe to newsletter
- [x] Social media profile
- [x] Optimize with Google SEO


## Validation

### Validation Errors

| **HTML Validation Issue** | **Description** |
|:---------------------------|:----------------|
| Duplicate attribute `rel` on `<link>` tags | Multiple `rel` attributes found on the same `<link>` element |
| Missing `type="button"` on non-form `<button>` | Buttons not inside forms should explicitly declare `type="button"` |
| Using `<div>` directly inside a `<ul>` | Invalid HTML structure; `<ul>` should only contain `<li>` elements |
| Button missing `type="submit"` | Form submit buttons missing an explicit `type="submit"` attribute |
| Empty `<a href="">` if no image exists | Empty anchor tags if an image is missing from inside the link |
| `<p>` inside `<strong>` not valid | Block-level `<p>` tags incorrectly placed inside inline `<strong>` tags |
| No `alt` fallback if `product.image` is missing | Missing descriptive text for images when `product.image` is not available |
| Empty `<div class="row mt-1 mb-2"></div>` | Empty `<div>` without meaningful content |
| Missing closing `</div>` for button container | Unclosed `<div>` leading to HTML structure errors |
| No `<label>` explicitly for form fields | Form inputs missing associated `<label>` elements |
| Empty `<br>` tag inside `<p>` | Improper use of empty `<br>` tag within a paragraph |
| Misplaced closing `</div>` | Closing a `</div>` tag at the wrong location, breaking layout |
| Trailing slash on void elements | Unnecessary trailing `/` on self-closing tags in HTML5 |
| No `<p>` element in scope but a `</p>` end tag | `</p>` tag used without an open `<p>` tag |
| Stray end tag `</div>` | Extra or misplaced `</div>` without a matching open tag |

### HTML Validation Corrected
Testing using the recommended [HTML W3C Validator](https://validator.w3.org/) to validate all of my HTML files.
- [x] HTML validation all passed:

**Home page**  
![Home Page HTML Validation](static/documentation/testing/html-home.jpg)

**Signup Page**  
![Signup Page HTML Validation](static/documentation/testing/html-signup.jpg)

**Login Page**  
![Login Page HTML Validation](static/documentation/testing/html-login.jpg)

**Logout Page**  
![Logout Page HTML Validation](static/documentation/testing/html-signout.jpg)

**Products Page**  
![Products Page Page HTML Validation](static/documentation/testing/html-products.jpg)

**Product Detail Page**  
![Product Detail Page HTML Validation](static/documentation/testing/html-product-detail.jpg)

**Categories Page**  
![Add Product Page HTML Validation](static/documentation/testing/html-categories.jpg)

**Wishlist Page**  
![Grow Guide HTML Validation](static/documentation/testing/html-wishlist.jpg)

**FAQ Page**  
![Course Page HTML Validation](static/documentation/testing/html-faq.jpg)

**Add to Bag Page**  
![Review Post Page HTML Validation](static/documentation/testing/html-add-to-bag.jpg)

**Contact Page**  
![Contact Page HTML Validation](static/documentation/testing/html-contact.jpg)

**Product Management Page**  
![Message Sent HTML Validation](static/documentation/testing/html-product-management.jpg)

**Shopping Bag Page**  
![Bag Page HTML Validation](static/documentation/testing/html-bag.jpg)

**Checkout Page**  
![Checkout Page HTML Validation](static/documentation/testing/html-checkout.jpg)

**Checkout Success Page**  
![Checkout Success HTML Validation](static/documentation/testing/html-checkout-success.jpg)

**Profile Page**  
![Profile Page HTML Validation](static/documentation/testing/html-profile.jpg)

**Order History Page**  
![Order History HTML Validation](static/documentation/testing/html-order-history.jpg)

**Products & Deals Page**  
![Products & Deals HTML Validation](static/documentation/testing/html-product&deals.jpg)

### Validation Errors

| **CSS Validation Issue** | **Description** |
|:-------------------------|:----------------|
| Invalid CSS property `text-decoration-style: none;` | `text-decoration-style` does not accept `none`; corrected |
| Invalid CSS property `font-weight: 200px;` | `font-weight 200px` is not  `a font weight value`; corrected |



### CSS Validation Corrected
Testing using the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator/) to validate all of my CSS files.
- [x] CSS validation all passed.

**base.css**  
![base.css Validation](static/documentation/testing/css-base.jpg)

**profile.css**  
![profile.css Validation](static/documentation/testing/css-profile.jpg)

**checkout.css**  
![checkout.css Validation](static/documentation/testing/css-checkout.jpg)


### Validation Errors

| **JavaScript Validation Issue** | **Description** |
|:---------------------------------|:----------------|
| `console` undefined | Added `/* global console */` comment to declare `console` as a global variable |


### JavaScript Validation Corrected
Testing using the recommended [JShint Validator](https://jshint.com/) to validate all of my JavaScript files.
- [x] JavaScript tests all passed.

**star-rating.js**  
![star-rating.js Validation](static/documentation/testing/js-star-rating.jpg)

**wishlist.js**  
![wishlist.js Validation](static/documentation/testing/js-wishlist.jpg)

**countryfield.js**  
![countryfield.js Validation](static/documentation/testing/js-countryfield.jpg)

**bag.js**  
![bag.js Validation](static/documentation/testing/js-bag.jpg)

**stripe_element.js**  
![stripe_element.js Validation](static/documentation/testing/js-stripe-element.jpg)

### CI Python Linter
Testing using the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com/) to validate all of my Python files.
- [x] Python tests all passed.

During development, code quality was maintained by following the [PEP8](https://peps.python.org/pep-0008/) style guide for Python. Errors & warnings were detected & corrected accross apps by running flake8.
    
Common issues that were identified & resolved included:
| **Issue** | **Action Taken** |
|:----------|:-----------------|
| Lines exceeding 79 characters (E501) | Broken into multiple lines for readability |
| Trailing whitespace (W291) & blank lines with whitespace (W293) | Cleaned up for clarity & consistency |
| Missing or insufficient blank lines after class or function definitions (E302, E305) | Added blank lines to improve code structure |
| Unused imports (F401) & unused variables (F841) | Removed unused code for a cleaner, efficient codebase |
| Missing newlines at end of files (W292, W391) | Added newlines to meet formatting standards |


    All Python files containing the project's code have been tested, & the errors were fixed.
    After running the CI Python Linter, it shows there are no errors.

![Python Tests Clear](static/documentation/testing/py-clear.webp)
