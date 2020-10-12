import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-J9SLKFT;'
                      'Database=FixedSystems;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('select * from dbo.')
for row in cursor:
    print(row)