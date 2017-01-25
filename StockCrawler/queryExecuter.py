import time
import mysql.connector 

# conn = mysql.connector.connect(user='root', password ='enfndks@0', host='localhost', database='stockdata')
# mycursor = conn.cursor()
# queryString = "INSERT INTO pvinsight (Dateinfo) VALUES('"+ time.strftime("%Y-%m-%d") + "');"
# mycursor.execute(queryString)
# conn.commit()
class myQueryExecuter():

    conn = mysql.connector.connect(user='root', password ='enfndks@0', host='localhost', database='stockdata')
    mycursor = conn.cursor()
    
    def execute(self, queryString):
        # TODO : commit only when the execute work well 
        self.mycursor.execute(queryString)
        self.conn.commit()


