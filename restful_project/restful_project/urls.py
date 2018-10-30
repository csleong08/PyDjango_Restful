from django.conf.urls import url, include  

urlpatterns = [
    url(r'^', include('apps.restful_app.urls')),
]
