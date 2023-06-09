import webbrowser, time

url = input("Ссылка на видео>>")
while True:
	try:
		dur = int(input("Время просмотра>>"))
		break
	except:
		print("Введите число!")
while True:
	try:
		wtc = int(input("Коло-во просмотров>>"))
		break
	except:
		print("Введите число!")

for i in range(wtc):
	webbrowser.open_new(url)
	time.sleep(dur)