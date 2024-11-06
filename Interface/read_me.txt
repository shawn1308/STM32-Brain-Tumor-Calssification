-----------Lancer l'interface---------------

- Prérequis : 
	- pip install pyqt5-tools
	- pip install pillow
	- pip install numpy
	- pip install pyserial

- Ouvrez terminal ou CMD dans le dossier
- Commande : "python image_sender.py"
- Connecter la carte stm32 :
	- choisir port COMxx
	- BAUD : 115200
	- DATA : 8
	- STOP : 1
	- PARITY : NONE
	puis CONNECT -> si STATUS passe à CONNECTED, la connection est établit.

- Choisir l'image en appuyant BROWSE puis SEND.
- La prédiction s'affiche sur <OUTPUT> et la connexion sera interrompue.
- La connexion est à rétablir à chaque fois.

%------ possiblité de lancer depuis vs code ou spyder 
(Placer dans le dossier avant de lancer le script car les images sh.jpg et re_im.jpg sont utilisé dans l'interface).

%------ J'ai effectué une conversion .py vers .exe ( fichier .exe fait 50mo)
