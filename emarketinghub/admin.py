from django.contrib import admin
from oscar.core.loading import get_model

EmarketHub = get_model('emarketinghub', 'EmarketingHub')

class EmarketHubAdmin(admin.ModelAdmin):
	pass

admin.site.register(EmarketHub, EmarketHubAdmin)