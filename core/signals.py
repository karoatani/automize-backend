# from channels.layers import get_channel_layer
# import json
# from asgiref.sync import async_to_sync

# from django.db.models.signals import post_save
# from django.dispatch import receiver

# from .models import Debt, Notification




# @receiver(post_save, sender=Debt)
# def notify_user_on_debt_add(sender, instance, **kwargs):
#     user = instance.user
#     notification = Notification.objects.create(user=user, message="New Debt Added")
    
#     message = {
#         "notification_message" : notification.message
#     }
    
#     group_name = user.username + "_"+ str(user.id)

#     channel_layer = get_channel_layer()

#     async_to_sync(channel_layer.group_send)(
        
#         group_name,
#         {
#             'type': 'send.notification',
#             'text': message
#         }
#     )