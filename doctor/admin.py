from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.AvailableTime)
class DesignationModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name",]}
admin.site.register(models.Designation,DesignationModelAdmin)
class SpecializationModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["name",]}
admin.site.register(models.Specialization,SpecializationModelAdmin)
admin.site.register(models.Doctor)
admin.site.register(models.Review)