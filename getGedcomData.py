# DHRUVIN DINESHBHAI PATEL
# CWID: 10420356
# dpate78@stevens.edu
# CS/SSW 555

def getData():
	l=[]
	path = "dhruvinPatel.ged"	#path to the gedcom file
	validTags = ['NAME', 'SEX', 'BIRT', 'DEAT', 'FAMC', 'FAMS', 'MARR', 'HUSB', 'WIFE', 'CHIL', 'DIV', 'DATE', 'HEAD','TRLR', 'NOTE']
	additionalValidTags = ['INDI', 'FAM']
	inputFileHandler = open(path, "r")
	outputFileHandler = open("output.txt","w")
	for line in inputFileHandler:
		l = line.split()
		if l[0] == "NOTE":
			continue 
		elif l[1] in validTags:
			print(' '.join(l[0:]))
			outputFileHandler.write(' '.join(l[0:]))
		elif len(l) == 3 and l[2] in additionalValidTags:
			print(' '.join(l[0:]))
			outputFileHandler.write(' '.join(l[0:]))
		else:
			print("Invalid Tag")
			outputFileHandler.write("Invalid Tag")
		outputFileHandler.write('\n')
	inputFileHandler.close()
	outputFileHandler.close()


#print allLinesToList()
if __name__ == '__main__':
	getData()