import mysql.connector

class Getphones:
    def __init__(self, model):
        self.model = model

    def getIP(self):
         mydb = mysql.connector.connect( host="localhost", user="root", password="root@123", port="3306", database="mydatabase")
         mycursor = mydb.cursor()
         mycursor.execute("SELECT ipaddress FROM phones WHERE model = '"+self.model+"'")
         myresult = mycursor.next()
         ipaddress = str(myresult[0])
         print("Phone picked is " + self.model +" "+ ipaddress)
         return ipaddress

'''
mycursor.execute("CREATE TABLE phones (model VARCHAR(255), ipaddress VARCHAR(255))")
sql = "INSERT INTO phones (model, ipaddress) VALUES (%s, %s)"
val = ("VVX350", "10.221.26.173")
mycursor.execute(sql, val)
val = ("VVX501", "10.221.33.14")
mycursor.execute(sql, val)
mydb.commit()
'''

