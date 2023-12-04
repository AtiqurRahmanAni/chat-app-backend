from django.urls import path
from . views import *


urlpatterns = [
    path("thread/", UserThreadView.as_view(), name="thread"),
    path("message/", UserMessageView.as_view(), name="message"),
]
