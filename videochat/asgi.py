"""
ASGI config for videochat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/asgi/
"""
print("ASGI LOADED")

import os
from channels.routing import ProtocolTypeRouter , URLRouter
from django.core.asgi import get_asgi_application
from video.consumers import VideoChat
from django.urls import path
from channels.security.websocket import AllowedHostsOriginValidator
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'videochat.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter([
        path("ws/", VideoChat.as_asgi()),
    ]),
})