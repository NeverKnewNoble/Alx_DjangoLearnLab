# Permissions and Groups Setup

## Custom Permissions

The `Book` model has the following custom permissions:
- **can_view**: Allows viewing of book details.
- **can_create**: Allows creating new books.
- **can_edit**: Allows editing existing books.
- **can_delete**: Allows deleting books.

## Groups and Permissions

The following groups are set up with specific permissions:

- **Viewers**: can_view
- **Editors**: can_create, can_edit, can_view
- **Admins**: can_create, can_edit, can_delete, can_view

## Enforcing Permissions in Views

Permissions are enforced in views using the `@permission_required` decorator. Users must have the relevant permissions to access create, edit, and delete actions.
