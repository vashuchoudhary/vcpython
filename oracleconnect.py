import jaydebeapi
conn = jaydebeapi.connect("oracle.jdbc.OracleDriver",
                            "jdbc:oracle:thin:@//TSORA12C:1521/PDB01",
                            ["c02813949", "c02813949"],
                            "C:\jdbcdriver\oracle\ojdbc7.jar",)
curs = conn.cursor()
curs.execute('create table CUSTOMER'
               '("CUST_ID" INTEGER not null,'
               ' "NAME" VARCHAR(50) not null,'
               ' primary key ("CUST_ID"))'
              )
curs.execute("insert into CUSTOMER values (1, 'John')")
curs.execute("select * from CUSTOMER")
curs.fetchall()
[(1, u'John')]
curs.close()
conn.close()
