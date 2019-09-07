import requests
from os import getcwd, chdir, remove
import zipfile

version='https://raw.githubusercontent.com/MrUrica/game/master/version/last_version'
url_newver='https://raw.githubusercontent.com/MrUrica/game/master/version/'
ver=[1,0,0]

def getVersion():
	global ver
	num_ver=str(ver[0])+'.'+str(ver[1])+'.'+str(ver[2])
	return num_ver

def checkUpdates():
	global version
	global ver
	global url_newver

	file_found=False
	try:
		r=requests.get(version)
		file_found=True
	except:
		print('Pas de connexion Internet !')

	if file_found:
		with open('test.txt','wb') as f:
			f.write(r.content)

		del r
		file_found=False

		file=open('test.txt','r')
		file_text=file.read()

		file.close()
		remove('test.txt')

		file_text=file_text.split(':')
		new_version=file_text[1]
		del file_text
		del file

		nb=new_version.split('.')
		nb[2]=int(nb[2])
		nb[2]=str(nb[2])
		if int(nb[0]) > ver[0] or int(nb[1]) > ver[1] or int(nb[2]) > ver[2]:
			print('Nouvelle version disponible !\nVersion: ', new_version)
			new_ver=nb[0]+'.'+nb[1]+'.'+nb[2]+'/recap.txt'
			url_newver='https://raw.githubusercontent.com/MrUrica/game/master/version/'+str(new_ver)
			downloadUpdate()

		else:
			print('Pas de nouvelle version.')

def downloadUpdate():
	global url_newver
	file_found=False

	try:
		r=requests.get(url_newver)
		file_found=True
	except:
		print('Erreur')

	if file_found:
		with open('recap.txt','wb') as f:
			f.write(r.content)
		del r

		file=open('recap.txt','r')
		updates=file.read()    
		updates=updates.split('\n')

		for u in range(0,len(updates)):
			ligne=updates[u]
			ligne=ligne.split('>>')

			try:
				r=requests.get(ligne[1])
			except:
				file_found=False

			if not file_found:
				if len(updates)-1==u:
					print('Mise à jour effectuée !')
				else:
					print('Erreur dans le téléchargement !')

				break

			else:
				if ligne[2]==' ':
					with open(ligne[0],'wb') as f:
						f.write(r.content)

					if '.zip' in ligne[0]:
						with zipfile.ZipFile(ligne[0],'r') as zp:
							zp.extractall()

						remove(ligne[0])


				else:
					with open(ligne[2]+ligne[0],'wb') as f:
						f.write(r.content)

					if '.zip' in ligne[0]:
						with zipfile.ZipFile(ligne[2]+ligne[0],'r') as zp:
							zp.extractall(ligne[2])

						remove(ligne[2]+ligne[0])

				del r

checkUpdates()
