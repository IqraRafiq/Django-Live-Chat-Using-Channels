from django.contrib import admin

# Register your models here.
from chating import models
admin.site.register(models.Thread)
admin.site.register(models.ChatMessage)
