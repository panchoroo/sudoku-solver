# A well constructed Su Doku puzzle has a unique solution and can be solved by logic, although it may be necessary 
# to employ "guess and test" methods in order to eliminate options (there is much contested opinion over this).
#  The complexity of the search determines the difficulty of the puzzle; the example above is considered easy 
#  because it can be solved by straight forward direct deduction.

# The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), contains fifty different Su Doku puzzles
#  ranging in difficulty, but all with unique solutions (the first puzzle in the file is the example above).

# By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution 
# grid; for example, 483 is the 3-digit number found in the top left corner of the solution grid above.

print 'derp'
sudokuText= "p096_sudoku.txt"
def loadSuccesses():
	inFile = open(sudokuText, 'r')
	line = inFile.readline()
	sudokuList = []
	while line:
		if line[0] == 'G':
			newPuzzle = [];
			count = 0;
		if count > 0:
			newPuzzle.append(line[:9]);
		count += 1
		if count >= 8:
			sudokuList.append(newPuzzle);
		line = inFile.readline()
	inFile.close()
	return sudokuList

# puzzleList = loadSuccesses()
# when it works, load all 50 puzzles, for now, just the first one
puzzleList = [['003020600', '900305001', '001806400', '008102900', '700000008', '006708200', '002609500', '800203009', '005010300']];
# print puzzleList;

solutionsList = [];
for p in puzzleList:
	# iterate through each puzzle from the text file
	startIndex = 0;
	workingPuzzle = p;
	possiblySolved = [];
	possibleDigits = '123456789';
	for line in workingPuzzle:
		thisLineDigits = '';
		for d in possibleDigits:
			if d not in line:
				thisLineDigits += d;
		# print thisLineDigits;
		for digit in line:
			# print digit
			if digit == '0':
				line = line[:line.index(digit)] + thisLineDigits[startIndex] + line[line.index(digit)+1:]
				# print line
				# line[line.index(digit)] = ;
				thisLineDigits = thisLineDigits[1:];
				# what happens when it finds an error?  maybe inc start index by 1? 
				# or shuffle digits around? but dont let start digit end up in same place? 
		# print line;
		possiblySolved.append(line);
	# print possiblySolved;
	possiblySolved=['123527689', 
	'456365781', 
	'789856479', 
	'348152967', 
	'712345698', 
	'136748259', 
	'132649578', 
	'814253679', 
	'245617389'];

	def gridChecker(rowStart, colStart):
		gridNums = '';
		count = 0;
		line = possiblySolved[rowStart];
		while count < 9:
			print line;
			colCount = 0;
			if count == 3:
				line = possiblySolved[rowStart+1];
				colCount = 0;
			elif count == 6: 
				line = possiblySolved[rowStart+2];
				colCount = 0;
			digit = line[colStart+colCount];
			if digit in gridNums:
				print digit, gridNums;
				# return False;
			else:
				gridNums += digit;
			count += 1;
			colCount += 1;
		print gridNums;
		return True;

		# 
		# line2 = possiblySolved[rowStart+1];
		# line3 = possiblySolved[rowStart+2];


		# gridNums += line1[colStart];
		# 	if line1[colStart+1] not in gridNums:
		# 		gridNums += 



	gridRowIndex = 0;
	while gridRowIndex < 7:
		# check each 3x3 grid for numbers 1-9, no repeats
		gridColIndex = 0;
		while gridColIndex < 7:
			if gridChecker (gridRowIndex, gridColIndex):
				print 'yeah'
			else:
				print 'naw'
			

			gridColIndex += 3;
		gridRowIndex += 3;



	# for solvedLine in possiblySolved:
		# for solvedDigit in solvedLine:
			# check each digit of each line to see if this possible solution has any errors
			# check columns for > 1 of same digit, (rows should already be error-free byt design)








# 	def getGrid(index):
# 		firstGrid = [0,1,2];
# 		secondGrid = [3,4,5];
# 		thirdGrid = [6,7,8];
# 		if index in firstGrid:
# 			return firstGrid;
# 		elif index in secondGrid:
# 			return secondGrid;
# 		elif index in thirdGrid:
# 			return thirdGrid;
# 		else:
# 			print('something has gone terribly, terribly wrong');

