#!/usr/bin/python

DEBUG=0
Samples=2049   #number of samples
Duty=.05      #% cycles should be on or off, remaining time is spent in Neutral
DutyCyles=int((Samples*Duty))  #sdfsdf
NutrualCycles=int(Samples-(DutyCyles*2))
NetrualCyclesA=int(NutrualCycles/2)
NetrualCyclesB=NutrualCycles-NetrualCyclesA

if DEBUG:
  print "NetrualCyclesA=%d" % (NetrualCyclesA)
  print "DutyCyles=%d" % (DutyCyles)
  print "NetrualCyclesB=%d" % (NetrualCyclesB)
  print "DutyCyles=%d" % (DutyCyles)

  Total=NetrualCyclesA+DutyCyles+NetrualCyclesB+DutyCyles
  print ( "Total=%d\n" % (Total) )

#TODO: If total dont=Samples we have a problem


#
High=4095
Netral=2048
Low=1
Seq=1
#Print the array
for x in range (0, NetrualCyclesA):
  if DEBUG:
    print "%d=%d" % (Seq,Netral)
  else:
    print Netral
  Seq=Seq+1

for x in range (0, DutyCyles):
  if DEBUG:
    print "%d=%d" % (Seq,High)
  else:
    print High
  Seq=Seq+1
  
for x in range (0, NetrualCyclesB):
  if DEBUG:
    print "%d=%d" % (Seq,Netral)
  else:
    print Netral
  Seq=Seq+1
    
for x in range (0, DutyCyles):
  if DEBUG:
    print "%d=%d" % (Seq,Low)
  else:
    print Low
  Seq=Seq+1
    