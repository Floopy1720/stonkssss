from fastapi import FastAPI
from fastapi.responses import FileResponse
from PIL import Image, ImageFont, ImageDraw
stonk = Image.open('stonk orginal.png')
draw_stonk = ImageDraw.Draw(stonk)
font = ImageFont.truetype('Roboto-Medium.ttf', 150)
app = FastAPI()

db = "None"

@app.get('/stonk/')
def index(text: str):
	draw_stonk.text((1250,900), text, font = font, fill='white')
	stonk.save('stonk.png')
	return FileResponse('stonk.png')

@app.get('/cities')
def get_cities():
	return db

#@app.get('/cities/{city_id}')


@app.post('/cities')
def postci(city):
	db = city
	pass
#@app.delete('/cities')