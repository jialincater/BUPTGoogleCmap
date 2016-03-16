from django.contrib import admin
from .models import Agent
# Register your models here.
class AgentAdmin(admin.ModelAdmin):
    list_display = ['name','join','level', 'mail','phone','eat',]
    class Meta:
		model = Agent
admin.site.register(Agent,AgentAdmin)