import os 

def save_file(filename, head, data) :
  path = "./logs/"
  filename = filename.find('.log') > -1 and filename or filename + '.log'
  is_exists = os.path.exists(path + filename)

  f = open(path + filename, 'a')
  if not is_exists:
    f.write(','.join(head))
    f.write('\n')

  for packet in data:
    f.write(','.join(dict_to_list(packet, head)))
    f.write('\n')


def dict_to_list(origin, head):
  temp = []
  for column in head:
    temp.append(origin[column])
  # print(origin['img'], temp[2])
  return temp


if __name__ == "__main__":
  save_file('t.log', ['link', 'title', 'img', 'info', 'text'], [['1', '2', '3', '4', '5']])
