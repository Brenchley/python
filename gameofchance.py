import random
def rolldie():
	die1=random.randrange(1,7)
	die2=random.randrange(1,7)
	worksum=die1+die2
	print'The player rolled %d + %d = %d'%(die1,die2,worksum)

	return worksum

sum=rolldie()
if sum==7 or sum==11:
	gamestatus='WON'
elif sum==2 or sum==3 or sum==12:
	gamestatus='LOST'
else:
	gamestatus='CONTINUE'
	mypoints=sum
	print'Your points are: ',mypoints
while gamestatus=='CONTINUE':
	sum=rolldie()
	if sum== mypoints:
		gamestatus='WON'
	elif sum==7:
		gamestatus='LOST'
if gamestatus=='WON':
	print'Player wins'

if gamestatus=='LOST':
	print'Player losses'
	