from pyrogram import Client

from datetime import datetime
import time

StartTime = time.time()
START_TIME = datetime.now()
SUDO_USER = 6834053539
clients = []
ids = []

if API_ID:
   API_ID = 20112715
else:
   print("WARNING: API ID NOT FOUND !!")  

if API_HASH:
   API_HASH = "fe56c4634729f7c557b3298f0bb0cf1e"
else:
   print("WARNING: API HASH NOT FOUND !!")      


STRING_SESSION1 = ""

if STRING_SESSION1:   
   print("Client1: Found.. Starting..📳")
   client1 = Client(name="one", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION1, plugins=dict(root="VGS/modules"))
   clients.append(client1)

if STRING_SESSION2:
   print("Client2: Found.. Starting.. 📳")
   client2 = Client(name="two", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION2, plugins=dict(root="VGS/modules"))
   clients.append(client2)

if STRING_SESSION3:
   print("Client3: Found.. Starting.. 📳")
   client3 = Client(name="three", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION3, plugins=dict(root="VGS/modules"))
   clients.append(client3)

if STRING_SESSION4:
   print("Client4: Found.. Starting.. 📳")
   client4 = Client(name="four", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION4, plugins=dict(root="VGS/modules"))
   clients.append(client4)

if STRING_SESSION5:
   print("Client5: Found.. Starting.. 📳")
   client5 = Client(name="five", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION5, plugins=dict(root="VGS/modules"))
   clients.append(client5)

if STRING_SESSION6:
   print("Client6: Found.. Starting.. 📳")
   client6 = Client(name="six", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION6, plugins=dict(root="VGS/modules"))
   clients.append(client6)

if STRING_SESSION7:
   print("Client7: Found.. Starting.. 📳")
   client7 = Client(name="seven", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION7, plugins=dict(root="VGS/modules"))
   clients.append(client7)

if STRING_SESSION8:
   print("Client8: Found.. Starting.. 📳")
   client8 = Client(name="eight", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION8, plugins=dict(root="VGS/modules"))
   clients.append(client8)

if STRING_SESSION9:
   print("Client9: Found.. Starting.. 📳")
   client9 = Client(name="nine", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION9, plugins=dict(root="VGS/modules"))
   clients.append(client9)

if STRING_SESSION10:
   print("Client10: Found.. Starting.. 📳")
   client10 = Client(name="ten", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION10, plugins=dict(root="VGS/modules")) 
   clients.append(client10)
