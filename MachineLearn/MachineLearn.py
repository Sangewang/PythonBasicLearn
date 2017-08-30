from sklearn import svm, datasets
  
class Dataset(object):
  def __init__(self,name):
    self.name = name

  def download_data(self):
    if self.name == 'iris':
      self.download_data = datasets.load_iris()
    elif self.name == 'digits':
      self.download_data = datasets.load_digits()
    else:
      print('Dataset Error: No named datasets')

  def generate_xy(self):
    self.download_data()
    x = self.download_data.data
    y = self.download_data.target
    print('\nOriginal data looks like this: \n',x)
    print('\nLabels looks like this: \n',y)
    return x,y

  def get_train_test_set(self,ratio):
    x,y = self.generate_xy()
    n_samples = len(x)
    n_train   = round(n_samples * ratio)
    X_train = x[:n_train]
    y_train = y[:n_train]
    X_test  = x[n_train:]
    y_test  = y[n_train:]
    return X_train,y_train,X_test,y_test


data = Dataset('digits')
X_train,y_train,X_test,y_test = data.get_train_test_set(0.7)

clf = svm.SVC()
clf.fit(X_train,y_train)
test_point = X_test[7]
y_true = y_test[7]
print('y_true = ',y_true)
print('test_point = ',test_point)
print('test = ',clf.predict(test_point))
