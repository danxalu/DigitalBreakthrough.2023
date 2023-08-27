from PIL import Image
from pylab import *
from numpy import *

im = array(Image.open('0a0ba31d-baeb-4095-9835-b0801b995c0a.jpg').convert('L'))
figure()
imshow(im)
show()


def histeq(im, nbr_bins=256):
    """ Выравнивание гисгограммы полутонового изображения. """
    # получить гистограмму изображения
    imhist, bins = histogram (im.flatten(), nbr_bins, normed=True)
    cdf = imhist.cumsum() # функция распределения
    cdf = 255 * cdf / cdf[-1] # нормировать
    # использовать линейную интерполяцию сб для нахождения
    # значений новых пикселей
    im2 = interp(im.flatten(), bins[:-1], cdf)
    return im2.reshape(im.shape), cdf


im2, cdf = histeq(im)
print(im)

