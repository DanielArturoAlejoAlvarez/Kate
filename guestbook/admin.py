from django.contrib import admin

#TODO: Import our models
from .models import Comment
#FIXME: Configure Comment Register to Admin Panel
admin.site.register(Comment)