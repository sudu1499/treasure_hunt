import sqlite3

conn=sqlite3.connect('q.db')
c=conn.cursor()
#c.execute('create table q_table (q text,a text,b text,c text,d text,ans text)')
c.execute('''insert into q_table values("Grand Central Terminal, Park Avenue, New York is the world\'s","largest railway station","highest railway station","longest railway station","None of the above",'a')''')
c.execute("""insert into q_table values(
    'Entomology is the science that studies','Behavior of human beings','Insects','The origin and history of technical and scientific terms','The formation of rocks','b') 
    """)
c.execute(''' insert into q_table values("Eritrea, which became the 182nd member of the UN in 1993, is in the continent of","Asia","Africa","Europe","Australia","b" )
''') 
c.execute(''' insert into q_table values(
    "Garampani sanctuary is located at","Junagarh, Gujarat","Diphu, Assam","Kohima, Nagaland","Gangtok, Sikkim","b"
)
''')
c.execute('''insert into q_table values(
    "For which of the following disciplines is Nobel Prize awarded?","Labour Party","Nazi Party","Ku-Klux-Klan","Democratic Party",'b'
)''')
c.execute("""insert into q_table values(
    "In which year of First World War Germany declared war on Russia and France?","1914","1915","1916","1917","a"
)
""")
c.execute("""insert into  q_table values(
    "ICAO stands for","International Civil Aviation Organization","Indian Corporation of Agriculture Organization","Institute of Company of Accounts Organization","None of the above","a"
)
""")
c.execute("""insert into  q_table values(
    "India's first Technicolor film ____ in the early 1950s was produced by ____","'Jhansi Ki Rani', Sohrab Modi","	'Jhansi Ki Rani', Sir Syed Ahmed","'Mirza Ghalib', Sohrab Modi","	'Mirza Ghalib', Munshi Premchand","a")""")
c.execute("""insert into  q_table values(
    "India has largest deposits of ____ in the world.","gold","copper","mica","none of the above","c"
)
""")
c.execute("""insert into  q_table values(
    "How many Lok Sabha seats belong to Rajasthan?","32","25","30","17","b")""")
c.execute("""insert into q_table values(
    "The 2006 World Cup Football Tournament held in","France","China","Germany","Brazil","c"
)
""")
conn.commit()
c.execute("select * from q_table")
for i in c.fetchall():
    print(i)
conn.close()
