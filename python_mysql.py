import mysql.connector

# conn=mysql.connector.connect(host="localhost",user="root",password="root")
# print(conn)

# cursor=conn.cursor()
# cursor.execute("CREATE DATABASE mydb")

conn=mysql.connector.connect(host="localhost",user="root",password="root",db="mydb")
print(conn)

cur=conn.cursor()

# cur.execute("CREATE TABLE contacts(id int primary key auto_increment,name varchar(20),phone bigint)")
# print("table created")

# # ---------- Insertion ----------

# cur.execute("INSERT INTO contacts VALUES(null,'ajith',9947354942)")
# conn.commit()

# print("Values inserted")

# ---------- Selection ----------

cur.execute("SELECT * FROM contacts")
# res=cur.fetchall()
res=cur.fetchone()
print(res)