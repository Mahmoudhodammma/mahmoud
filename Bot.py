import requests,telebot
from telebot import types
import re,os
tok = "5079622366:AAGSHmz4fGr5S_Sk-12i_Mcjt3OQTYdy9M8"
eg = "🇪🇬"
si = "🇮🇱"
su = "🇸🇦"
dev = types.InlineKeyboardButton(text="- 7🅰︎🅼︎🅾︎🅳︎🆈︎ -",url='https://t.me/uufffuu')
ge = types.InlineKeyboardButton(text=f"- EGYPT "+str(eg),callback_data="egy")
sui = types.InlineKeyboardButton(text=f"- ISRAEL "+str(si),callback_data="sii")
siu = types.InlineKeyboardButton(text=f"- SAUDI ARABIA "+str(su),callback_data="suu")
bot = telebot.TeleBot(tok)
@bot.message_handler(commands=["start"])
def me(message):
	name = message.chat.first_name
	u = "https://t.me/pydroi_d_3/35"
	key = types.InlineKeyboardMarkup()
	key.row_width=1
	key.add(ge,sui,siu,dev)
	bot.send_photo((message.chat.id),u,f"""
- Hi {name}
- Surveillance Camera 🤳
- Please Choice Country 
- Dev •@uufffuu""",reply_to_message_id=(message.message_id),reply_markup=key)
@bot.callback_query_handler(func=lambda call :True)
def f(call):
	if call.data=="egy":
		p(call.message)
	if call.data=="sii":
		o(call.message)
	if call.data=="suu":
		i(call.message)
def i(message):
	x=0
	bot.send_message(message.chat.id,f"Wait Get Ip Cam "+str(su))
	headers = {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0"}
	url = requests.get("https://www.insecam.org/en/bycountry/SA",headers=headers)
	last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', url.text)[0]
	for page in range(int(last_page)):
		res = requests.get(f"https://www.insecam.org/en/bycountry/SA/?page={page}",headers=headers)
		find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
		for ip in find_ip:
			print(ip)
			x+=1
			with open("IP.txt","a") as mode:
				mode.write(f"{ip}\n")
	file = open("IP.txt")
	bot.send_document((message.chat.id),file,caption=f"""
- - - - - - - - - - - - - - - - - -
- Done Get Ip Cam ✔️
- Ip : {x}
- ᴄᴏᴜɴᴛʀʏ : {su}
- - - - - - - - - - - - - - - - - -
""",reply_to_message_id=(message.message_id))
	os.remove("IP.txt")
def o(message):
	x=0
	bot.send_message(message.chat.id,f"Wait Get Ip Cam "+str(si))
	headers = {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0"}
	url = requests.get("https://www.insecam.org/en/bycountry/SI",headers=headers)
	last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', url.text)[0]
	for page in range(int(last_page)):
		res = requests.get(f"https://www.insecam.org/en/bycountry/SI/?page={page}",headers=headers)
		find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
		for ip in find_ip:
			print(ip)
			x+=1
			with open("IP.txt","a") as mode:
				mode.write(f"{ip}\n")
	file = open("IP.txt")
	bot.send_document((message.chat.id),file,caption=f"""
- - - - - - - - - - - - - - - - - -
- Done Get Ip Cam ✔️
- Ip : {x}
- ᴄᴏᴜɴᴛʀʏ : {si}
- - - - - - - - - - - - - - - - - -
""",reply_to_message_id=(message.message_id))
	os.remove("IP.txt")	
def p(message):
	x=0
	bot.send_message(message.chat.id,f"Wait Get Ip Cam "+str(eg))
	headers = {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0"}
	url = requests.get("https://www.insecam.org/en/bycountry/EG",headers=headers)
	last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', url.text)[0]
	for page in range(int(last_page)):
		res = requests.get(f"https://www.insecam.org/en/bycountry/EG/?page={page}",headers=headers)
		find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
		for ip in find_ip:
			print(ip)
			x+=1
			with open("IP.txt","a") as mode:
				mode.write(f"{ip}\n")
	file = open("IP.txt")
	bot.send_document((message.chat.id),file,caption=f"""
- - - - - - - - - - - - - - - - - -
- Done Get Ip Cam ✔️
- Ip : {x}
- ᴄᴏᴜɴᴛʀʏ : {eg}
- - - - - - - - - - - - - - - - - -
""",reply_to_message_id=(message.message_id))
	os.remove("IP.txt")
bot.polling(True)
