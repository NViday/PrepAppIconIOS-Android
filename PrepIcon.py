#!/bin/python 

import os
import re
from AndroidIconPrep import *
from iOSIconPrep import *


# input :  -[clt] [filename]


if __name__=="__main__":

	# validate arguments 

	filename = sys.argv[2]
	
	if os.path.isfile(filename) :

		action = sys.argv[1]

		context = re.compile("-[Cc]")

		launcher = re.compile("-[Ll]")

		tab  = re.compile("-[Tt]")

		if context.search(action):
			name = ""

			if(sys.argv.len() >= 3) :
				name = sys.argv[3]

			iOSPrepContextualIcon(filename, name)
			AndroidPrepContextualIcon(filename, name) 
			break

		elif  launcher.search(action):

			iOSPrepLauncher( filename)
			AndroidPrepLauncher( filename)
			break


		elif tab.search(action):
			name = ""

			if(sys.argv.len() >= 3) :
			        name = sys.argv[3]

			iOSPrepTabIcon(filename, name)
			AndroidPrepTabIcon(filename, name)
			break
		else:

			print ( "wrong command!")
			print ( "     -C , -c : prep for contextual icons") 
			print ( "     -L , -l : prep for launcher icons  " )
			print ( "     -T , -t : prep for tab icons " ) 

	else : 

		print ( "ERROR : Incorrect File") 
	
	





