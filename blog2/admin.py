from django.contrib import admin

from .models import Post, Category, Tag, Comments, SubscribeNewsletter, Country, City, Profile

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comments)
admin.site.register(SubscribeNewsletter)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Profile)

# Register your models here.
