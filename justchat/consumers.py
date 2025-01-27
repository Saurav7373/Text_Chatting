import json
import asyncio
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
# from .models import Thread, ChatMessage
class ChatConsumer( AsyncConsumer ):
    async def websocket_connect(self, event):
        print( "connected", event )
        await self.send({
            "type": "websocket.accept"
        })
        await asyncio .sleep(10)
        await self.send( {
            "type": "websocket.send"
        } )

    async def websocket_recive(self, event):
        print( "receive", event )

    async def websocket_disconnect(self, event):
        print( 'disconnect', event )