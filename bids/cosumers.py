from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .redis import add_bid,get_top10_bidders,current_highest_bid
from asgiref.sync import sync_to_async
from market.models import Item

class DashboardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        bidpk=self.scope['url_route']['kwargs']['pk']
        self.bidpk=bidpk
        self.room_group_name=f'livebid-{bidpk}'
        await self.channel_layer.group_add(self.room_group_name,self.channel_name)
        await self.accept()
    async def disconnect(self,close_code):
        print(f'connection closed with code:{close_code}')
        await  self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    async def receive(self, text_data):
        text_data_json=json.loads(text_data)
        message=text_data_json['message']
        sender=text_data_json['sender']

        result= await current_highest_bid(self.bidpk)
        print(result)


        if len(result)!=0 and float(message) <= float(result[0][1]):

            # Send an error message back to the user
            self.send(text_data="error")
        else:
            await self.save_bid(float(message),sender,self.bidpk)


            await  self.channel_layer.group_send(self.room_group_name,{
                'type':'bid',
                'message':message,
                'sender':sender,

            })
    async def bid(self,event):
            message=event['message']
            sender=event['sender']

            await  self.send(text_data=json.dumps({
                'message':message,
                'sender':sender,

        }))


    async def save_bid(self,bid,user,pk):

        await add_bid(bid,user,pk)
    # async def send_top10(self,pk):
    #         top_10_bidders = await get_top10_bidders(pk)
    #         await self.send(text_data=json.dumps({
    #             'top_10_bidders': top_10_bidders
    #         }))

