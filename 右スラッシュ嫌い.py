import pyperclip,time,re

ato='hoge'

def replace_slash():
  global ato
  if (pyperclip.paste(), '\\'):
    if ato == pyperclip.paste():
      return
    mae = pyperclip.paste()
    print('Before : ' + mae)
    ato = mae.replace('\\', '/')
    pyperclip.copy(ato)
    print('After : ' + ato+'\n')
  else:return

while True:
  replace_slash()
  time.sleep(0.5)

#ずっとループしてるから重くなりそうだけど、大して変わらないのでWhile Trueのところでは分岐させてません。