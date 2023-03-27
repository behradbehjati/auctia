from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .redis import add_bid,current_highest_bid
from asgiref.sync import sync_to_async
from market.models import Item
from notification.notifs_tasks import notif_creation_task

"""
make a query async for channels
"""
@sync_to_async()
def item_query(item_id):
    return Item.objects.get(id=item_id)



class DashboardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        bidpk=self.scope['url_route']['kwargs']['pk']
        self.bidpk=bidpk
        self.room_group_name=f'livebid-{bidpk}'
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()
        if (await item_query(self.bidpk)).auction_status == False:
           await self.close(4003)







    async def disconnect(self,close_code):

        await  self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    async def receive(self, text_data):
        text_data_json=json.loads(text_data)
        message=text_data_json['message']
        sender=text_data_json['sender']

        result= await current_highest_bid(self.bidpk)

        minimum_bid= result[0][1] if len(result)!=0 else  (await item_query(self.bidpk)).starting_bid_price





        if float(message) <= float(minimum_bid):

            # Send an error message back to the user
            self.send(text_data="error")
        else:
            notif_creation_task.delay(result[0][0].decode('utf-8'),f' پیشنهادی بالاتر از پیشنهاد شما ثبت شد #{self.bidpk}')
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

