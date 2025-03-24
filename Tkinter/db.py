import sqlite3
class DataBase:
    def __init__(self,db):
        self.con=sqlite3.connect(db)
        self.cur=self.con.cursor()
        sql="""
        CREATE TABLE IF NOT EXISTS employees(
        Id integer primary key,
        name text,
        age text,
        doj text,
        email text,
        gender text,
        contact text,
        address text)"""
        self.cur.execute(sql)
        self.con.commit()
    #insert table
    def insert(self,name,age,doj,email,gender,contact,address):
        self.cur.execute("insert into employees values(NULL,?,?,?,?,?,?,?)",(name,age,doj,email,gender,contact,address))
        self.con.commit()
    #update 
    def update(self,id,name,age,doj,email,gender,contact,address):
        self.cur.execute("update employees set name=?,age=?,doj=?,email=?,gender=?,contact=?,address=? where id=?",(name,age,doj,email,gender,contact,address,id))
        self.con.commit()
    #delete
    def remove(self,id):
        self.cur.execute("delete from employees where id=?",(id,))
        self.con.commit()
    #fetch data
    def fetch(self):
        self.cur.execute("select * from employees")
        rows=self.cur.fetchall()
        return rows
        

