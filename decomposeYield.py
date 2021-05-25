import sys
from ROOT import TCanvas, TFormula, TF1, TFile, SetOwnership
from ROOT import gROOT, gObjectTable
import re
import ROOT as rt
import numpy as np

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

print newfname
readFiles_cx()
print "sm = ", float(smYield[0])  
print "sm_lin_quad_cG = ", float(smYield[0])*(1+param_cx[1]+param_cx[2])
print "quad_cG = ", float(smYield[0])*(param_cx[2])

#updateSignalYield()
