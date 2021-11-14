from nonebot import on_command
from nonebot.rule import to_me
from nonebot.adapters.cqhttp import Bot, MessageEvent, Message
import httpx
from PIL import Image
import cv2
import numpy as np

CAT_API_URL = 'https://api.thecatapi.com/v1/images/search'

TEST_IMG_PATH = '/assets/images/cat-test.jpg'
LUMU_IMG_PATH = '/assets/images/lumu.png'
OUTPUT_IMG_PATH = '/assets/images/cat.png'
DETECTOR_PATH = '/assets/catface_detector.xml'

cat_request = on_command('来点猫图', to_me())

@cat_request.handle()
async def _(bot: Bot, event: MessageEvent):
    async with httpx.AsyncClient() as client:
        r = await client.get(CAT_API_URL)
        url = r.json()[0]['url']
        pic = await client.get(url)

        cat = Image.open(pic).convert('RGBA')
        lumu = Image.open(LUMU_IMG_PATH).convert('RGBA')
        make_meme(cat, lumu)
        cat.save(OUTPUT_IMG_PATH)

        msg = Message(f'[CQ:image,file=file://{OUTPUT_IMG_PATH}]')
        await cat_request.finish(msg)

cat_test = on_command('测试猫图', to_me())

@cat_test.handle()
async def _(bot: Bot, event: MessageEvent):
    cat = Image.open(TEST_IMG_PATH).convert('RGBA')
    lumu = Image.open(LUMU_IMG_PATH).convert('RGBA')
    make_meme(cat, lumu)
    cat.save(OUTPUT_IMG_PATH)

    msg = Message(f'[CQ:image,file=file://{OUTPUT_IMG_PATH}]')
    await cat_test.finish(msg)

def make_meme(cat: Image, lumu: Image):
    # Convert to greyscale
    tmp = cat.convert('L')
    tmp = np.array(tmp)

    # Detect cat faces
    catface_cascade = cv2.CascadeClassifier(DETECTOR_PATH)
    cat_faces = catface_cascade.detectMultiScale(tmp, scaleFactor=1.3, minNeighbors=5, minSize=(20,20))

    # Draw Lumu
    for (i, (x, y, w, h)) in enumerate(cat_faces):
        # Resize Lumu
        (a, b) = lumu.size
        if a/w > b/h:
            size = (int(a / b * h * 1.5), int(h * 1.5))
        else:
            size = (int(w * 1.5), int(b / a * w * 1.5))

        src = lumu.resize(size)
        pos = (int(x + w/2 - size[0] / 2), int(y + h/2 - size[1] / 2 ))
        r, g, b, a = src.split()
        cat.paste(src, pos, mask=a)

    cat.thumbnail((680, 680))