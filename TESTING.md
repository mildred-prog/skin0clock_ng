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

| **Feature** | **admin.py** | **apps.py** | **models.py** | **urls.py** | **views.py** | **forms.py** | **tests.py** | 
| ----------- |:------------:|:-----------:|:-------------:|:-----------:|:------------:|:------------:|:------------:|
| skin0clock_ng | n/a | [no errors](static/documentation/testing/main-urls.jpg) | [no errors](static/documentation/testing/main-views.jpg) | n/a | n/a |
| home | n/a | [no errors](static/documentation/testing/home-apps.jpg) | n/a | [no errors](static/documentation/testing/home-urls.jpg) | [no errors](static/documentation/testing/home-views.jpg) | n/a | [no errors](static/documentation/testing/home-test.webp) |
| products | [no errors](static/documentation/testing/products-admin.jpg) | [no errors](static/documentation/testing/products-apps.jpg) | [no errors](static/documentation/testing/products-models.jpg) | [no errors](static/documentation/testing/products-urls.jpg) | [no errors](static/documentation/testing/products-views.jpg) | [no errors](static/documentation/testing/products-forms.jpg) | [no errors](static/documentation/testing/products-test.webp) |
| wishlist | [no errors](static/documentation/testing/wishlist-admin.jpg) | n/a | [no errors](static/documentation/testing/wishlist-models.jpg) | [no errors](static/documentation/testing/wishlist-urls.jpg) | [no errors](static/documentation/testing/wishlist-views.jpg) | n/a | [no errors](static/documentation/testing/wishlist-test.jpg) |
| faq | [no errors](static/documentation/testing/faq-admin.jpg) | [no errors](static/documentation/testing/faq-apps.jpg) | [no errors](static/documentation/testing/faq-models.jpg) | [no errors](static/documentation/testing/faq-urls.jpg) | [no errors](static/documentation/testing/faq-views.jpg) | n/a | [no errors](static/documentation/testing/faq-test.jpg) |
| bag | n/a | [no errors](static/documentation/testing/bag-apps.jpg) | n/a | [no errors](static/documentation/testing/bag-urls.jpg) | [no errors](static/documentation/testing/bag-views.jpg) | n/a | [no errors](static/documentation/testing/bag-test.jpg) |
| checkout | [no errors](static/documentation/testing/checkout-admin.jpg) | [no errors](static/documentation/testing/checkout-apps.jpg) | [no errors](static/documentation/testing/checkout-models.jpg) | [no errors](static/documentation/testing/checkout-urls.jpg) | [no errors](static/documentation/testing/checkout-views.jpg) | [no errors](static/documentation/testing/checkout-forms.jpg) | [no errors](static/documentation/testing/checkout-test.jpg) |
| profiles | n/a | [no errors](static/documentation/testing/profiles-apps.jpg) | [no errors](static/documentation/testing/profiles-models.jpg) | [no errors](static/documentation/testing/profiles-url.jpg) | [no errors](static/documentation/testing/profiles-views.jpg) | [no errors](static/documentation/testing/profiles-forms.jpg) | [no errors](static/documentation/testing/profiles-test.jpg) |
| review | [no errors](static/documentation/testing/review-admin.jpg) | [no errors](static/documentation/testing/review-apps.jpg) | [no errors](static/documentation/testing/review-models.jpg) | [no errors](static/documentation/testing/wishlist-urls.jpg) | [no errors](static/documentation/testing/wishlist-views.jpg) | [no errors](static/documentation/testing/review-forms.jpg) | [no errors](static/documentation/testing/review-test.jpg) |
| contact | [no errors](static/documentation/testing/contact-admin.jpg) | [no errors](static/documentation/testing/contact-apps.jpg) | [no errors](static/documentation/testing/contact-models.jpg) | [no errors](static/documentation/testing/contact-urls.jpg) | [no errors](static/documentation/testing/contact-views.jpg) | [no errors](static/documentation/testing/contact-forms.jpg) | [no errors](static/documentation/testing/contact-test.jpg) |


| **Feature** | **contexts.py** | **signals.py** | **webhook_handler.py** | **webhooks.py** | **utils.py** |
|-------------|:---------------:|:--------------:|:----------------------:|:---------------:|:-------------:|
| bag | [no errors](static/documentation/testing/bag-context.jpg) | n/a | n/a | n/a | [no errors](static/documentation/testing/bag-utils.webp)
| checkout | n/a | [no errors](static/documentation/testing/checkout-signals.jpg) | [no errors](static/documentation/testing/checkout-webhook-handler.jpg) | [no errors](static/documentation/testing/checkout-webhooks.jpg)| n/a


