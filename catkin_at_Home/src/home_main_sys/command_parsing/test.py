import subprocess
import sys,os
f = open('sentence.txt', 'w')
f.write("test sentence")
#Call compiled parser
dir_path = os.path.dirname(os.path.realpath(__file__))
#print (dir_path)
loc = dir_path+'/main.exe'
#print(loc)
p = subprocess.Popen([loc])
print(p)
#out = open('output.txt','r+')
#answer = out.readline()
#print(answer)
#os.remove('output.txt')