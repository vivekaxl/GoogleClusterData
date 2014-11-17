from __future__ import division
from collections import defaultdict
import sys
import random
import math

class JobEvent(object):
  def __init__(self,ts,jbid,etype,jobt):
    self.timestamp = ts
    self.job_id = jbid
    self.event_type = etype
    self.job_type = jobt #1- least imp; 3- latency sensitive

#TODO: Need to change this global implementation
flag = False
start_time=0
def extract_job_event(file_name,dictionary):
  global flag,start_time
  for line in open(file_name):
    temp = line.replace("\n","").split(",")
    if int(temp[0]) == 0: continue
    else:
      if flag == False: 
        start_time = int(temp[0])
        flag = True
      #print "TimeStamp: ",int(temp[0])-start_time
      objct = JobEvent(int(temp[0])-start_time,temp[2],temp[3],temp[6])
      if temp[2] in dictionary: 
        dictionary[temp[2]].append(objct)
      else: 
        if int(temp[3])!=0: continue
        tempL = [objct]
        dictionary[temp[2]] = tempL
  return dictionary

def _check_dictionary(dictionary):
  delete_keys=[]
  for key in dictionary:
    flag = False
    for item in dictionary[key]:
      if int(item.event_type) == 4: flag = True
      if flag == True: 
        temp_time = int(item.timestamp) - int(dictionary[key][0].timestamp)
        with open("Results.txt", "a") as myfile: 
          myfile.write("Job id: %s Time: %d\n"%(key,temp_time))
        delete_keys.append(key)
  for x in delete_keys: dictionary.pop(x,None)
  return dictionary

def get_names(dir_name):
  import glob,os
  name = dir_name+"/*.csv"
  filelist = glob.glob(name)
  return sorted(filelist)



if __name__ == '__main__': 

  dictionary = defaultdict(list)
  files = get_names("job_events")
  count = 0
  for f in files:
    count+=1
    print count,
    dictionary = extract_job_event(f,dictionary)
    print len(dictionary.keys()),
    dictionary = _check_dictionary(dictionary)
    print len(dictionary.keys())



