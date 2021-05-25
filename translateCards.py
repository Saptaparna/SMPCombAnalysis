import sys
from ROOT import TCanvas, TFormula, TF1, TFile, SetOwnership
from ROOT import gROOT, gObjectTable
import re
import ROOT as rt
import numpy as np

param_cx = []
param_cw = []
param_cb = []

fname = str(sys.argv[1])
file = TFile.Open(fname)

def readFiles_cx():
  func = file.Get('bin_content_par1_par2_par3_1')
  param_sm = func.GetParameter(0)
  param_int_cx = func.GetParameter(1)
  param_bsm_cx = func.GetParameter(7)
  param_cx.append(param_sm)
  param_cx.append(param_int_cx)
  param_cx.append(param_bsm_cx)

def readFiles_cw():
  func = file.Get('bin_content_par1_par2_par3_1')
  param_sm = func.GetParameter(0)
  param_int_cw = func.GetParameter(2)
  param_bsm_cw = func.GetParameter(8)
  param_cw.append(param_sm)
  param_cw.append(param_int_cw)
  param_cw.append(param_bsm_cw)

def readFiles_cb():
  func = file.Get('bin_content_par1_par2_par3_1')
  param_sm = func.GetParameter(0)
  param_int_cb = func.GetParameter(3)
  param_bsm_cb = func.GetParameter(9)
  param_cb.append(param_sm)
  param_cb.append(param_int_cb)
  param_cb.append(param_bsm_cb)

def parabola_cx_1D(x):
  readFiles_cx()
  funct = param_cx[0] + param_cx[1]*x + param_cx[2]*x*x
  return funct

def parabola_cw_1D(x):
  readFiles_cw()
  funct = param_cw[0] + param_cw[1]*x + param_cw[2]*x*x
  return funct

def parabola_cb_1D(x):
  readFiles_cb()
  funct = param_cb[0] + param_cb[1]*x + param_cb[2]*x*x
  return funct

readFiles_cx()
print parabola_cx_1D(10.0)

readFiles_cw()
print parabola_cw_1D(10.0)

readFiles_cb()
print parabola_cb_1D(10.0)

fname = fname.replace('.root','.txt')
fname = fname.replace('signal_proc','aC')

newfname = fname.strip(".txt") + '_AM'
newfname = newfname + ".txt"
print newfname

dataCard = open(fname, 'r')
remove_words = ['shapes', 'shape1']#, '------']
with open(fname) as oldfile, open(newfname, 'w') as newfile:
  for line in oldfile:
    if not any(remove_word in line for remove_word in remove_words):
      newfile.write(line)


file.Close()
