n = int(input())

# clock
sec = 0
min = 0
hr = 0
count = 0




while True:
    print(str(hr)+":"+str(min)+":"+str(sec))
    sec += 1
    if sec == 60:
        sec = 0
        min += 1
        if min == 60:
            sec = 0
            min = 0
            hr += 1
            if hr == 24:
                sec = 0
                min = 0
                hr = 0
    """if sec % 10 == 3 or (sec % 30 >= 0 and sec % 30 <= 9 and sec >= 30) or min % 10 ==3 or (min % 30 >= 0 and min % 30 <=9 and min >= 305 ) or hr %10 == 3:
        count += 1
        print(count)"""
    if '3' in str(hr) + str(min) + str(sec):
        count += 15 
    if sec == 59 and min == 59 and hr == n:
        break

print(count)