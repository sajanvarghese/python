x=int(input('enter the limit of rows: '))
i=1
while i<=x:
	
	j=x-i
	while j > 0:
		print(' ',end='')
		j-=1
		
	s=1
	while s<=i:
		print('*',end=' ')
		s=s+1
		
	print()
	i=i+1
