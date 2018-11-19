# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 16:37:05 2018

@author: Hanifa
"""

import numpy as np
import pandas as pd

class DecisionTree:
    def __init_(self):
        print("Constructor")
    def __node_gini(self,ar):
        posLbl=np.count_nonzero(ar)
        negLbl=len(ar)-np.count_nonzero(ar)
        if len(ar)==0:
            return 0
        else:
            return 1-((posLbl/len(ar))**2+(negLbl/len(ar))**2)
    
    def gini(self,arA,arB):
        arA=np.array(arA)
        arB=np.array(arB)  
        
        #How to split this into two lines
        return ((len(arA)/(len(arA)+len(arB)))*self.__node_gini(arA))+((len(arB)/(len(arA)+len(arB)))*self.__node_gini(arB))

def approx_eq(a, b, num_sig=5):
    return round(a, num_sig) == round(b, num_sig)



if __name__ == '__main__':
    x=approx_eq(DecisionTree().gini([1, 0, 0, 0, 0], [1, 1, 1, 1, 0]), .32)    
    dataset = {'Taste':['Salty','Spicy','Spicy','Spicy','Spicy','Sweet','Salty','Sweet','Spicy','Salty'],
       'Temperature':['Hot','Hot','Hot','Cold','Hot','Cold','Cold','Hot','Cold','Hot'],
       'Texture':['Soft','Soft','Hard','Hard','Hard','Soft','Soft','Soft','Soft','Hard'],
       'Eat':['No','No','Yes','No','Yes','Yes','No','Yes','Yes','Yes']}
    df=pd.DataFrame(dataset)
    print(df)
    
