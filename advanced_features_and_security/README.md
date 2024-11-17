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
