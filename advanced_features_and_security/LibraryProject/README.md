# In the 'bookshelf/models.py' file
# Custom permissions have been defined for the Book model.
# Permissions:
# - can_view: Allows viewing books.
# - can_create: Allows creating books.
# - can_edit: Allows editing books.
# - can_delete: Allows deleting books.

# In the 'bookshelf/views.py' file
# Permissions are enforced for views that create, edit, or delete books.
# The 'permission_required' decorator is used to check if the user has the required permission before performing any action.
# Example:
# - The 'create_book' view requires 'can_create' permission.
# - The 'edit_book' view requires 'can_edit' permission.
# - The 'delete_book' view requires 'can_delete' permission.

# User groups:
# - Editors: Can create and edit books (permissions: can_create, can_edit).
# - Viewers: Can only view books (permission: can_view).
# - Admins: Can perform all actions (permissions: can_view, can_create, can_edit, can_delete).

# Django Security Best Practices

## Settings
- `DEBUG` is set to `False` for production.
- Security-related settings configured: XSS filter, X-Frame-Options, Content-Type-Nosniff, secure cookies.

## CSRF Protection
- All forms include `{% csrf_token %}` to protect against CSRF attacks.

## SQL Injection Protection
- All database queries are handled using Django's ORM to prevent SQL injection.

## Content Security Policy (CSP)
- `django-csp` middleware is used to enforce a Content Security Policy header.

# HTTPS and Secure Redirects Implementation

## Overview
To enhance the security of the Django application, several settings have been configured to enforce HTTPS and secure cookies.

## Changes Made:
1. **SECURE_SSL_REDIRECT**: Enabled redirection of HTTP requests to HTTPS to ensure all communications are encrypted.
2. **SECURE_HSTS_SECONDS**: Configured to 31536000 seconds (one year) to instruct browsers to only access the site via HTTPS.
3. **SECURE_HSTS_INCLUDE_SUBDOMAINS**: Enabled to apply HSTS to all subdomains.
4. **SECURE_HSTS_PRELOAD**: Enabled to allow the site to be preloaded into browsers’ HSTS list.
5. **SESSION_COOKIE_SECURE & CSRF_COOKIE_SECURE**: Ensured that cookies are only transmitted over HTTPS.
6. **X_FRAME_OPTIONS**: Set to `DENY` to prevent clickjacking attacks.
7. **SECURE_CONTENT_TYPE_NOSNIFF**: Enabled to prevent MIME sniffing.
8. **SECURE_BROWSER_XSS_FILTER**: Enabled the browser’s XSS filter to help prevent cross-site scripting attacks.

## Deployment Configuration:
Nginx/Apache configurations were updated to serve the site over HTTPS, including SSL/TLS certificates and HSTS headers.

## Testing:
- Manually tested that all HTTP requests are redirected to HTTPS.
- Verified that secure cookies are set and transmitted only over HTTPS.
- Tested that all configured security headers are present in the HTTP responses.
