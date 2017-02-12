from django.contrib import admin
from register.models import MyUser
# Register your models here.
class UserAdmin(admin.ModelAdmin):
	list_display = ('uid','username','phone')
	class Meta:
		model = MyUser

admin.site.register(MyUser,UserAdmin)
