# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 14:23:35 2024

@author: basti
"""

import numpy as np
import sys
import pathlib

'''
from learning import LearnerSP, LossFunction, Solver, ProblemType
from learning import Cache, AmortizedCache, EvaluateCompareCaching, ArmotizedCaching, CachingStrategyType
from learning import InferencePCTSP, PCTSPUtils, ProblemPCTSP
from learning import InferenceKP, KPUtils, ProblemKP
from config import set_verbose, is_verbose
'''

from sklearn.model_selection import train_test_split
from datetime import datetime
import argparse


parser = argparse.ArgumentParser('Experiments on synthetic pctsp datasets')
parser.add_argument('-p', '--problem_type', type=lambda input: ProblemType[input], default=ProblemType.PCTSP, choices=list(ProblemType), help="Problem that will be solved (PCTSP or KP)")
parser.add_argument('-i', '--dataset_path', type=str, default="../datasets/pctsp/nthreads_0/cp_training_n01_t600_s200.csv", help="dataset path")
parser.add_argument('-c', '--results_dir', type=str, default="results/resultsFinal", help="results directory")



y = [1,2,3]

def z(y):
    return (y[1]+y[2])*2 + (y[0])*3 

def FP(m,w,y):

    m = gp.read(Xpath)
    m.addVars()
    m.setParam('TimeLimit', 600)
    m.setObjective(quicksum(cost[i]*variables[i] for i in range(0,L)), GRB.MINIMIZE) 
    m.optimize()
    
    sol = [var.X for var in variables]    
    return sol


def SLS(Y,YY,w,y):

    model = gp.Model('SLS')
    
    y = model.addVar()
    kappa = model.addVars(L,name="k",lb = -GRB.INFINITY)
    w_bar = model.addVars(L,name="k",lb = -GRB.INFINITY)
    
    model.addConstr((w_bar + kappa) @ (z(y) - z(y)) == 0, name="constraint1")
    
    model.addConstr(w*w_bar = 0)
    
    #kappa2 = model.addVars(L,name="k2",lb = -GRB.INFINITY)
    #for j in range(0,L):
     #   model.addConstr(kappa[j] <= kappa2[j] )
      #  model.addConstr(-kappa2[j] <= kappa[j])
    
    model.setObjective(gp.quicksum(gp.abs_(kappa_i) for kappa_i in kappa), GRB.MINIMIZE)
    
    
    
    
    
    
    
    