import pandas as pd
import sqlite3 as sq

from flask import Flask
app = Flask(__name__)

@app.route('/')




def new():
    conn = sq.connect('test.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS cameron(
              "Name" VARCHAR,
              "type" VARCHAR,
              "Jan" VARCHAR,
              "Feb" VARCHAR
              "Mar" VARCHAR,
              "Total" VARCHAR,
              "Budget" VARCHAR);""")
    input_01='http://opsperf2/scorecards2/finance/BudgetYEEs.aspx?Execute=DownloadXLSX&AsOPUser=6095666&ManualOPPWD=P73C9566&Prime=*lee,%20jason*'
    data = pd.read_excel(input_01,index_col=0)
    df = pd.DataFrame(data, columns= ['Name','Type','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec','Total','Budget'])
    df = df.drop_duplicates()
    df.to_sql("cameron", conn, if_exists="replace")
    
    conn.commit()         

    
    Best_Network = pd.read_sql_query(""" SELECT *  FROM cameron where Name="Best Network"  """, conn)
    print(k = Best_Network['Type'][0])
    kwargs = {BN = 
            
            
            
            
            }
       
        I 
       
new()
       
    


    






