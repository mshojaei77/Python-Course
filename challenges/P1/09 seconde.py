# تبدیل ثانیه به روز ساعت ماه 
sec = int(input("Seconde: " ))
d = sec / 86400
h = sec / 38600
m = sec / 60

print(sec," seconde is ",round(d,3),"day and ",round(h,3),"hour and ",round(m,3),"minute")
