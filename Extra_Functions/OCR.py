import easyocr
import os
from PIL import Image


reader = easyocr.Reader(['ru', 'en'])
directory = '/Users/dmitriinizovcev/Downloads/train_dataset_Датасет/tg/images' # Ваша директория картинок
for filename in os.listdir(directory)[:4]: # Первые 10 экзэмпляров
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        img = Image.open(f)
        black_and_white = img.convert("L")
        black_and_white.save("filename.png")
        text = reader.readtext("filename.png", detail=0, paragraph=True)
        with open("datatext.txt", "a") as o:
            o.write('Начало данных')
            for element in text:
                o.write(f'{element}, ')
            o.write('Конец данных')