# 	currentGrid = [0,1,2];
# 	checkIndex = 0;

# 	def rowDigitChecker(digit):
# 		noNew = True;
# 		def currentCheck(line):	
# 			return line.index(digit);
# 			# checkIndex = line.index(digit);
# 			# if workingPuzzle.index(line) not in currentGrid:
# 			# 	newGrid = getGrid(workingPuzzle.index(line));
# 			# return newGrid;

# 		def currentGridChecker(line, grid):
			
# 			newGrid = grid;
# 			# checkIndex = line.index(digit);
# 			if workingPuzzle.index(line) not in grid:
# 				newGrid = getGrid(workingPuzzle.index(line));
# 			return newGrid;

# 		line = 0;
# 		currentGrid = getGrid(line);

# 		lineIndex = 0;
# 		while lineIndex < 7:
# 			workingLine = workingPuzzle[lineIndex]
# 			first = [digit in workingLine, 0];
# 			second = [digit in workingPuzzle[workingPuzzle.index(workingLine)+1], 1];
# 			third = [digit in workingPuzzle[workingPuzzle.index(workingLine)+2], 2];
# 			found = [first, second, third];
# 			successes = [f[1] for f in found if f[0]]
# 			# print ('successes', successes)

# 			if len(successes) == 2:
# 				print 'heyo'
# 				# figure out which two column grids have been done already, 
# 				# check that rows' grids' 0's
# 				# Get one that's not used and check other rows at 0's indices 
# 				line1 = workingPuzzle[workingPuzzle.index(workingLine)+successes[0]];
# 				index1 = line1.index(digit);
# 				grid1 = getGrid(index1);

# 				line2 = workingPuzzle[workingPuzzle.index(workingLine)+successes[1]];
# 				index2 = line1.index(digit);
# 				grid2 = getGrid(index2);

# 				if (0 in grid1 or 0 in grid2 and (3 in grid1 or 3 in grid2)):
# 					grid3 = [6,7,8];
# 				elif (0 in grid1 or 0 in grid2 and (6 in grid1 or 6 in grid2)):
# 					grid3 = [3,4,5];
# 				else:
# 					grid3 = [0,1,2];

# 				print ('lines',workingPuzzle.index(line1), workingPuzzle.index(line2))
# 				if (successes[1] - successes[0] == 2):
# 					line3 = workingPuzzle[workingPuzzle.index(workingLine)+1];
# 				elif (workingPuzzle.index(line1) == 0 or workingPuzzle.index(line1) == 3 or workingPuzzle.index(line1) == 6):
# 					line3 = workingPuzzle[workingPuzzle.index(workingLine)+2];
# 				else:
# 					line3 = workingPuzzle[workingPuzzle.index(workingLine)];
				
# 				# searching line 3 w/i grid 3 for 0's to find available
# 				# comparing column at indicies of 0s to see if we can rule any out
# 				print ('3s ', line3, grid3);
# 				zeroes = []
# 				for g in grid3:
# 					print line3[g]
# 					# maybe filter grid3 somehow?
# 					if (str(line3[g]) == '0'):
# 						zeroes.append(g);
						
# 				matches = [];
# 				for z in zeroes:
# 					# print ('z? ',z)
# 					for testLine in workingPuzzle:
# 						if testLine[z] == digit:
# 							zeroes.remove(z);
# 				if len(zeroes) == 1:
# 					print 'YEAY'
# 					# print (line3, digit, zeroes[0])
# 					noNew = False;

# 					newLine = line3[:zeroes[0]] + str(digit) + line3[zeroes[0]+1:];
# 					# newLine[zeroes[0]] = str(digit);
# 					workingPuzzle[workingPuzzle.index(line3)] = newLine;

# 			lineIndex += 3;
# 		return noNew;


# 	done = False;
# 	while not done:
# 		allDone = True;
# 	 	for digit in possibleDigits:
# 	 		if rowDigitChecker(digit) == False:
# 	 			allDone = False;
# 	 	if allDone == True:
# 	 		done = True;

# 	# rowDigitChecker(possibleDigits[0]);

# print workingPuzzle;

