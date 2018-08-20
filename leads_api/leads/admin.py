from django.contrib import admin

from leads_api.leads.models import Pessoa, Tipo


admin.site.register(Pessoa)

admin.site.register(Tipo)
