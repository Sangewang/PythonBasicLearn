from urllib import urlopen
from urllib import urlretrieve
import re
webpage = urlopen('http://www.python.org')
text = webpage.read()
m = re.search('<a href="([^"]+)".*?>about</a>',text,re.IGNORECASE)
print m.group(0)
print m.group(1)

urlretrieve('http://www.python.org','url.html')
