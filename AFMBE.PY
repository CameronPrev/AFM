import pandas as pd
import sqlite3 as sq

conn = sq.connect('test.db')
c = conn.cursor()

def set_table():
    c.execute("""CREATE TABLE IF NOT EXISTS cameron(
              "Name" VARCHAR,
              "type" VARCHAR,
              "Jan" VARCHAR,
              "Feb" VARCHAR
              "Mar" VARCHAR,
              "Total" VARCHAR,
              "Budget" VARCHAR);""")
    conn.commit()         



set_table()


input_01='http://opsperf2/scorecards2/finance/BudgetYEEs.aspx?Execute=DownloadXLSX&AsOPUser=6095666&ManualOPPWD=P73C9566&Prime=*lee,%20jason*'
data = pd.read_excel(input_01,index_col=0)
df = pd.DataFrame(data, columns= ['Name','Type','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec','Total','Budget'])
df = df.drop_duplicates()
df.to_sql("cameron", conn, if_exists="replace")

Best_Network = pd.read_sql_query(""" SELECT *  FROM cameron where Name="Best Network"  """, conn)
Actix_One = pd.read_sql_query(""" SELECT *  FROM cameron where Name="ActixOne"  """, conn)
Son = pd.read_sql_query(""" SELECT *  FROM cameron where Name="ActixOne"  """, conn)
Plnt = pd.read_sql_query(""" SELECT *  FROM cameron where Name="ActixOne"  """, conn)
Machine_Learning= pd.read_sql_query(""" SELECT *  FROM cameron where Name="ActixOne"  """, conn)
UXI= pd.read_sql_query(""" SELECT *  FROM cameron where Name="ActixOne"  """, conn)
Drone_Innovation= pd.read_sql_query(""" SELECT *  FROM cameron where Name="ActixOne"  """, conn)





print(Best_Network)
print(Actix_One)
print(Son)
print(Plnt)
print(Machine_Learning)
print(UXI)
print(Drone_Innovation)

