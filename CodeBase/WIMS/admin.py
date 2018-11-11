from django.contrib import admin


from .models import User, Admin, Authentication, Project, ProjectMembers, Item, ProjectMaterials, Donor, Donation

# Register your models here.
admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Authentication)
admin.site.register(Project)
admin.site.register(ProjectMembers)
admin.site.register(Item)
admin.site.register(ProjectMaterials)
admin.site.register(Donor)
admin.site.register(Donation)

