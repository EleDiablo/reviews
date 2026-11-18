from django.contrib import admin
from django.urls import include, path
from reviews.views import ReviewListView, index, ThanksView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', index, name='index'),
    path('thanks/', ThanksView.as_view(), name='thanks'),
    path('list/', ReviewListView.as_view(), name='review_list')
]
