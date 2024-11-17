from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group, Permission
from .models import CustomUser
from django.contrib.contenttypes.models import ContentType
from .models import Book

# Register the Book model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Customize the list display to show specific fields
    list_display = ('title', 'author', 'publication_year')
    # Add filters for easy navigation
    list_filter = ('publication_year', 'author')
    # Enable search functionality for specific fields
    search_fields = ('title', 'author')

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'date_of_birth', 'profile_photo', 'is_staff']
    list_filter = ['is_staff', 'is_superuser', 'groups']
    search_fields = ['username', 'email']
    ordering = ['username']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'date_of_birth', 'profile_photo', 'is_staff', 'is_active')}
        ),
    )

admin.site.register(CustomUser, CustomUserAdmin)

def create_groups_and_permissions():
    # Ensure permissions are created
    content_type = ContentType.objects.get_for_model(Book)
    Permission.objects.get_or_create(codename='can_view', name='Can view book', content_type=content_type)
    Permission.objects.get_or_create(codename='can_create', name='Can create book', content_type=content_type)
    Permission.objects.get_or_create(codename='can_edit', name='Can edit book', content_type=content_type)
    Permission.objects.get_or_create(codename='can_delete', name='Can delete book', content_type=content_type)

    # Create groups and assign permissions
    editors_group, created = Group.objects.get_or_create(name='Editors')
    editors_group.permissions.add(Permission.objects.get(codename='can_edit'))
    editors_group.permissions.add(Permission.objects.get(codename='can_create'))

    viewers_group, created = Group.objects.get_or_create(name='Viewers')
    viewers_group.permissions.add(Permission.objects.get(codename='can_view'))

    admins_group, created = Group.objects.get_or_create(name='Admins')
    admins_group.permissions.add(Permission.objects.get(codename='can_view'))
    admins_group.permissions.add(Permission.objects.get(codename='can_create'))
    admins_group.permissions.add(Permission.objects.get(codename='can_edit'))
    admins_group.permissions.add(Permission.objects.get(codename='can_delete'))

# Run the function to create groups and permissions
create_groups_and_permissions()

# Register your models here.
