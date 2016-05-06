#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telepot
import time
import datetime
import numpy as np
import cv2

def handle(msg):
	chat_id = msg['from']['id']
	command = msg['text']

	print 'Mensaje recibido: %s' % command
	if command == '/hora':
		bot.sendMessage(chat_id, 'La hora es: ' + str(datetime.datetime.now()))
	elif command == '/help':
		bot.sendMessage(chat_id, 'Ayura')
	elif command == '/photo':
		bot.sendMessage(chat_id, 'Solicitando imágen de la cámara...')
		bot.sendChatAction(chat_id, 'upload_photo')
		cap = cv2.VideoCapture(0)
		ret, frame = cap.read()
		cv2.imwrite('/tmp/default.jpg',frame)
		cap.release()
		result = bot.sendPhoto(chat_id, open('/tmp/default.jpg', 'rb'), caption='Imagen desde la cámara.')
	else:
		bot.sendMessage(chat_id, 'Lo siento. No entendí tu mensaje.\nPuedes escribir el comando \'/help\' para obtener ayuda.')

bot = telepot.Bot('211389236:AAFvvA0oyQD31kfmmDvTWQN9F26T-Xd12ls')
bot.message_loop(handle)
print 'Estoy escuchando...'

while 1:
	time.sleep(10)
