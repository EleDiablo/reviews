from django.contrib import admin

from .models import Review

admin.site.empty_value_display = '----'


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'text')


admin.site.register(Review, ReviewsAdmin)
