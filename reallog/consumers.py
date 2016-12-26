#coding:utf-8
from django.http import HttpResponse
from channels.handler import AsgiHandler

#message.reply_channel    一个客户端通道的对象
#message.reply_channel.send(chunk)  用来唯一返回这个客户端

#一个管道大概会持续30s

#当连接上时，发回去一个connect字符串
def ws_connect(message):
    response = HttpResponse("Hello world! You asked for %s" % message.content['path'])

    #for chunk in AsgiHandler.encode_response(response):
    #message.reply_channel.send(response)'''

#将发来的信息原样返回
def ws_message(message):
    
    message.reply_channel.send({
        "text": message.content['text'],
    })
#断开连接时发送一个disconnect字符串，当然，他已经收不到了
def ws_disconnect(message):
    pass
    #message.reply_channel.send({"disconnect"})