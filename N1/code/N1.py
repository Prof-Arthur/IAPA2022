import numpy as np
import pandas as pd
import random

def generator(RA): # V1000, A(3x4), B(4x5), C(3x3), I4(4x4), V1(1x5), V2(5x1)
    nomes=['Alberto','Ana','Bruna','Bruno','Cláudio','Cláudia','Diana','David','Edson','Élida','Fabiana','Fausto','Gustavo','Gabriela','Helena','Hyago','Iago','Iara','Joana','João','José','Kelson','Kelly','Luana','Lucas','Mariano','Mário','Márcia','Neide','Nelson','Otávio','Olívia','Patrícia','Pedro','Quênia','Roberto','Roberta','Silvio','Samara','Tamara','Thiago','Ulisses','Vanderson','Valéria','Wendell','Wanessa','Xuxa','Yves','Zênia'];grupos=['A']*(len(nomes)//3)+['B']*(len(nomes)-len(nomes)//3);RA=int(RA)%(2**32-1);random.seed(RA);random.shuffle(nomes);random.shuffle(grupos);np.random.seed(RA);idades=list(1+(80*np.random.rand(len(nomes))).astype(int));pd.DataFrame({'Nome':nomes,'Grupo':grupos,'Idade':idades}).to_csv('dataframe.csv',index=False);return list(((RA%10)*10+100)+np.random.randn(1000)*(3+(RA%10))),(20*np.random.rand(3,4)-10).astype(int),(20*np.random.rand(4,5)-10).astype(int),(20*np.random.rand(3,3)-10).astype(int),np.eye(4),(20*np.random.rand(1,5)-10).astype(int),(20*np.random.rand(5,1)-10).astype(int)

