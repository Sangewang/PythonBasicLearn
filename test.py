import traceback
class Students(object):
  @property
  def score(self):
    return self._score

  @score.setter
  def score(self,value):
    if not isinstance(value,int):
      raise ValueError('not int')
    elif(value<0) or (value>100):
      raise ValueError('not between 0~100')

    self._score = value
  @property
  def double_score(self):
    return self._score * 2



sa = Students()
sa.score = 75
print(sa.score)
try:
  sa.score = 10212
except ValueError:
  traceback.print_exc()
try:
  sa.score = 'asd'
except:
  traceback.print_exc()
print(sa.double_score)
try:
  sa.double_score = 160
except AttributeError:
  traceback.print_exc()
