from django.contrib import admin


from .models import Project, ProjectMembers, Item, ProjectMaterials, Donor, Donation

# Register your models here.
admin.site.register(Project)
admin.site.register(ProjectMembers)
admin.site.register(Item)
admin.site.register(ProjectMaterials)
admin.site.register(Donor)
admin.site.register(Donation)

