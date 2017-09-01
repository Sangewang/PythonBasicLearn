class FileOperation(object):
  def __init__(self):
    print('Start Operate File...')
  
  def Copy(self,src,dst):
    print('srouce file location = ',src)
    print('dest file location = ',dst)
    try:
      file_src = open(src)
      file_dst = open(dst,"w")
      while(True):
        line_src = file_src.readline()
        file_dst.write(line_src)
        if not line_src:
          break
    except:
      print('------------------>Check File if exist!<---------------------')  
    finally:
      file_src.close()
      file_dst.close()
      print('Done File Copy...')

  

class File(FileOperation):
  def __init__(self):
    print('Start WithCopy File...')
  
  def WithCopy(self,src,dst):
    try:
      with open(src,'r') as file_src:
        with open(dst,'w') as file_dst:
          for line in file_src:
            file_dst.write(line)
    except:
      print('WithCopy Failed!')
    finally:
      print('Done WithCopy File!')

if __name__ == '__main__':
  Op_File = File()
  Op_File.Copy('/var/www/Python/test.py','/var/www/Python/copy.py')
  Op_File.WithCopy('/var/www/Python/test.py','/var/www/Python/withcopy.py')

