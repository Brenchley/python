import glob


path = '/home/brenchley/Videos/series/*'

files= glob.glob(path)

for file in files:     
   print file