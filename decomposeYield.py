import sys
from ROOT import TCanvas, TFormula, TF1, TFile, SetOwnership
from ROOT import gROOT, gObjectTable
import re
import ROOT as rt
import numpy as np
from collections import Counter

fname = str(sys.argv[1])
file = TFile.Open(fname)

param_cx = []

def readFiles_cx():
  func = file.Get('bin_content_par1_par2_par3_1')
  param_sm = func.GetParameter(0)
  param_int_cx = func.GetParameter(1)
  param_bsm_cx = func.GetParameter(7)
  param_cx.append(param_sm)
  param_cx.append(param_int_cx)
  param_cx.append(param_bsm_cx)

def parabola_cx_1D(x):
  readFiles_cx()
  funct = param_cx[0] + param_cx[1]*x + param_cx[2]*x*x
  return funct

fname = fname.replace('.root','.txt')
fname = fname.replace('signal_proc','aC')
newfname = fname.strip(".txt") + '_AM'
newfname = newfname + ".txt"

#def updateSignalYield():
dataCard = open(newfname,"r") 
smYield = []
for line in dataCard:
  if line.startswith("rate"):
    parts = line.split()
    smYield.append(parts[1])

dataCardAgain = open(newfname,"r")
wnewfname = fname.strip(".txt") + "_AM_v1.txt"
nline = 0
nformat = 0
with open(wnewfname, 'w') as f:
  for line in dataCardAgain:
    if 'number of backgrounds' in line:
      words = line.split()
      newword = int(words[1]) + 2 #constant factor of 2
      line = line.replace(words[1], str(newword))
    if line.startswith("bin"):
      words = line.split()
      if len(words) > 2:
        newline = line.strip() + "                                       " + str(words[1]) + "                                       " + str(words[1])  + "\n"
        line = line.replace(line, newline)
    if line.startswith("process"):
      nline += 1
      words = line.split()
      if(nline==1):
        newwords = "sm" + "                                       "  + "quad_cG" + "                                       " + "sm_lin_quad_cG" + "                                       "
        line = line.replace(words[1], newwords) 
      if(nline==2):
        newline = line.strip() + "                                       " + str(int(words[len(words)-1])+1) + "                                       " + str(int(words[len(words)-1])+2)  + "\n"
        line = line.replace(line, newline)
    if line.startswith("rate"):
      words = line.split()
      readFiles_cx()
      newwords = str(float(smYield[0])) + "                                       " + str(float(smYield[0])*(param_cx[2])) + "                                       " + str(float(smYield[0])*(1+param_cx[1]+param_cx[2])) + "                                       "  
      line = line.replace(words[1], newwords)
    if 'lnN' in line: 
      words = line.split()
      newwords = words[2] + "                                       " + words[2]  + "                                       " +  words[2]  + "                                       "
      line = line.replace(words[2], str(newwords))   
    f.write(line)

readFiles_cx()
print "sm = ", float(smYield[0])  
print "sm_lin_quad_cG = ", float(smYield[0])*(1+param_cx[1]+param_cx[2])
print "quad_cG = ", float(smYield[0])*(param_cx[2])

#updateSignalYield()
