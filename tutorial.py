from os import listdir
from os.path import isfile, join
from PIL import Image


path = '/Users/haeseong/Downloads'
results = list(filter(lambda x: x.find('.jpg') >= 0, listdir(path)))
WIDTH = 1125/2
HEIGHT = 750/2
CARD_RATIO = 1.5

for filename in results:
	file_path = join(path, filename)
	im = Image.open(file_path)
	ratio = im.size[0] / im.size[1]
	# print(im.format, im.mode, im.size[0], im.size[1], '%.3f' % ratio)

	if im.size[0] > WIDTH or im.size[1] > HEIGHT:
		if ratio > CARD_RATIO:
			scale = WIDTH / im.size[0]
		elif ratio < CARD_RATIO:
			scale = HEIGHT / im.size[1]
		else:
			scale = 1
		size_x = im.size[0] * scale
		size_y = im.size[1] * scale
		print('%d, %d' % (int(size_x), int(size_y)))
		im.thumbnail((size_x, size_y))
		im.show()
		im.save(file_path + '.thumbnail.jpg', 'JPEG')


# 1 : 1.618
# 1 : 1.778	= 16 / 9
width = 750
height = 1125


