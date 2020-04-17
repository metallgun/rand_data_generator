# Inserting random data into SQL-database
# For churn rate analysis


"""
import pyodbc
server = 'DESKTOP-D4KA4D1\SQLEXPRESS' 
database = 'Test' 
username = 'gkkor' 
password = ''
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

cursor.execute('SELECT * FROM '+database+'.subscriptions')

for row in cursor:
    print(row)
"""

import random as rnd
import time

f = open("randomdata.sql", "w").close()
f = open("randomdata.sql", "a")

# Measuring elapsed time
start_time = time.time()

f.write("insert into subscriptions values ")
# print("insert into subscriptions values ")
for i in range(999):
    start_date = [rnd.randint(2010, 2019), rnd.randint(1, 12), rnd.randint(1, 28)]
    end_date = [None, None, None]

    # With the probability of 50% each user has canceled his subscription
    if rnd.random() > 0.5:
        # Start and end date generator starts
        while True:
            end_date[0] = rnd.randint(2010, 2019)
            if end_date[0] < start_date[0]:
                continue
            else:
                break

        if end_date[0] > start_date[0]:
            end_date[1] = rnd.randint(1, 12)
            end_date[2] = rnd.randint(1, 28)
        else:
            while True:
                end_date[1] = rnd.randint(1, 12)
                if end_date[1] > start_date[1]:
                    end_date[2] = rnd.randint(1, 28)
                    break
                elif end_date[1] == start_date[1]:
                    if start_date[2] != 28:
                        end_date[2] = rnd.randint(start_date[2], 28)
                    else:
                        end_date[2] = 28
                    break
                else:
                    continue
        # Start and end date generator ends


    if end_date[0] is not None:
        print("({}, '{}-{}-{}', '{}-{}-{}', {}),".format(i+1, start_date[0], start_date[1], start_date[2], end_date[0], end_date[1], end_date[2], rnd.randint(1, 4)))
        f.write("({}, '{}-{}-{}', '{}-{}-{}', {}),\n".format(i+1, start_date[0], start_date[1], start_date[2], end_date[0], end_date[1], end_date[2], rnd.randint(1, 4)))
    else:
        print("({}, '{}-{}-{}', '9999-12-31', {}),".format(i+1, start_date[0], start_date[1], start_date[2], rnd.randint(1, 4)))
        f.write("({}, '{}-{}-{}', '9999-12-31', {}),\n".format(i+1, start_date[0], start_date[1], start_date[2], rnd.randint(1, 4)))

print("Rows created! Elapsed: {}".format(time.time()-start_time))
f.close()
