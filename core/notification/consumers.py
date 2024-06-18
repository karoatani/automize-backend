import json
from channels.generic.websocket import WebsocketConsumer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AnonymousUser
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

class NotificationConsumer(WebsocketConsumer):
    def connect(self):
        user = self.scope["user"]
        self.name = user.username + "_"+ str(user.id)
        
        async_to_sync(self.channel_layer.group_add)(
            self.name, self.channel_name
        )
        self.accept()


    
    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.name, self.channel_name
        )
        self.close()
        
    
    
    
    def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        try:
            message = data["notification_message"]
            
            async_to_sync(self.channel_layer.group_send)(self.name,{
                "type": "send.notification",
                "text": data,
            },
            )
        except:
            pass
    

    def send_notification(self,event):
        notification_message = event["text"]
        self.send(text_data=json.dumps(notification_message))


