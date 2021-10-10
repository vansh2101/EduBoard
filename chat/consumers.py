from channels.generic.websocket import AsyncWebsocketConsumer
import json



class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name'].replace(' ', '')
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()


    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )


    async def receive(self, text_data):
        text_data_json = json.loads(text_data)

        if 'action' in text_data_json and text_data_json['action'] == 'disconnect':
            return await self.close()
        
        message = text_data_json['message']
        user = text_data_json['username']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chatroom_message',
                'message': message,
                'username': user
            }
        )


    async def chatroom_message(self, event):
        message = event['message']
        user = event['username']

        await self.send(text_data=json.dumps({
            'message': message,
            'username': user,
        }))