from django.conf.urls import url
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator

from chating.consumers import ChatConsumer
from .auth_token import TokenAuthMiddleware 

application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    'websocket': AllowedHostsOriginValidator(
        TokenAuthMiddleware(
            URLRouter(  
                [
                    url(r"messages/(?P<username>[\w.@+-]+)/$",ChatConsumer)
                ]
            )
        )
    )
})