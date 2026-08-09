temps : list[int] = [21, 30, -999, 26, -999, 17, 33, -999, 28]
count = len(temps)
print ("count : ", count)
print ("First three : ", temps[:3])
print ("Last three : ", temps[-3:])
print("Every second : ", temps[0::2])
while -999 in temps:
    temps.remove(-999)
print ("Cleaned : ", temps)
Dropped_f_r = temps.pop(0)
print ("Dropped the first reading : ", Dropped_f_r)
temps.append(31)
print("After append : ", temps)
print ("Max : ",max(temps), "  Min : ", min(temps), "  Sum : ", sum(temps), "  Avg : ", (sum(temps)/len(temps)))
avg = sum(temps) / len(temps)
for i in temps :
    if i > avg:
        print ("Above average : ", i)