import pandas as pd
import matplotlib.pyplot as pt

class workout:
    def __init__(self,name,data):
        self.name=name
        self.datapath=data 
        if self.datapath == "":
            self.datapath='data.csv'
            print("\n")
            print("\033[31m Graph loading [success]....")
        else:
            print("")
            print("\033[31m # Data loading  [Success].....")      
            print("\033[31m # Graph loading [Success].....")             
    def process(self):
        path=pd.read_csv(self.datapath)       
        x=path['days']
        y=path[self.name]
        pt.bar(x,y)
        pt.title('data visualization'+" "+self.name) 
        pt.xlabel('days')
        pt.ylabel('counting')
        pt.show()


name=input("\033[32m enter the workout name :")
data=input("\033[32m enter the workout data path :")

work=workout(name,data)
work.process()
