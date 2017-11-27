#lab6aex4

import json
f=open('wx.json')
data=f.read()
f.close()
wx= json.loads(data)
main=wx['main']
wind=wx['wind']
speed=wind['speed']
deg=wind['deg']
temp=main['temp']
humidity=main['humidity']

print(wind,speed,deg,temp,humidity)