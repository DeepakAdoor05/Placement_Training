# time = '00:00:00' to '23:59:59'

# i/p
# @9:00:00

# o/p
# 09:00:00
# 19:00:00

def display_time(hr,min_,sec):
    time = hr +':'+min_+':'+sec
    print(time)
    return time
# display_time(hr,min_,sec)

t = input()
hr = t[:2]
min_ = t[3:5]
sec = t[-2:]
if sec[1] == '@':
    sec = sec[0]+'0'
    display_time(hr,min_,sec)
    sec = sec[0]+'9'
    display_time(hr,min_,sec)
elif sec[0] == '@':
    sec = '0'+sec[1]
    display_time(hr,min_,sec)
    sec = '5'+sec[1]
    display_time(hr,min_,sec)

elif min_[1] == '@':
    min_ = min_[0]+'0'
    display_time(hr,min_,sec)
    min_ = min_[0]+'9'
    display_time(hr,min_,sec)
elif min_[0] == '@':
    min_ = '0'+min_[1]
    display_time(hr,min_,sec)
    min_ = '5'+min_[1]
    display_time(hr,min_,sec)

elif hr[1] == '@':
    hr = hr[0]+'0'
    display_time(hr,min_,sec)
    if hr[0] == '2':
        hr = hr[0]+'3'
        display_time(hr,min_,sec)
    else:
        hr = hr[0]+'9'
        display_time(hr,min_,sec)
elif hr[0] == '@':
    hr = '0'+hr[1]
    display_time(hr,min_,sec)
    if hr[1] <= '3':
        hr = '2'+hr[1]
    else:
        hr = '1'+hr[1]
    display_time(hr,min_,sec)
else:
    display_time(hr,min_,sec)