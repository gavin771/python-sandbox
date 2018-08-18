import webbrowser
import time

print("Started at {}".format(time.ctime()))
for c in range(3):
  time.sleep(2*60*60)
  print("Break #{} at {}".format(c+1, time.ctime()))
  webbrowser.open("https://www.youtube.com/watch?v=r6GMBCaagok")