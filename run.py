# -*- coding: UTF-8 -*-

import Tkinter as tk
import tkMessageBox
import random
import codecs
import json

from gtts import gTTS
import mp3play
from pygame import mixer
import tempfile
import time

import os

import urllib3  # <- https://www.92ez.com/?action=show&id=23443
urllib3.disable_warnings()

# pip install gTTS==1.2.0			   <- requests.exceptions.SSLError: HTTPSConnectionPool(host='translate.google.com', port=443): 
# 										  Max retries exceeded with url: / 
# 										  (Caused by SSLError(SSLError("bad handshake: Error([('SSL routines', 'tls_process_server_certificate', 
# 										  'certificate verify failed')],)",),))

# pip install mp3play
# pip install pygame

# pip install --upgrade pyOpenSSL      <- 'module' object has no attribute 'X509_up_ref'


with codecs.open('word.json', 'r', 'utf-8') as f:
	word_dict = json.load(f)


if __name__ == '__main__':
	ok = 0

	win = tk.Tk()
	win.title("My English code GUI v2.0")
	win.geometry('800x430')
	win.resizable(0,0)
	win.configure(background='#696969')
	background_txt = '#696969'
	background_E_txt = '#AAAAAA'


	def B1_def():
		global ok
		global DayList
		global DayListOK
		DayListOK = []
		for x in DayList:
			if x.get() != '':
				DayListOK.append(x.get())
		tkMessageBox.showinfo(title='OK', message='chosen\n'+ str(DayListOK))
		ok = 1
		Comparison()

	def Comparison():
		

		def returnClickAction1(event):
			# print(sleep_text.get())
			if sleep_text.get() == val:
				tk.Label(win,
					text = 'very good!!',
					bg= background_txt,
					font = ('Arial',12),
					fg = '#0f02cc',
					width = 25 ,height=1,
					justify = 'left', anchor='w'
					).place(x = 350, y =  215)

				tk.Label(win,
					text = exp,
					bg= background_txt,
					fg = '#000088',
					font = ('Arial',12),
					width = 40,height=5 ,
					anchor='w').place(x = 100, y =  280)
			else:
				tk.Label(win,
					text = 'No, the answer is \"' + str(val) + '\".',
					bg= background_txt,
					fg = '#f70909',
					font = ('Arial',12),
					width = 25,height=1,
					justify = 'left', anchor='w').place(x = 350, y = 215)

		def returnClickAction2(event):
			Comparison()		
		
		def returnClickAction3(event):
			with tempfile.NamedTemporaryFile(delete=True) as fp:
				tts=gTTS(text=val, lang='en')
				tts.save("{}.mp3".format(fp.name))
				mixer.init()
				mixer.music.load("{}.mp3".format(fp.name))
				mixer.music.play()

			# tts = gTTS(text=val, lang='en')
			# tts.save("val.mp3")

			# clip = mp3play.load("val.mp3")
			# clip.play()
			# time.sleep(1)
			# clip.stop()

		# 以下兩函式，ctrl+A 全選 功能
		def callback(event):
			# print('T1.get():', T1.get())
			# or more universal
			# print('event.widget.get():', event.widget.get())
			# select text after 50ms
			win.after(50, select_all, event.widget)
		def select_all(widget):
			# select text
			widget.select_range(0, 'end')
			# move cursor to the end
			widget.icursor('end')

		global ok
		if ok == 1:
			# print( \
			# 	word_dict[ \
			# 		str(random.sample(DayListOK, 1)[0]) \
			# 	] \
			# )
			# pass

			# print(random.sample(word_dict,1)[0])
			w = random.sample(word_dict[str(random.sample(DayListOK, 1)[0])],1)[0]
			key  = w[0]
			val  = w[1]
			note = w[2]
			exp  = w[3]

			print("word : " + key + "\t, " + val)

			tk.Label(win,
				text = key,
				bg= background_txt,
				font = ('Arial',12),
				width = 30,height=1 ,
				anchor='w').place(x = 100, y =  190)

			sleep_text = tk.StringVar()
			T1 = tk.Entry(win,
				bg= background_E_txt,
				font=("Helvetica",16),
				width = 20, 
				textvariable = sleep_text)
			T1.bind('<Return>',returnClickAction1)
			T1.bind('<F1>',returnClickAction2)
			T1.bind('<F2>',returnClickAction3)
			T1.bind('<Control-a>', callback)
			T1.focus_set()
			T1.place(x = 100, y =  215)

			tk.Label(win,
				text = note,
				bg= background_txt,
				fg='#99FF99',
				font = ('Arial',12),
				width = 30,height=1 ,
				anchor='w').place(x = 100, y =  250)

			tk.Label(win,
				text = '',
				bg= background_txt,
				font = ('Arial',12),
				width = 25,height=1 ,
				anchor='w').place(x = 350, y =  215)
			tk.Label(win,
				text = '',
				bg= background_txt,
				font = ('Arial',12),
				width = 40,height=5 ,
				anchor='w').place(x = 100, y =  280)	
		else:
			tkMessageBox.showinfo(title='Error', message='請先選擇日期!!')

	DayList = []
	DayListOK = []
	for x in range(0,30):
		DayList.append(tk.StringVar())

	#--------------------------------------------------------
	tk.Label(win,
		text = '※Select days',
		bg= background_txt,
		font = ('Arial',12),
		width = 15,height=1 ,
		anchor='w').place(x = 10, y =  10)

	B1 = tk.Button(win, 
	    text='confirm',
	    width=10, height=2, 
	    command=B1_def).place(x = 650, y =  40)

	c1 =tk.Checkbutton(win,text='Day1' ,bg= background_txt ,variable=DayList[0] ,onvalue='Day1' ,offvalue='').place(x = 10 , y =  40)
	c2 =tk.Checkbutton(win,text='Day2' ,bg= background_txt ,variable=DayList[1] ,onvalue='Day2' ,offvalue='').place(x = 70 , y =  40)
	c3 =tk.Checkbutton(win,text='Day3' ,bg= background_txt ,variable=DayList[2] ,onvalue='Day3' ,offvalue='').place(x = 130, y =  40)
	c4 =tk.Checkbutton(win,text='Day4' ,bg= background_txt ,variable=DayList[3] ,onvalue='Day4' ,offvalue='').place(x = 190, y =  40)
	c5 =tk.Checkbutton(win,text='Day5' ,bg= background_txt ,variable=DayList[4] ,onvalue='Day5' ,offvalue='').place(x = 250, y =  40)
	c6 =tk.Checkbutton(win,text='Day6' ,bg= background_txt ,variable=DayList[5] ,onvalue='Day6' ,offvalue='').place(x = 310, y =  40)
	c7 =tk.Checkbutton(win,text='Day7' ,bg= background_txt ,variable=DayList[6] ,onvalue='Day7' ,offvalue='').place(x = 370, y =  40)
	c8 =tk.Checkbutton(win,text='Day8' ,bg= background_txt ,variable=DayList[7] ,onvalue='Day8' ,offvalue='').place(x = 430, y =  40)
	c9 =tk.Checkbutton(win,text='Day9' ,bg= background_txt ,variable=DayList[8] ,onvalue='Day9' ,offvalue='').place(x = 490, y =  40)
	c10=tk.Checkbutton(win,text='Day10',bg= background_txt ,variable=DayList[9] ,onvalue='Day10',offvalue='').place(x = 550, y =  40)

	c11=tk.Checkbutton(win,text='Day11',bg= background_txt ,variable=DayList[10],onvalue='Day11',offvalue='').place(x = 10 , y =  70)
	c12=tk.Checkbutton(win,text='Day12',bg= background_txt ,variable=DayList[11],onvalue='Day12',offvalue='').place(x = 70 , y =  70)
	c13=tk.Checkbutton(win,text='Day13',bg= background_txt ,variable=DayList[12],onvalue='Day13',offvalue='').place(x = 130, y =  70)
	c14=tk.Checkbutton(win,text='Day14',bg= background_txt ,variable=DayList[13],onvalue='Day14',offvalue='').place(x = 190, y =  70)
	c15=tk.Checkbutton(win,text='Day15',bg= background_txt ,variable=DayList[14],onvalue='Day15',offvalue='').place(x = 250, y =  70)
	c16=tk.Checkbutton(win,text='Day16',bg= background_txt ,variable=DayList[15],onvalue='Day16',offvalue='').place(x = 310, y =  70)
	c17=tk.Checkbutton(win,text='Day17',bg= background_txt ,variable=DayList[16],onvalue='Day17',offvalue='').place(x = 370, y =  70)
	c18=tk.Checkbutton(win,text='Day18',bg= background_txt ,variable=DayList[17],onvalue='Day18',offvalue='').place(x = 430, y =  70)
	c19=tk.Checkbutton(win,text='Day19',bg= background_txt ,variable=DayList[18],onvalue='Day19',offvalue='').place(x = 490, y =  70)
	c20=tk.Checkbutton(win,text='Day20',bg= background_txt ,variable=DayList[19],onvalue='Day20',offvalue='').place(x = 550, y =  70)

	c21=tk.Checkbutton(win,text='Day21',bg= background_txt ,variable=DayList[20],onvalue='Day21',offvalue='').place(x = 10 , y =  100)
	c22=tk.Checkbutton(win,text='Day22',bg= background_txt ,variable=DayList[21],onvalue='Day22',offvalue='').place(x = 70 , y =  100)
	c23=tk.Checkbutton(win,text='Day23',bg= background_txt ,variable=DayList[22],onvalue='Day23',offvalue='').place(x = 130, y =  100)
	c24=tk.Checkbutton(win,text='Day24',bg= background_txt ,variable=DayList[23],onvalue='Day24',offvalue='').place(x = 190, y =  100)
	c25=tk.Checkbutton(win,text='Day25',bg= background_txt ,variable=DayList[24],onvalue='Day25',offvalue='').place(x = 250, y =  100)
	c26=tk.Checkbutton(win,text='Day26',bg= background_txt ,variable=DayList[25],onvalue='Day26',offvalue='').place(x = 310, y =  100)
	c27=tk.Checkbutton(win,text='Day27',bg= background_txt ,variable=DayList[26],onvalue='Day27',offvalue='').place(x = 370, y =  100)
	c28=tk.Checkbutton(win,text='Day28',bg= background_txt ,variable=DayList[27],onvalue='Day28',offvalue='').place(x = 430, y =  100)
	c29=tk.Checkbutton(win,text='Day29',bg= background_txt ,variable=DayList[28],onvalue='Day29',offvalue='').place(x = 490, y =  100)
	c30=tk.Checkbutton(win,text='Day30',bg= background_txt ,variable=DayList[29],onvalue='Day30',offvalue='').place(x = 550, y =  100)

	tk.Canvas(win, bg= background_txt, width = 600, height = 0).place(x = 10, y = 140)

	tk.Label(win,
		text = '※Examination',
		bg= background_txt,
		font = ('Arial',12),
		width = 15,height=1 ,
		anchor='w').place(x = 10, y =  160)
	
	tk.Label(win,
		text = 'Word\t: ',
		bg= background_txt,
		font = ('Arial',12),
		width = 20,height=1 ,
		anchor='w').place(x = 10, y =  190)

	tk.Label(win,
		text = 'Ans\t: ',
		bg= background_txt,
		font = ('Arial',12),
		width = 20,height=1 ,
		anchor='w').place(x = 10, y =  220)

	tk.Label(win,
		text = 'Note\t: ',
		bg= background_txt,
		font = ('Arial',12),
		width = 20,height=1 ,
		anchor='w').place(x = 10, y =  250)

	tk.Label(win,
		text = 'Exp\t: ',
		bg= background_txt,
		font = ('Arial',12),
		width = 20,height=1 ,
		anchor='w').place(x = 10, y =  280)
	
	# canvas = tk.Canvas(win,width=500,height=110)
	# canvas.place(x = 90, y =  275)
	# canvas.create_rectangle(10,10,500,110)

	# ------------------------------------------------------------------------
	def callback_1(event):
		# print('T1.get():', T1.get())
		# or more universal
		# print('event.widget.get():', event.widget.get())
		# select text after 50ms
		win.after(50, select_all_1, event.widget)
	def select_all_1(widget):
		# select text
		widget.select_range(0, 'end')
		# move cursor to the end
		widget.icursor('end')


	def T2_1(event):
		with tempfile.NamedTemporaryFile(delete=True) as fp:
			tts=gTTS(text=str(str_text.get()), lang='en')
			tts.save("{}.mp3".format(fp.name))
			mixer.init()
			mixer.music.load("{}.mp3".format(fp.name))
			mixer.music.play()

	tk.Label(win,
		text = 'Speak\t:',
		bg= background_txt,
		font = ('Arial',12),
		width = 25,height=1 ,
		anchor='w').place(x = 10, y =  380)

	str_text = tk.StringVar()
	T2 = tk.Entry(win,
		bg= background_E_txt,
		font=("Helvetica",16),
		width = 50,
		textvariable = str_text)
	T2.focus_set()
	T2.place(x = 100, y =  380)
	# T2 = tk.Text(win,width= 28,height=15).place(x = 590, y =  170)
	T2.bind('<F3>',T2_1)
	T2.bind('<Control-a>', callback_1)
	# -----------------------------------------------------------------------
	tk.Label(win,
		text = 'F1 : Next , F2 : Sound, ,F3 : speak ,Enter : OK',
		bg= background_txt,
		font = ('Arial',10),
		width = 50,height=1 ,
		anchor='w').place(x = 520, y =  408)
	# cv2 = tk.Canvas(win, bg= background_txt)
	# cv2.create_rectangle(10,100,100,10,outline = background_txt)
	# cv2.pack()
	# cv2.place(x = -1, y = 404)

	win.mainloop()