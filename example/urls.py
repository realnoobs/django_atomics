from django.urls import path
from django.contrib import admin
from example.app.views import IndexPage

urlpatterns = [
    path("", IndexPage.as_view(), name="index"),
    path("admin/", admin.site.urls),
]
