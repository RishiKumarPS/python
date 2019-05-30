from sqlite3 import *
open('Hospital.db','w').close()
con=connect('Hospital.db')
cur=con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS Hospital (Hospital_Id int,Hospital_Name text,Bed_Count int)')
cur.execute('INSERT INTO Hospital VALUES(1,"Mayo Clinic",200)')
cur.execute('INSERT INTO Hospital VALUES(2,"Cleveland Clinic",400)')
cur.execute('INSERT INTO Hospital VALUES(3,"Johns Hopkins",1000)')
cur.execute('INSERT INTO Hospital VALUES(4,"UCLA Medical Centre",1500)')
con.commit()
print('HOSPITAL DB'.center(31,'*'))
print('ID\t\tHospital Name\t\tBed Count')
cur.execute('SELECT* FROM Hospital')
l=cur.fetchall()
for i in l:
    print(i[0],'\t',i[1].center(19),'\t\t',i[2],sep='') #19 because the length of largest hospital name is 19
print('\nExecuting suggested queries:')
print('1. Updating Bed Count of Hospital ID 1 to 100')
cur.execute('UPDATE Hospital SET Bed_Count=100 WHERE Hospital_Id=1')
con.commit()
print('HOSPITAL DB'.center(31,'*'))
print('ID\t\tHospital Name\t\tBed Count')
cur.execute('SELECT* FROM Hospital')
l=cur.fetchall()
for i in l:
    print(i[0],'\t',i[1].center(19),'\t\t',i[2],sep='') #19 because the length of largest hospital name is 19
print('\n2. Deleting entry of Hospital ID 3')
cur.execute('DELETE FROM Hospital WHERE Hospital_Id=3')
con.commit()
print('HOSPITAL DB'.center(31,'*'))
print('ID\t\tHospital Name\t\tBed Count')
cur.execute('SELECT* FROM Hospital')
l=cur.fetchall()
for i in l:
    print(i[0],'\t',i[1].center(19),'\t\t',i[2],sep='') #19 because the length of largest hospital name is 19
