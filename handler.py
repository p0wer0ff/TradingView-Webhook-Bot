# import config
import requests


def send_alert(data):

    msg = data["msg"].encode("latin-1", "backslashreplace").decode("unicode_escape")
    x={"msgtype": "text", 
    "text": {
        "content": msg}}

    try :
        requests.post(url="https://oapi.dingtalk.com/robot/send?access_token=82f8196870626c0ce51280abd06170aeb0bc79da686dd5fb3ad07207931e4eeb",data=x)
    except:
        requests.post(url="https://oapi.dingtalk.com/robot/send?access_token=82f8196870626c0ce51280abd06170aeb0bc79da686dd5fb3ad07207931e4eeb",data=x)
