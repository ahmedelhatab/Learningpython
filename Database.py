import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-J9SLKFT;'
                      'Database=FixedSystems;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
result=cursor.execute('select * from dbo.all_active_users')
for row in result:
    print(row)
# find a result of query
find_user_data=conn.cursor()
find_user_data.execute('select * from dbo.main_user_profile where ')

