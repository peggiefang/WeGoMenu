from tkinter import *
#import tkinter as tk



win = Tk()
win.title('WeGo Menu')
win.geometry("400x400+200+200")
win.minsize(width=400,height=200)
win.maxsize(width=800,height=600)
win.iconbitmap("/Users/chiehfang/Desktop/Menu/ico.ico")
win.config(bg="white")
# win.attributes('-alpha',0.8)


item_show = Label(text= "",bg='white')
item_show.pack(padx=20, pady=10)

price_show = Label(text= "",bg='white')
price_show.pack(padx=20, pady=15)

items = []
entry = []


def item_price(entry,item):
	menu = {'肉燥乾拌麵':15,'漁夫海鮮烏冬':25,'台灣紅燒牛肉麵':25,'奶油培根白醬義大利麵':28,'鮮蝦白醬義大利麵':32,'台灣肉燥飯':15,'台灣滷肉飯':16,'台灣雞肉飯':16,'台灣香腸飯':16,'蝦仁炒飯':22,'漁夫海鮮泡飯':20,'南洋椰香咖哩飯':22,'台灣三杯雞飯':22,'台灣紅燒牛肉飯':25,'奶油培根白醬飯':28,'鮮蝦白醬飯':32,'招牌冰花煎餃':15,'牛肉湯餃':20,'洛神花茶':6,'冬瓜茶':6,'檸檬冬瓜茶':8,'冬瓜鮮奶':10,'黑糖珍珠鮮奶':12}
	items.insert(-1,item)
	entry.insert(-1,menu[item])

	item_show.config(text = items )
	print(entry)

def cal(entry):
	price = str(sum(entry))
	price_show.config(text = "price: " + price)



n01 = Button(text='牛肉麵',command = lambda : item_price(entry,'牛肉麵'))
n01.pack(padx=20)

n02 = Button(text='滷肉飯',command = lambda : item_price(entry,'滷肉飯'))
n02.pack(padx=20)

n03 = Button(text='冬瓜鮮奶',command = lambda : item_price(entry,'冬瓜鮮奶'))
n03.pack(padx=20)

n04 = Button(text='冬瓜鮮奶',command = lambda : item_price(entry,'冬瓜鮮奶'))
n04.pack(padx=20)


count = Button(text='結帳',command = lambda : cal(entry))
count.pack(padx=20)

quit = Button(text='結束視窗',command = win.destroy).pack(padx=20)

btn = Button()
# img =("path")
# btn.confing(image = img)

win.mainloop()










