from django.urls import path
from app import consumers

websocket_urlpatterns=[
    # path('webs/sync/<str:GroupName>/<str:user2_id>/',consumers.mysync_class.as_asgi()),
    path('webs/sync/<str:GroupName>/',consumers.mysync_class.as_asgi()),
]
