ASSIGNMENT NO: 6
Problem statement: Write a PL/SQL block of code using Cursor for different applications.

Connect System;
Enter Password:
Connected.
SQL> create table newroll(Roll_no numeric,Name varchar(30),Class varchar(5));
Table created.
SQL> insert into newroll values(1,'Amar','B.E');
1 row created.
SQL> ed
Wrote file afiedt.buf
45
q
  1* insert into newroll values(2,'Dipak','S.E')
SQL> /
1 row created.
SQL> ed
Wrote file afiedt.buf
46
Q

  1* insert into newroll values(3,'Saurab','MTech')
SQL> /
1 row created.
SQL> ed
Wrote file afiedt.buf
49
q
  1* insert into newroll values(4,'Amit','F.E')
SQL> /
1 row created.
SQL> insert into newroll values(9,'Rushikesh','B.E');

1 row created.
SQL> create table oldroll(ID numeric,Name varchar(30),Class varchar(5));
Table created.
SQL> insert into oldroll values(1,'Amar','B.E');
1 row created.
SQL> ed
Wrote file afiedt.buf
45
q
  1* insert into oldroll values(2,'Dipak','S.E')
SQL> /
1 row created.
SQL> ed
Wrote file afiedt.buf
46
q
  1* insert into oldroll values(3,'Saurab','MTech')
SQL> /
1 row created.

SQL> ed
Wrote file afiedt.buf
49
q
  1* insert into oldroll values(4,'Amit','F.E')
SQL> /

1 row created.

SQL> ed
Wrote file afiedt.buf
45
q
  1* insert into oldroll values(5,'Kunal','T.E')
SQL> /

1 row created.
SQL> ed
Wrote file afiedt.buf
46
q
  1* insert into oldroll values(6,'Akash','B.E')
SQL> /

1 row created.
SQL> select * from newroll; 

   ROLL_NO NAME               CLASS
---------- ------------------------------ -----
     1 Amar               B.E
     2 Dipak              S.E
     3 Saurab              MTech
     4 Amit               F.E
     9 Rushikesh              B.E

SQL> select * from oldroll;

    ID NAME               CLASS
---------- ------------------------------ -----
     1 Amar               B.E
     2 Dipak              S.E
     3 Saurab              MTech
     4 Amit               F.E
     5 Kunal              T.E
     6 Akash              B.E

6 rows selected.
SQL> ed
Wrote file afiedt.buf
610
q
  1  declare
  2  roll_no1 oldroll.ID%type;
  3  name1 oldroll.Name%type;
  4  class1 oldroll.Class%type;
  5  cursor oldsroll is select * from oldroll;
  6  cursor newsroll(id number) is select Roll_No from newroll where Roll_No=id;
  7  begin
  8  open oldsroll;
  9  loop
 10  fetch oldsroll into roll_no1,name1,class1;
 11  exit when oldsroll%notfound;
 12  open newsroll(roll_no1);
 13  fetch newsroll into roll_no1;
 14  if newsroll%found then
 15  dbms_output.put_line('Existing Record!!!!!');
 16  else
 17  if newsroll%notfound then
 18  dbms_output.put_line('New Record.');
 19  insert into newroll values(roll_no1,name1,class1);
 20  end if;
 21  end if;
 22  close newsroll;
 23  end loop;
 24  close oldsroll;
 25* end;
 26  /
Existing Record!!!!!
Existing Record!!!!!
New Record.
New Record.
PL/SQL procedure successfully completed.
SQL> select * from newroll;
   ROLL_NO NAME               CLASS
---------- ------------------------------ -----
     1 Amar               B.E
     2 Dipak              S.E
     3 Saurab              MTech
     4 Amit               F.E
     9 Rushikesh              B.E
     5 Kunal              T.E
     6 Akash              B.E

7 rows selected.
