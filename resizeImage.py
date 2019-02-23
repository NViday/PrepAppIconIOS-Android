# Goal : convert an svg into a png of given size 
# input = file.svg , size
# output = file.png


#!/bin/python
import re
import cairo
from PIL import Image
from resizeimage import resizeimage 
from gi.repository import rsvg

#Checking File Type 

# Input 
# filename : ( str ) " test.png "
# regex    : ( str ) ".[Pp][Nn][Gg] " 

# Output
#            (bool) true / false 
   
def checkExtension(filename, regex):
	pattern = re.compile(regex)
	return pattern.search(filename)




def IsSVG(filename):
	return checkExtension(filename, ".[Ss][Vv][Gg]")


def IsPNG(filename):
	return checkExtension(filename, ".[Pp][Nn][Gg]")

#To Name resized Picture

# Input
# folder     : (str) ".../folder/"
# iconType   : (str) " launcher " 
# size       : (str) " 200x300 "
# res        : (str) " 2x"

#Output      
# newName    : (str)  ".../folder/ic-launcher-200x300@2x"

def GetName(folder,iconType, size, resolution):
	return folder+"ic-"+iconType+"-"+size+resolution


#To Resize  Image 
def ResizeImageSVG(filename,name,size):
	
	dimension = size.split('x')

	width = int(dimension[0])

	height = int( dimension[1] )  

	image = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)  
	
	context = cairo.Context(image)

	handle = rsvg.Handle(filename) 

	handle.render_cairo(context) 
	
	image.write_to_png(name+".png")

	

def ResizeImagePNG(filename,name, size):

	dimension = size.split('x')

	width = int( dimension[0] )

	height = int( dimension[1] )

	with open(filename, 'r+b') as f:

		with Image.open(f) as image : 

			resizedImage = resizeimage.resize_cover(image, [ width, height])

			resizedImage.save(name+".png", image.format)  




def PrepIcon( filename, icFoler, icType, size, resolution) :
	
	#name of the output file
	newName = GetName( icFolder, icType, size, res)
	
	# check if svg / png 
	if IsSVG(filename):
 
		resizeImageSVG(filename, newName, size)

	elif IsPNG(filename):

		resizeImagePNG( filename, newName, size)

	else :

		print("REQUIRED FORMAT: PNG ,  SVG") 

 
def PrepIcons(folder, filename, iconType, sizes, resolutions) :

	for index in range(0, sizes.len()):
		
		size = sizes[index]

		resolution = resolutions[index]

		PrepIcon(filename, folder, iconType, size, resolution)


