import pyodbc
conn = pyodbc.connect(
'Driver={SQL Server};'
'Server=servercarbontower.database.windows.net;'
'Database=carbontower;'
'Integrated_Security=false;'
'UID=tower;'
'PWD=!Carbon6;'
'Trusted_Connection=no;')