## Backend Testing
Automated backend testing has been implemented across all apps using Django’s built-in TestCase framework. Each app has its own test.py file containing unit & view tests. All tests are [PEP8](https://peps.python.org/pep-0008/) compliant & validate the critical functionality of models, forms, views & session handling.

__Apps tested:__
- [x] home
- [x] products
- [x] wishlist
- [x] review
- [ ] faq
- [x] bag
- [x] checkout
- [x] profiles
- [x] contact

| **Testing Includes** | **Description** |
|:--------------|:----------------|
| **Model String Representations** | Tests that model `__str__` methods return correct readable strings. |
| **Form Validations** | Ensures forms validate correctly with valid & invalid inputs. |
| **View Responses & Template Rendering** | Verifies correct HTTP responses & that the correct templates are rendered. |
| **Access Control for Restricted Views** | Tests that only admins can access certain admin-only views & actions. |
| **Bag Session Behavior** | Tests session functionality for adding, adjusting & removing bag items. |
| **Checkout Process & Order Creation** | Verifies checkout flow, order saving & stock adjustments post-purchase. |
| **Stripe Webhook Handling & Order Confirmation** | Tests webhook reception, validation & updating orders after Stripe confirmation. |
| **User Profile Updates & Order History Retrieval** | Ensures users can update profiles & view past orders from their account page. |


### Running Tests

    NOTE: To run all tests across the project:
    run `python manage.py test` in console
    OR
    run `python manage.py test app_name` in console for specific app testing

- [x] **Home Test Results**  
![console Validation](static/documentation/testing/console-home-test.jpg)

- [x] **Products Test Results**  
![console Validation](static/documentation/testing/console-product-test.jpg)

- [x] **Faq Test Results**  
![console Validation](static/documentation/testing/console-faq-test.jpg)

- [x] **Review Test Results**  
![console Validation](static/documentation/testing/console-review-test.jpg)

- [x] **Bag Test Results**  
![console Validation](static/documentation/testing/console-bag-test.jpg)

- [x] **Checkout Test Results**  
![console Validation](static/documentation/testing/console-checkout-test.jpg)

- [x] **Profiles Test Results**  
![console Validation](static/documentation/testing/console-profiles-test.jpg)

- [x] **Wishlist Test Results**  
![console Validation](static/documentation/testing/console-wishlist-test.jpg)

- [x] **Contact Test Results**  
![console Validation](static/documentation/testing/console-contact-test.jpg)

## Lighthouse Test

- [x] Desktop view:

    **Home Page**  
    ![Lighthouse Report Home](static/documentation/testing/lh-home.jpg)

    **Products page**  
    ![Lighthouse Report Products](static/documentation/testing/lh-products.jpg)

    **Faq Page**  
    ![Lighthouse Report Grow Guide](static/documentation/testing/lh-guide.webp)

    **Wishlist Page**  
    ![Lighthouse Report Wishlist](static/documentation/testing/lh-courses.webp)

    **Bag Page**  
    ![Lighthouse Report Bag](static/documentation/testing/lh-bag.webp)

    **Checkout Page**  
    ![Lighthouse Report Checkout](static/documentation/testing/lh-checkout.webp)

    **Profiles Page**  
    ![Lighthouse Report Profiles](static/documentation/testing/lh-profiles.webp)

    **Signup Page**  
    ![Lighthouse Report Signup](static/documentation/testing/lh-signup.webp)

    **Login Page**  
    ![Lighthouse Report Login](static/documentation/testing/lh-login.webp)

    **Logout Page**  
    ![Lighthouse Report Logout](static/documentation/testing/lh-logout.webp)

    **Contact Page**  
    ![Lighthouse Report Logout](static/documentation/testing/lh-contact.webp)

- [x] Mobile view:

    Performance was lower than preferred on mobile view due to the site being image heavy on landing page with hero & featured products. Images used in the sites design were compressed to offer the best chance for a decent performance score.

    **Mobile Home Page**  
    ![Lighthouse Report Home Mobile](static/documentation/testing/lh-mobile.webp)
