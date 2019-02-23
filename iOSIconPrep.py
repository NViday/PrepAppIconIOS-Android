# Goal : Resize an high-resolution  Image to fit iOS Icon standard 
# Follwoing Android Stnadard 
# @ 1x 
# @ 2x 
# @ 3x
   
#!/bin/python
import os
import errno
from resizeImage import *



path = os.getcwd()
print(path) 

def createIOSFolder(folderPath):
	try : 
		os.makedirs(folderPath + "/iOS/")

	except FileExistError:
		pass

	return folderPath
 


def iOSPrepLauncher( filename) :

	iconType = "launcher"

	# create an icon folder
	folder = createAndroidFolder(iconType)

	print (folder)

	resolutions = ["@2x","@2x", "@3x", "@2x", "@3x", "@3x", "@2x", "@2x", "@3x", "AppStore"]

	sizes = ["40x40", "58x58", "60x60","80x80","87x87", "120x120", "152x152", "167x167","180x180", "1024x1024"] 	 

	PrepIcons(folder, filename, iconType, sizes, resolutions) 
	



	
def iOSPrepTabIcon(filename, name) :

	iconType = "tab-"+name
	
	folder = createAndroidFolder(iconType)
	
	print(folder)

	resolutions = ["square-comp@2x","circle-comp@2x", "square-reg@2x", "circle-reg@2x", "square-comp@3x", "circle-comp@3x", "square-reg@3x", "circle-reg@3x"  ]

	sizes = ["34x34","36x36", "46x46", "50x50", "51x51" , "54x54",  "69x69", "75x75"]

	PrepIcons(folder, filename, iconType, sizes, resolutions) 




def iOSPrepContextualIcon(filename, name):
	
	iconType = "context-"+ name
	
	folder = createAndroidFolder(iconType)

	 resolutions = ["square-comp@2x","circle-comp@2x", "square-reg@2x", "circle-reg@2x", "square-comp@3x", "circle-comp@3x", "square-reg@3x", "circle-reg@3x"  ]


	 sizes = ["34x34","36x36", "46x46", "50x50", "51x51" , "54x54",  "69x69", "75x75"]

	PrepIcons(folder, filename, iconType, sizes, resolutions) 



 
