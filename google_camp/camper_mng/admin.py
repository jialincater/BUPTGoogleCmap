from django.contrib import admin

# Register your models here.
from .models import Camper

class CamperAdmin(admin.ModelAdmin):
    list_display = ['name', 'student_id','mail','phone','grade','school','gender','classNo']
    class Meta:
		model = Camper
admin.site.register(Camper,CamperAdmin)