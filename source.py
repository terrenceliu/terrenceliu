from jinja2 import Template
import os
ROOT_PATH = 'images/'

def create_section(href, name):
	return {'href': href, 'name': name}


def getFile(section_path):
	"""
	:param root_path:
	:param section_path:
	:return: filenames
	"""
	files = []
	if section_path:
		path = os.path.join(ROOT_PATH, section_path)
	else:
		path = ROOT_PATH
	for file in os.listdir(path):
		if file.endswith('.jpg'):
			files.append(file)
		# files.append(file)
		# print type(file)
	return files

def setImg(section_path):
	reg_files = getFile(section_path)
	imgs = []
	for ele in reg_files:
		href = os.path.join(ROOT_PATH, section_path, ele)
		thumbnail = os.path.join(ROOT_PATH, section_path, 'thumbnails', ele)
		img = {'href': href, 'thumbnail': thumbnail, 'height': 175}
		imgs.append(img)
	return imgs

def test():
	with open('template.html', 'r') as f:
		tmp = Template(f.read())
	
	sec_title = ['SF']
	pg_title = [i.lower().replace(' ', '_') for i in sec_title]
	secs = []
	
	# Get section title
	for sec in sec_title:
		sec = sec
		href = sec.lower().replace(' ', '_') + '.html'
		secs.append(create_section(href, sec))
	
	# Render index
	with open('index.html', 'w') as f:
		imgs = getFile('index')
		html = tmp.render(
			sections = secs
		)
		f.write(html)
	
	# Render page
	for page in pg_title:
		fname = page +'.html'
		imgs = setImg(page)
		with open(fname, 'w') as f:
			html = tmp.render(
				sections = secs,
				items = imgs
			)
			f.write(html)
	
	

test()
