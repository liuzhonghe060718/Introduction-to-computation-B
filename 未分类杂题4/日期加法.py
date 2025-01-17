day=list(map(int,input().split('-')))
n=int(input())
def check_year(a):
    m = a % 4
    p = a % 100
    t = a % 400
    if m != 0:
        return False
    elif p== 0 and t != 0:
        return False
    else:
        return True
def bianhuan(x,y,r,date):
    da_yue=[1,3,5,7,8,10,12]
    xiao_yue=[4,6,9,11]
    while r>0:
        if y in da_yue:
            r_1=r-31
        if y in xiao_yue:
            r_1=r-30
        if y==2:
            if check_year(x):
                r_1=r-29
            else:
                r_1=r-28
        if r_1<=0:
            break
        else:
            r=r_1
            if y<=11:
                y+=1
            else:
                y=1
                x+=1
    date=date+r
    if y in da_yue and date>31:
        date-=31
        y+=1
    if y in xiao_yue and date > 30:
        date -= 30
        y += 1
    if y == 2:
        if check_year(x) and date>29:
            date-=29
            y+=1
        elif check_year(x) and date>28:
            date-=28
            y+=1
        else:
            pass
    return str("{:02d}".format(x)),str("{:02d}".format(y)),str("{:02d}".format(date))
s=bianhuan(day[0],day[1],n,day[2])
print('-'.join(s))




day = list(map(int, input().split('-')))
n = int(input())


def check_year(a):
    return a % 4 == 0 and (a % 100 != 0 or a % 400 == 0)


def bianhuan(x, y, r, date):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    while r > 0:
        if y == 2 and check_year(x):
            days_in_month[1] = 29
        else:
            days_in_month[1] = 28

        if date + r > days_in_month[y - 1]:
            r -= (days_in_month[y - 1] - date + 1)
            date = 1
            y += 1
            if y > 12:
                y = 1
                x += 1
        else:
            date += r
            r = 0

    return str("{:04d}".format(x)), str("{:02d}".format(y)), str("{:02d}".format(date))


s = bianhuan(day[0], day[1], n, day[2])
print('-'.join(s))
