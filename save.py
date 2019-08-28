import os 

def saveByFile(filename, head, data) :
  path = "./logs/"
  isexists = os.path.exists(path + filename)

  f = open(path + filename, 'a')
  if not isexists:
    f.write(','.join(head))
    f.write('\n')

  f.write(','.join(data))
  f.write('\n')

if __name__ == "__main__":
  saveByFile('t.log', ['title', 'content'], ['1', '2'])
  saveByFile('t.log', ['title', 'content'], ['1', '2'])
  saveByFile('t.log', ['title', 'content'], ['1', '2'])