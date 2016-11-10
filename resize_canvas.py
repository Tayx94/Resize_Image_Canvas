# Command from IM to execute:
# convert imgPath -background none -gravity center -extent newWidthxnewHeight imgPath

import os
import subprocess
from fnmatch import fnmatch

root 	= 'C:\Program-Files\sprite\_Sprites'
pattern = "*.png"

multipleToResizeTo = 4

imgPath 	= ''
newWidth 	= 0
newHeight 	= 0

elementCount = 0
resizedCount = 0

print
print('= START IMAGE CANVAS RESIZING =')
print('<<<--------------------------------->>>')

for path, subdirs, files in os.walk(root):
    for name in files:
		elementCount = elementCount + 1
		if fnmatch(name, pattern):
			
			resizedCount = resizedCount + 1
			
			imgPath = os.path.join(path, name)
			#print('File: ' + imgPath)
			output = subprocess.check_output("convert " + imgPath + " -ping -format \"%w\" info:", shell=True)
			newWidth = int(output)
			while (newWidth % multipleToResizeTo != 0):
				newWidth = newWidth + 1
			
			output2 = subprocess.check_output("convert " + imgPath + " -ping -format \"%h\" info:", shell=True)
			newHeight = int(output2)
			while (newHeight % multipleToResizeTo != 0):
				newHeight = newHeight + 1
				
			print('file: ' + imgPath + ' ---> new size: ' + str(newWidth) + 'x' + str(newHeight))
			
			# Calls convert IM operation - UNCOMMENT TO USE
			# subprocess.call("convert " + imgPath + " -background none -gravity center -extent " + str(newWidth) + "x" + str(newHeight) + " " + imgPath, shell=True)

print
print('Elements scanned: ' + str(elementCount))
print('Elements resized: ' + str(resizedCount))
print('<<<--------------------------------->>>')
print