from django.contrib import admin
from .models import Vulnes

class ProfileAdmin(admin.ModelAdmin):

    list_display = [i.name for i in Vulnes._meta.fields]
    list_filter = ["id"]

    class Meta():
        model = Vulnes

admin.site.register(Vulnes, ProfileAdmin)