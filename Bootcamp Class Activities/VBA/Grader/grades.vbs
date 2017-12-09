Sub Formatter()
if Cells(2, 2).Value >=90 then 
		Cells(2, 3).Interior.ColorIndex = 4
		Cells(2, 3).Value = "Pass"
	
	elseif Cells(2, 3).Value >=80 then 
		Cells(2, 3).Interior.ColorIndex = 4 
		Cells(2, 3).Value = "Pass"

	elseif Cells(2, 3).Value >= 70 then
		Cells(2, 3).Interior.ColorIndex = 2
		Cells(2, 3).Value = "Warning"

	else 
		Cells(2, 3).Interior.ColorIndex = 3 
		Cells(2, 3).Value = "Fail"

end if
	
End Sub