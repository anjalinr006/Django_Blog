from django.conf.urls import url
from .views import (
      post_post,
      post_view,
)

urlpatterns = [
    url('post', post_post),
    url(r'^(?P<id>\d+)/$', post_view),
]


