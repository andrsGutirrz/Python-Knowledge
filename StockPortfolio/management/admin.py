from django.contrib import admin
from .models import User,Portfolio,Investment,Transaction

admin.site.register(User)
admin.site.register(Portfolio)
admin.site.register(Investment)
admin.site.register(Transaction)
