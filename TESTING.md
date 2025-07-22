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