import datetime
class Demo:
  def intervalDays(self,str1,str2):
    list1 = str1.split('/')
    year1 = int(list1[0])
    mon1  = int(list1[1])
    day1  = int(list1[2])

    list2 = str2.split('/')
    year2 = int(list2[0])
    mon2  = int(list2[1])
    day2  = int(list2[2])

    date1 = datetime.datetime(year1,mon1,day1)
    date2 = datetime.datetime(year2,mon2,day2)

    interval = (date1 - date2).days
    return interval

Test = Demo()
str1 = raw_input('Please Input a data(like:xxxx/xx/xx): ')
str2 = raw_input('Please Input a data(like:xxxx/xx/xx): ')

print Test.intervalDays(str1,str2)
