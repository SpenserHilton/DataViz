'Function to check if worksheet exists
Function WorksheetExists(sName As String) As Boolean
    WorksheetExists = Evaluate("ISREF('" & sName & "'!A1)")
End Function

Sub WorkingPart2_AG()

    Dim LastRowCombinedData
    Dim LastRowActiveDataSheet
    Dim HeaderSet As Boolean
        'New datatype below - WorkSheet (only exists in Excel VBA)
    Dim CombinedSheet As Worksheet
    
        'Random flag to check if we placed a header on Combined_Data
    HeaderSet = False
    
        'Check if CombinedData tab already exists, if it does delete data, if not add it
    If (WorksheetExists("Combined_Data")) Then
    
        Sheets("Combined_Data").Cells.Delete
    
    Else
            'Select the first sheet, and add a new spreadsheet before it
        Sheets("Alabama_Wells_Fargo_Deposits").Select
        Sheets.Add
        
            'Select the new sheet and rename it to Combined Data
        ActiveSheet.Name = "Combined_Data"
    End If


        'Set CombinedSheet equal to the worksheet titled Combined Data
    Set CombinedSheet = Worksheets("Combined_Data")
    
        'Set LastRowCombinedData equal to the first blank row (last row with data + 1)
    LastRowCombinedData = CombinedSheet.Cells(Rows.Count, "A").End(xlUp).Row + 1
    
    For i = 1 To ThisWorkbook.Worksheets.Count
    
        If (ThisWorkbook.Worksheets(i).Name <> "Combined_Data") Then
            ThisWorkbook.Worksheets(i).Select
            If (HeaderSet = False) Then
                CombinedSheet.Range("A1:G1").Value = ActiveSheet.Range("A1:G1").Value
                HeaderSet = True
            End If
        
            ThisWorkbook.Worksheets(i).Activate
                'Grab the last row of the sheet you are copying data from
            LastRowActiveDataSheet = ActiveSheet.Cells(Rows.Count, "A").End(xlUp).Row
            
                'Set the empty space of Combined Sheet equal to full range of data from Active data sheet
            Worksheets("Combined_Data").Range("A" & LastRowCombinedData & ":G" & LastRowCombinedData + (LastRowActiveDataSheet - 1) - 1).Value = _
            ThisWorkbook.Worksheets(i).Range("A2:G" & LastRowActiveDataSheet).Value

                'Adjust the LastRowCombinedData number to new last row for Combined Data Sheet
            LastRowCombinedData = CombinedSheet.Cells(Rows.Count, "A").End(xlUp).Row + 1

            
        End If
        
    Next i

            CombinedSheet.Select
            Columns("A:G").Select
    
            With Selection
                .HorizontalAlignment = xlCenter
            End With
            Columns("A:G").EntireColumn.AutoFit
    
End Sub



