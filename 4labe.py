import os


def dir():
  pass
  
  
  
  
  
  
  
def dict_way_size(way):
    dictl = {}
    for root, dirs, files in os.walk(way):
        for file in files:
            newkey = {os.path.join(root, file): os.path.getsize(root + '\\' + file)}
            dict1.update(newkey)
    return dict1
            







def analysis(dict1):




  
  
  
  
  
def dupclicate(duplicate):
