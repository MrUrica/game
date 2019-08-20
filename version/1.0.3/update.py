import requests
from os import getcwd, chdir, remove

version='https://raw.githubusercontent.com/MrUrica/game/master/version/last_version'
ver=[1,0,3]

def checkUpdates():
	global version
	global ver

	file_found=False
	try:
		r=requests.get(version)
		file_found=True
	except:
		print('Pas de connexion Internet !')

	if file_found:
		with open('test.txt','wb') as f:
			f.write(r.content)

		file=open('test.txt','r')
		file_text=file.read()

		file.close()

		file_text=file_text.split(':')
		new_version=file_text[1]
		del file_text

		nb=new_version.split('.')
		if int(nb[0]) > ver[0] or int(nb[1]) > ver[1] or int(nb[2]) > ver[2]:
			print('Nouvelle version disponible !\nVersion: ', new_version)
			ver=[int(nb[0]),int(nb[1]),int(nb[2])]
			print(ver)
		else:
			print('Pas de nouvelle version.')

checkUpdates()
