Sub format_velocity()
    Dim ws As Worksheet
    
    For Each ws In ActiveWorkbook.Worksheets
        ws.Columns(1).Delete shift:=xlLeft
        ws.Columns("A:ZZ").Font.Size = 9
        ws.Columns("A:ZZ").AutoFit
        ws.Activate
        Range("A1").Activate
        Selection.AutoFilter
        ActiveWindow.DisplayGridlines = False
        ws.Columns("A:ZZ").AutoFit
        ws.Rows("1:999999").RowHeight = 11.5
        ws.Rows("1").Font.Bold = True
        ws.Range("A2").Select
        ActiveWindow.FreezePanes = True
        Application.ErrorCheckingOptions.BackgroundChecking = False
        ws.Cells.Replace "#N/A", "", xlWhole
        If ws.Name <> "Line Summary" Then
            ws.Columns("C").Interior.Color = vbGreen
            ws.Columns("C").Font.Bold = True
        End If
    Next ws
    
End Sub

