
from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync,sync_to_async
from app.models import CustomUser
from channels.db import database_sync_to_async
import json

# channel layers..

class mysync_class(SyncConsumer):
    def websocket_connect(self,event):
        print('def websocket_connect',event)       # <---- this is event....
        print('channel layer',self.channel_layer)
        print('channel name',self.channel_name)
        
        
        self.group_name=self.scope['url_route']['kwargs']['GroupName']
        print('groupname--',self.group_name)
        # print('self.scope[url_route]--->',self.scope['url_route'])

        async_to_sync(self.channel_layer.group_add)(self.group_name,self.channel_name)
        self.send({
            'type':'websocket.accept',
            'text':'server connection is done'
        })

    def websocket_receive(self,event):
        print('message coming from client event(sync) --->',event)
        print('message coming from client(sync) --->',event['text'])
        print('type of the event(sync)--->',type(event['text']))
        
        chat_data = json.loads(event['text'])
        print('chat data(sync)-->',chat_data) 
        print('type of chat data(sync)-->',type(chat_data)) 
        print(' actual chat data message(sync)---->',chat_data['msg']) 
        print('type of actual chat data(sync)-->',type(chat_data['msg'])) 

# here the code of authenticate the user...........
        if self.scope['user'].is_authenticated:
#  create chat object...-

            chat_data['user'] = self.scope['user'].username
            print('complete data....(sync)--->',chat_data)
            print('type of complete data....(sync)--->',type(chat_data))

            async_to_sync(self.channel_layer.group_send)(self.group_name,
                    {'type':'chat.message',             #<------event
                    'message': json.dumps(chat_data)
                    })

        else:
            self.send({
                'type':'websocket.send',
                'text':json.dumps({'msg':'Login Required','user':'unknown'})
            })            

    def chat_message(self,event):
        print('chat_message_event(sync)-->',event)    
        print('chat_messag_actual data(sync)-->',event['message'])    
        print('chat_messag_ type of_ actual data(sync)-->',type(event['message']))    
        self.send({
            'type':'websocket.send',
            'text':event['message'],
        })    
 
    def websocket_disconnect(self,event):
       
        # self.user2_id=self.scope['url_route']['kwargs']['user2_id']
        # print('from backend diconnect........ ') 
          
        async_to_sync(self.channel_layer.group_discard)(self.group_name,self.channel_name)
        user_obj = CustomUser.objects.get(username=self.scope['user'].username)
        # user2_obj = CustomUser.objects.get(pk = self.user2_id)

        # user1
        user_obj.is_online = False
        user_obj.save()        
        user_obj.is_reserved = False
        user_obj.save()
        
        # user2
        # user2_obj.is_online = False
        # user2_obj.save()        
        # user2_obj.is_reserved = False
        # user2_obj.save()

       
        raise StopConsumer()    
        
    # ---------------------------------------------
    

