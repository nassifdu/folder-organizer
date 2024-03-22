
from shutil import move
from time import sleep
from glob import glob
import tkinter as tk
import customtkinter as ctk

root = ctk.CTk()
root.geometry('640x360')
root._set_appearance_mode('system')

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

selected_folder = None
folder_textbox = ctk.CTkTextbox(master=root,height=10,width=450,state='disabled')
folder_textbox.place(relx=0.62,rely=0.1,anchor='center')

moved_files_textbox = ctk.CTkTextbox(master=root,height=200,width=600,state='disabled')
moved_files_textbox.place(relx=0.5,rely=0.6,anchor='center')

def select_folder(): 
    global selected_folder
    selected_folder = ctk.filedialog.askdirectory()+'/'
    folder_textbox.configure(state='normal')
    folder_textbox.delete("0.0", "end")
    folder_textbox.insert('0.0',selected_folder)
    folder_textbox.configure(state='disabled')

folder_select_button = ctk.CTkButton(master=root,text='Select folder',command=select_folder)
folder_select_button.place(relx=0.14,rely=0.1,anchor='center')

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

def multiglob(path,exts): #ext, short for extension
	globbed = []
	for ext in exts:
		things = glob(path+'*.'+ext) #glob returns a list
		for thing in things: #getting each item from that list and putting it on the globbed list so that it isnt a list of lists
			globbed.append(thing)
	return globbed

moved_files = {}

def organize_folder():
	if selected_folder is not None:
		moved_files_textbox.configure(state='normal')
		for each in extensions:
			files = multiglob(selected_folder, extensions[each])
			for file in files:
				moved_files[file] = paths[each]
				move(file, paths[each])
				moved_files_textbox.insert('0.0','Moved '+file+' to '+paths[each]+'\n')
		moved_files_textbox.insert('0.0','Moved total of '+str(len(moved_files))+' files.\n')
		moved_files_textbox.configure(state='disabled')

organize_button = ctk.CTkButton(master=root,text='Organize folder',command=organize_folder,width=600)
organize_button.place(relx=0.5,rely=0.23,anchor='center')

	

root.mainloop()