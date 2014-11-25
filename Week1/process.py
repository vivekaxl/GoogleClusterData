from __future__ import division
import math

def get_list(filename):
  l = []
  f = open(filename,"r")
  count=0
  for line in f:
    count+=1
    l.append(int(line.replace("\n","").split(" ")[4])/1e8)
  return sorted(l)

def frequency_count(itt, nr_bins=12000, minn=None, maxx=None):
  ret = []
  if minn == None:
    minn = itt[0]
  if maxx == None:
    maxx = itt[-1]
  binsize = (maxx - minn) / float(nr_bins) #man, do I hate int division

  #construct bins
  ret.append([float("-infinity"), minn, 0]) #-inf -> min
  start = minn
  end = 0
  while end < maxx:
    end = start + math.pow(binsize,1.5)
    ret.append([start, end, 0])
    start+= math.pow(binsize,1.5)
  ret.append([end, float("infinity"), 0]) #maxx -> inf

  #assign items to bin
  for item in itt:
    for binn in ret:
      if binn[0] <= item < binn[1]:
        binn[2] += 1        
  return ret

if __name__ == '__main__': 
  l = get_list("Results.txt") 
  sl = frequency_count(l)
  for x in sl:
    print "%f %f %f"%(x[0],x[1],x[2])

