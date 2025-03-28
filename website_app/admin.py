from django.contrib import admin
from .models import ProjectsDone, ServiceOffers, MessagesFromForm, FrequentlyAsked


admin.site.register(ProjectsDone)
admin.site.register(ServiceOffers)
admin.site.register(MessagesFromForm)
admin.site.register(FrequentlyAsked)
