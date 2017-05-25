from django.contrib import admin
from statistic.models import Client, ExtendedClient, Statistic

# Register your models here.
admin.site.register(Client)
admin.site.register(ExtendedClient)
admin.site.register(Statistic)
