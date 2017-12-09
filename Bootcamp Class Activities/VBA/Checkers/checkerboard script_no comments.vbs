' nested for loop to determine even/odd rows and columns'
'odd/odd are red, even/even red'
'mixed are black'
Sub checkerboard()
dim cellnumber as integer
cellnumber = 1 

For r = 1 to 8
	For c = 1 to 8
		if(cellnumber Mod 2 = 0) Then
			Cells(r, c).Interior.Colorindex = 1

		else
			Cells(r, c).Interior.Colorindex = 3

		end if
		cellnumber = cellnumber + 1

	next c
	cellnumber = cellnumber + 1
next r
end Sub
