from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('', include('issue_tracker_app.urls')),
    path('admin/', admin.site.urls, name="admin"),
    path('users/', include('users.urls'))

]
