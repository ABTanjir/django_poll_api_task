from django.contrib import admin

from .models import Poll
from .models import choice

admin.site.register(Poll)
admin.site.register(choice)