from django.contrib import admin

# Register your models here.
from .models import Test
# Register your models here.
class TestAdmin(admin.ModelAdmin):
	list_display = ("test_id","status")
	class Meta :
		model = Test

admin.site.register(Test,TestAdmin)