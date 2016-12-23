#!/usr/bin/python2.7
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import random


class ImageCreator:


    base_image = None
    text_image = None
    height = None
    width = None
    rotate = None
    r, g, b = None, None, None
    fonts = {}

    def __init__(self):
        self.load_fonts()

    def create(self, text, difficulty):
        self.base_image = self.createBaseImage(text, int(difficulty))
        base_draw = ImageDraw.Draw(self.base_image)
        self.plantText(text, int(difficulty))
        self.base_image.save("current-img.png")


    def load_fonts(self):
        self.fonts['0'] = ImageFont.truetype("/usr/share/fonts/OTF/C059-Roman.otf", 50)
        self.fonts['1'] = ImageFont.truetype("/usr/share/fonts/OTF/P052-BoldItalic.otf", 50)
        self.fonts['2'] = ImageFont.truetype("/usr/share/fonts/OTF/NimbusMonoPS-BoldItalic.otf", 50)
        self.fonts['3'] = ImageFont.truetype("/usr/share/fonts/OTF/Z003-MediumItalic.otf", 50)
        self.fonts['4'] = ImageFont.truetype("/usr/share/fonts/OTF/SyrCOMJerusalemOutline.otf", 44)

    def createBaseImage(self, text, difficulty):
        self.width, self.height = self.fonts[str(difficulty)].getsize(text)
        
        if difficulty == 0:
            image = Image.new('RGBA', (self.width + 30, self.height + 20), (255, 255, 255))
        elif difficulty == 1:
            image = Image.new('RGBA', (self.width + 30, self.height + 20), (255, 255, 255))
        elif difficulty == 2:
            image = Image.new('RGBA', (self.width + 30, self.height + 20), (random.randint(160,250), random.randint(160,250), random.randint(160, 250)))
        elif difficulty == 3:
            self.r = random.randint(30, 255)
            self.g = random.randint(30, 255)
            self.b = random.randint(30, 255)
            image = Image.new('RGBA', (self.width + 30, self.height + 20), (self.r, self.g, self.b))
        elif difficulty == 4:
            self.r = random.randint(40, 255)
            self.g = random.randint(40, 255)
            self.b = random.randint(40, 255)
            self.rotate = random.randint(10, 60)
<<<<<<< HEAD
            image = Image.new('RGBA', (self.width + 30, int(self.height + self.width * self.rotate * 0.02 + 20)), (self.r, self.g, self.b))
=======
            image = Image.new('RGBA', (self.width + 30, int(self.height + self.width * self.rotate * 0.02)), (self.r, self.g, self.b))
>>>>>>> 729b79eb9de8ac0ab408bc8baa9f01db5fea970c

        return image

    def plantText(self, text, difficulty):
        width, height = self.fonts[str(difficulty)].getsize(text)
<<<<<<< HEAD
        self.text_image = Image.new('RGBA', (width + 30, height + 30), (255, 255, 255, 0))
=======
        self.text_image = Image.new('RGBA', (width, height), (255, 255, 255, 0))
>>>>>>> 729b79eb9de8ac0ab408bc8baa9f01db5fea970c
        draw = ImageDraw.Draw(self.text_image)
        if difficulty == 0:
            draw.text((0,0), text=text, font=self.fonts[str(difficulty)], fill=(0, 0, 0))
        elif difficulty == 1:
            draw.text((0,0), text=text, font=self.fonts[str(difficulty)], fill=(random.randint(40, 160), random.randint(40, 160), random.randint(40, 160)))
        elif difficulty == 2:
            draw.text((0,0), text=text, font=self.fonts[str(difficulty)], fill=(random.randint(0, 155), random.randint(0, 155), random.randint(0, 155)))
        elif difficulty == 3:
            draw.text((0,0), text=text, font=self.fonts[str(difficulty)], fill=(self.r - random.randint(0, 30), self.g - random.randint(0, 30), self.b - random.randint(0, 30)))
        elif difficulty == 4:
            draw.text((0,0), text=text, font=self.fonts[str(difficulty)], fill=(self.r - random.randint(0, 40), self.g - random.randint(0, 40), self.b - random.randint(0, 40)))
            minus_or_plus = random.randint(0, 1)
            if minus_or_plus == 0:
                self.text_image = self.text_image.rotate(self.rotate, expand=1)
            else:
                self.text_image = self.text_image.rotate(-self.rotate, expand=1)

        
        px, py = 10, 10
        sx, sy = self.text_image.size
        self.base_image.paste(self.text_image, (px, py, px+sx, py+sy), self.text_image)

