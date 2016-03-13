
'''
注意到datetime是模块，datetime模块还包含一个datetime类，通过from datetime import datetime导入的才是datetime这个类。

如果仅导入import datetime，则必须引用全名datetime.datetime。
'''
from datetime import datetime

now=datetime.now()
print(now)

dt=datetime(2015,4,19,12,20)
print(dt)

#timestamp
print(dt.timestamp() )# 把datetime转换为timestamp

t = 1429417200.0
print(datetime.fromtimestamp(t))
print(datetime.utcfromtimestamp(t)) # UTC时间

#str转换为datetime,需要一个日期和时间的格式化字符串:https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
#datetime转换为str
print(now.strftime('%a, %b %d %H:%M'))

#datetime加减,timedelta
from datetime import timedelta

print(now + timedelta(hours=10))
print(now + timedelta(days=2, hours=12))

#本地时间转换为UTC时间
from datetime import  timezone
tz_utc_8 = timezone(timedelta(hours=8))# 创建时区UTC+8:00
dt = now.replace(tzinfo=tz_utc_8) # 强制设置为UTC+8:00


'''
#假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp：
'''


