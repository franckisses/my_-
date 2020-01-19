from django.conf.urls import url
from .views import UserView

# post  http://127.0.0.1:8000/v1/users
urlpatterns = [
    url(r'^$',UserView.as_view())
]