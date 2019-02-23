# Goal : Resize an high-resolution  Image to fit Android Icon standard 
# Follwoing Android Stnadard 
# mdpi    ==> 1x 
# hdpi    ==> 1.5x 
# xhdpi   ==> 2x
# xxhdpi  ==> 3x
# xxxhdpi ==> 4x
   
#!/bin/python
import os
import errno
from resizeImage import *



path = os.getcwd()
print(path) 

def createAndroidFolder(folderPath):
	try : 
		os.makedirs(folderPath+"/Android/")

	except FileExistError:
		pass

	return folderPath
 


def AndroidPrepNotifIcon(filename):

	iconType = "notification"
	
	folder = createAndroidFolder(iconType)

	resolutions = ["-mdpi","-hdpi", "-xhdpi", "-xxhdpi", "-xxxhdpi"]

	sizes = ["24x24","36x36","48x48", "72x72", "96x96"]

	PrepIcons(folder, filename, iconType, sizes, resolutions)



def AndroidPrepLauncher( filename) :

	iconType = "launcher"

	# create an icon folder
	folder = createAndroidFolder(iconType)

	print (folder)

	resolutions = ["-mdpi","-hdpi", "-xhdpi", "-xxhdpi", "-xxxhdpi" "-GooglePlay"]

	sizes = ["48x48", "72x72", "96x96", "144x144", "192x192", "512x512"] 	 

	PrepIcons(folder, filename, iconType, sizes, resolutions) 
	
	AndroidPrepNotifIcon(filename)




	
def AndroidPrepTabIcon(filename, name) :

	iconType = "tab-"+name
	
	folder = createAndroidFolder(iconType  )
	
	print(folder)

	resolutions = ["-mdpi","-hdpi", "-xhdpi", "-xxhdpi", "-xxxhdpi" ]

	sizes = ["32x32", "48x48", "64x64", "96x96", "128x128"]

	PrepIcons(folder, filename, iconType, sizes, resolutions) 




def AndroidPrepContextualIcon(filename, name):
	
	iconType = "context-"+ name

	folder = createAndroidFolder(iconType)

	print(folder)

	resolutions = ["-mdpi","-hdpi", "-xhdpi", "-xxhdpi", "-xxxhdpi" ]

	sizes = ["16x16", "24x24", "32x32", "48x48", "64x64"]

	PrepIcons(folder, filename, iconType, sizes, resolutions) 



 
