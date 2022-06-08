'''
计算公元 1900 —— 2100 年之间的所有闰年

1582年以来的置闰规则:
普通闰年:公历年份是4的倍数，且不是100的倍数的，为闰年（如2004年、2020年等就是闰年）。
世纪闰年:公历年份是整百数的，必须是400的倍数才是闰年（如1900年不是闰年，2000年是闰年）。
1582年以前的惯例:四年一闰；如果公元A年的A（正数）能被4整除，那么它就是闰年；如果公元前B年的B（正数）除以4余1，那么它也是闰年。

'''

for year in range(1800,2400):
    if year % 4 == 0:
        if year % 100 != 0:
            print(year)
        elif year % 400 == 0:
            print(year)
