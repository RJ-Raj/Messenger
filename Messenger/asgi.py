import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from chatapp.consumers import *

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Messenger.settings')

application = ProtocolTypeRouter({
    'http' : get_asgi_application(),
    'websocket' : AuthMiddlewareStack(
        URLRouter([
            path("ws/room/<str:room_name>/",Chat.as_asgi()),
            path("ws/status/",Status.as_asgi()),
            path("ws/typing/",Typing.as_asgi()),
        ])
    )
})