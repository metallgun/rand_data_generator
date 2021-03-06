# Inserting random data into SQL-database
# For churn rate analysis

import random as rnd
import datetime as dt

f = open("randomdata.sql", "w").close()
f = open("randomdata.sql", "a")

start_date = dt.datetime.now()
end_date = dt.datetime.now()

f.write("use Test;\ndelete from {0};\ninsert into {0} values ".format("subscriptions"))
print("use Test;\ndelete from {0}\ninsert into {0} values ".format("subscriptions"))

for i in range(1000):

    rnd_delta = rnd.random()

    if 0 < rnd_delta < 0.33:
        start_date = dt.datetime.now() - dt.timedelta(rnd.randint(1, 30))
    elif 0.33 <= rnd_delta < 0.66:
        start_date = dt.datetime.now() - dt.timedelta(rnd.randint(30, 60))
    else:
        start_date = dt.datetime.now() - dt.timedelta(rnd.randint(60, 90))

    rnd_delta = rnd.random()

    if rnd.random() < 0.5:
        end_date = dt.datetime(9999, 1, 31)
    else:
        end_date = start_date + dt.timedelta(rnd.randint(1, 3)*30)


    f.write("({}, '{}', '{}', {}),".format(i+1, start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d"), rnd.randint(1, 4)))
    print("({}, '{}', '{}', {}),".format(i+1, start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d"), rnd.randint(1, 4)))

f.close()