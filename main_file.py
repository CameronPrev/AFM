import sqlite3
import pandas as pd

#Create database if not exist and get a connection to it

connection = sqlite3.connect('AFMDB/AFM.db')

# Get a cursor ro execute sql statements

cursor = connection.cursor()

# Create table

sql = '''CREATE TABLE IF NOT EXISTS OpsPerf
                '''
cursor.execute(sql)
# Insert data into table

sql = "INSERT INTO OpsPerf (,) VALUES (,)"

cursor.execute(sql)

# Persit data in AFM.db

connection.commit()

# Select all data of the table

sql = 'SELECT * FROM OpsPerf'
cursor.execute(sql)


rows = cursor.fetchall()

for row in rows
    print(row)


connection.close()


opsprf_data='http://opsperf2/scorecards2/finance/BudgetYEEs.aspx?Execute=DownloadXLSX&AsOPUser=6095666&ManualOPPWD=P73C9566&Prime=*lee,%20jason*'
df = pd.read_excel(input_01)


for budgetline, name, total, budget in df[['Budget Line'],['Name'],['Total','Budget']]:
   print (budgetline, name, total, budget)
   c.execute("INSERT INTO camers VALUES (?,?,?,?)",[budgetline, name, total, budget])


sql_command = """SELECT * FROM %s"""%(table)
c.execute(sql_command)

data = c.fetchall()
print(data, len(data))
