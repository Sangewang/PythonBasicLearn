class Demo:
  def rhomb(self,input):
    result = ''
    input = input.strip()
    try: 
      num = float(input)
      if num<0 or num>100:
        result = input + '-->' + 'Error number'
      elif num<60:
        result = input + '-->' + 'F'
      elif num<70:
        result = input + '-->' + 'D'
      elif num<80:
        result = input + '-->' + 'C'
      elif num<90:
        result = input + '-->' + 'B'
      else:
        result = input + '-->' + 'A'
    except:
      result = input + '-->' + 'It is not a number'
    return result

Test = Demo()
print Test.rhomb('59')
print Test.rhomb('90.5')
print Test.rhomb('23')
print Test.rhomb('60')
print Test.rhomb('75')
print Test.rhomb('e')
print Test.rhomb('-90')
print Test.rhomb('999')
print Test.rhomb('  999 ')
print Test.rhomb('88')
print Test.rhomb('0')
