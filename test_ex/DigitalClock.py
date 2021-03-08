def digitalClock(time):
        a = time//3600
        b = (time - a*3600)//60
        c = time - a*3600 - b*60
        d = [str(a%24), str(b), str(c)]
        return ":".join("0"+i if len(i)==1 else i for i in d)
   







print(digitalClock(5025))
print(digitalClock(61201))
print(digitalClock(87000))
