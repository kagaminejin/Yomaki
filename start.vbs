Dim WShell
Set WShell = CreateObject("WScript.Shell")
WShell.Run "replace_sole.py", 0
Set WShell = Nothing