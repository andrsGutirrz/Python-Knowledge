from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile

# Register your models here.

#admin.site.register(Profile)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """profile admin"""
    list_display = ('pk','user', 'phone_number', 'website', 'picture')
    list_display_links = ('pk','user',)
    list_editable = ('phone_number','website','picture',)
    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__lastname',
        'phone_number'
    ) # __ to access to the relationship attribs

    list_filter = ('created', 'modified', 'user__is_active','user__is_staff')

    fieldsets = (
        ('Profile', {
            'fields' : (
                ('user','picture')
            ),
        }),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography')
            ),
        }),
        ('Metadata',{
            'fields': (
                ('created', 'modified')
            ),
        })
    )

    readonly_fields = ('created', 'modified')


    # What we want, is to attach Profile to the User interface
    # see docs for more information

class ProfileInline(admin.StackedInline):
    """profile in-line admin for users"""

    model = Profile
    can_delete = False
    verbose_name = 'profile'

class UserAdmin(BaseUserAdmin):
    """ Add profile admin to base user admin interface """

    inlines = (ProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff')

# mandatory
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
