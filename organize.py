
from shutil import move
from time import sleep
from glob import glob

user_path = "C:/Users/dudun/"

paths = {
	'downloads':user_path+'Downloads/',
	'documents':user_path+'Documents',
	'pictures':user_path+'Pictures/',
	'music':user_path+'Music/',
	'videos':user_path+'Videos/',
	'other scripts':user_path+'Documents/Scripts/',
	'python scripts':user_path+'Documents/Scripts/Python/',
	'java scripts':user_path+'Documents/Scripts/Java/',
	'web scripts':user_path+'Documents/Scripts/Web/',
	'minecraft files':user_path+'Documents/Minecraft/'
}

folder_to_organize = input('What folder would you like to organize? ')

if folder_to_organize.lower() in paths:
	folder_to_organize = paths[folder_to_organize.lower()]

def multiglob(path,exts): #ext, short for extension
	globbed = []
	for ext in exts:
		globbing = glob(path+'*.'+ext) #glob returns a list
		for file in globbing: #getting each item from that list and putting it on the globbed list so that it isnt a list of lists
			globbed.append(file)
	return globbed

extensions = {
	'pictures': ['png','jpeg','jpg','webp','gif','eps','bmp','raw','svg'],
	'videos': ['mp4','mkv','avi','mov','webm'],
	'music': ['mp3','ogg','m4a','wav','flac'],
	'python scripts': ['py','pyw'],
	'java scripts': ['java'],
	'web scripts': ['css','js','html'],
	'minecraft files': ['jar'],
	'documents': ['pdf','txt','docx','doc','pptx','ppt','xls','xlsx']
}

moved_files = {}

for each in extensions:
	files = multiglob(folder_to_organize, extensions[each])
	for file in files:
		moved_files[file] = paths[each]
		move(file, paths[each])

print('Moved total of',len(moved_files),'files:')
for moved_file in moved_files:
	print('Moved',moved_file,'to',moved_files[moved_file])

sleep(2)