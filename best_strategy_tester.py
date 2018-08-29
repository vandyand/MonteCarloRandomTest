# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 14:41:21 2018

@author: dell
"""

import numpy as np
import random
import matplotlib.pyplot as plt

winning_final_bals = []
for k in range(100):
    
    #random.seed(1)
    all_strats = []
    all_trades = []
    
    for j in range(10):
        val = 0
        trades = []
        strat = []
        for i in range(20):
            value = random.random()*20-10.15
            trades.append(value)
            strat.append(val)
            val += value
        all_trades.append(trades)
        all_strats.append(strat)
    
    winning_trades = []
    winning_strat_num = []
    winning_strat_bal = []
    
    for i in range(1,len(trades)):
        current_winning_strat = -1
        current_winning_val = -1000000
        
        for j in range(len(all_trades)):
            if all_strats[j][i] > current_winning_val:
                current_winning_val = all_strats[j][i]
                current_winning_strat = j
        winning_strat_num.append(current_winning_strat)
        winning_trades.append(all_trades[current_winning_strat][i])
    
    winning_strat_bal = [0]+[ sum(winning_trades[:i]) for i in range(len(winning_trades)) ]
    
#    for j in range(len(all_strats)):
#        plt.plot(all_strats[j])
#    plt.plot(winning_strat_bal,c='black')
#    plt.show()
    
#    print(round(winning_strat_bal[-1],2))
    winning_final_bals.append(winning_strat_bal[-1])
    print(k)
    
print(np.mean(winning_final_bals))

