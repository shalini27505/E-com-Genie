from django.contrib import admin
from .models import Hermes,Zara, Chanel,Traditional,Western, Kurtis,Paulmi,Hoodie,Lehanga,Night,Shirts,Track

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'image_url', 'description']
    list_display_links = ['name']
    search_fields = ['name', 'description']
    list_filter = ['price']
    list_per_page = 20


admin.site.register(Hermes, ProductAdmin)
admin.site.register(Zara, ProductAdmin)
admin.site.register(Chanel, ProductAdmin)
admin.site.register(Kurtis, ProductAdmin)
admin.site.register(Hoodie, ProductAdmin)
admin.site.register(Lehanga, ProductAdmin)
admin.site.register(Night, ProductAdmin)
admin.site.register(Traditional, ProductAdmin)
admin.site.register(Western, ProductAdmin)
admin.site.register(Paulmi, ProductAdmin)
admin.site.register(Shirts, ProductAdmin)
admin.site.register(Track, ProductAdmin)

