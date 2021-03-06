                #------------WEATHER PREDICTION------------
#import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import tkinter as tk 
from tkinter import*

r = tk.Tk()
r.geometry("700x700") 
r.title('Choose the year that you want to show the ratio of rainfall in india') 


canvas=Canvas(width=2000, height=850,bg='white')
canvas.place(x=5,y=5)
rainfall=PhotoImage(file="pp.png")
canvas.create_image(0,0,image=rainfall,anchor=NW)


print(":::We have to predict the data of the following year:::\n")
df1={'YEAR':pd.Series(['2019','2018','2017','2016','2015'],index=[1,2,3,4,5])}
df=pd.DataFrame(df1)
print(df)
#print("DATA are as follows::::\n",df1)





def fun1(b):
    
    print("          ------RAINFALL RATIO OF 2015 IN INDIA ------")
    print("\n 1st::::In Winter")
    winter=['','38.8%','79.1%','21.7%','7.7%','30.1%']
    regions=['','Country as a Whole','North West India','Central India','South Peninsula','East & North East India'] 

    plt.title(" Region-wise Seasonal and Annual Rainfall(mm)- Year 2015")     # for title
    plt.bar(winter,regions,label='winter',color='yellow')

    plt.xlabel('WINTER(%)')
    plt.ylabel('REGIONS')
    plt.legend()                    #it will print label
    plt.show()

#------------------------------------------------------------------------------------------------------

    print("----------------------------------\n2nd::::In Pre-Monsoon")
    premonsoon=['','365.1%','212.4%','73.5%','179.8%','183.6%']
    regions=['','Country as a Whole','North West India','Central India','South Peninsula','East & North East India'] 

    plt.title(" Region-wise Seasonal and Annual Rainfall(mm)- Year 2015")     # for title
    plt.bar(premonsoon,regions,label='pre-monsoon',color='purple')

    plt.xlabel('PREMONSOON(%)')
    plt.ylabel('REGIONS')
    plt.legend()                    #it will print label
    plt.show()


#------------------------------------------------------------------------------------------------------

    print("----------------------------------\n3rd::::In Monsoon")
    monsoon=['','765.8%','510.8%','818.9%','605.1%','1343.4%']
    regions=['','Country as a Whole','North West India','Central India','South Peninsula','East & North East India'] 

    plt.title(" Region-wise Seasonal and Annual Rainfall(mm)- Year 2015")     # for title
    plt.bar(monsoon,regions,label='monsoon',color='red')

    plt.xlabel('MONSOON(%)')
    plt.ylabel('REGIONS')
    plt.legend()                    #it will print label
    plt.show()


#------------------------------------------------------------------------------------------------------

    print("---------------------------------\n4th::::In Post-Monsoon")
    postmonsoon=['','97.6%','46.2%','29.2%','317.2%','70.6%']
    regions=['','Country as a Whole','North West India','Central India','South Peninsula','East & North East India'] 

    plt.title(" Region-wise Seasonal and Annual Rainfall(mm)- Year 2015")     # for title
    plt.bar(postmonsoon,regions,label='postmonsoon',color='green')

    plt.xlabel('POSTMONSOON(%)')
    plt.ylabel('REGIONS')
    plt.legend()                    #it will print label
    plt.show()

#------------------------------------------------------------------------------------------------------

    print("--------------------------\n5th::::Annual Rainfall")
    annual=['','365.1%','212.4%','73.5%','179.8%','183.6%']
    regions=['','Country as a Whole','North West India','Central India','South Peninsula','East & North East India'] 

    plt.title(" Region-wise Seasonal and Annual Rainfall(mm)- Year 2015")     # for title
    plt.bar(annual,regions,label='annual',color='black')

    plt.xlabel('ANNUAL(%)')
    plt.ylabel('REGIONS')
    plt.legend()                    #it will print label
    plt.show()
    







#--------------------------------------------------------------------------------------

def fun2(b1):
    print("\n...............:: Rainfall Ratio(MM) of 2014 in India::............")
    print("\n            Analysing the data monthly in (MM)")
    j1=pd.read_csv('rishabh.csv')
    print(":::::\n",j1)
    







#--------------------------------------------------------------------------------------

def fun3(b2):
    print("\n...............::Region-Wise Monthly Rainfall Ratio of 2013(Milli Meter) in India::............")
    
    #PIE CHART "JANUARY"
    labels = 'COUNTRY AS A WHOLE', 'NORTH WEST INDIA', 'CENTRAL INDIA', 'SOUTH PENINSULA','EAST & NORTH_EAST INDIA'
    sizes = [11.3, 29.8, 2.2, 3.2,4.7]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','pink']
    explode = (0, 0.1, 0, 0, 0)  # explode 2nd slice
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
    autopct='%1.1f%%', shadow=True, startangle=140)
    plt.title("::JANUARY::\n")
    plt.axis('equal')
    plt.show()
    
    #PIE CHART "FEBRUARY"
    labels = 'COUNTRY AS A WHOLE', 'NORTH WEST INDIA', 'CENTRAL INDIA', 'SOUTH PENINSULA','EAST & NORTH_EAST INDIA'
    sizes = [40.1, 87.3, 16.1, 25.0,18.5]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','pink']
    explode = (0, 0.1, 0, 0, 0)  # explode 2nd slice
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
    autopct='%1.1f%%', shadow=True, startangle=140)
    plt.title("\n\n::FEBRUARY::\n")
    plt.axis('equal')
    plt.show()
    
    #PIE CHART "MARCH"
    labels = 'COUNTRY AS A WHOLE', 'NORTH WEST INDIA', 'CENTRAL INDIA', 'SOUTH PENINSULA','EAST & NORTH_EAST INDIA'
    sizes = [15.7,20.6,4.5,13.4,32.5]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','pink']
    explode = (0, 0, 0, 0, 0.1)  # explode 5th slice
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
    autopct='%1.1f%%', shadow=True, startangle=140)
    plt.title("\n\n::MARCH::\n")
    plt.axis('equal')
    plt.show()
    
    #PIE CHART "APRIL"
    labels = 'COUNTRY AS A WHOLE', 'NORTH WEST INDIA', 'CENTRAL INDIA', 'SOUTH PENINSULA','EAST & NORTH_EAST INDIA'
    sizes = [30.3,20.0,17.4,28.7,79.3]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','pink']
    explode = (0, 0, 0, 0, 0.1)  # explode 5th slice
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
    autopct='%1.1f%%', shadow=True, startangle=140)
    plt.title("\n\n::APRIL::\n")
    plt.axis('equal')
    plt.show()
    
    #PIE CHART "MAY"
    labels = 'COUNTRY AS A WHOLE', 'NORTH WEST INDIA', 'CENTRAL INDIA', 'SOUTH PENINSULA','EAST & NORTH_EAST INDIA'
    sizes = [57.8,17.9,10.6,53.9,239.4]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','pink']
    explode = (0, 0, 0, 0, 0.1)  # explode 5th slice
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
    autopct='%1.1f%%', shadow=True, startangle=140)
    plt.title("\n\n::MAY::\n")
    plt.axis('equal')
    plt.show()
    
     #PIE CHART "JUNE"
    labels = 'COUNTRY AS A WHOLE', 'NORTH WEST INDIA', 'CENTRAL INDIA', 'SOUTH PENINSULA','EAST & NORTH_EAST INDIA'
    sizes = [219.8,155.0,275.9,206.1,243.3]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','pink']
    explode = (0, 0, 0.1, 0, 0)  # explode 3rd slice
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
    autopct='%1.1f%%', shadow=True, startangle=140)
    plt.title("\n\n::JUNE::\n")
    plt.axis('equal')
    plt.show()
    
     #PIE CHART "JULY"
    labels = 'COUNTRY AS A WHOLE', 'NORTH WEST INDIA', 'CENTRAL INDIA', 'SOUTH PENINSULA','EAST & NORTH_EAST INDIA'
    sizes = [310.1,204.3,437.8,274.6,288.5]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','pink']
    explode = (0, 0, 0.1, 0, 0)  # explode 3rd slice
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
    autopct='%1.1f%%', shadow=True, startangle=140)
    plt.title("\n\n::JULY::\n")
    plt.axis('equal')
    plt.show()
    
     #PIE CHART "AUGUST"
    labels = 'COUNTRY AS A WHOLE', 'NORTH WEST INDIA', 'CENTRAL INDIA', 'SOUTH PENINSULA','EAST & NORTH_EAST INDIA'
    sizes = [254.9,247.2,299.7,164.9,286.0]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','pink']
    explode = (0, 0, 0.1, 0, 0)  # explode 3rd slice
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
    autopct='%1.1f%%', shadow=True, startangle=140)
    plt.title("\n\n::AUGUST::\n")
    plt.axis('equal')
    plt.show()
    
     #PIE CHART "SEPTEMBER"
    labels = 'COUNTRY AS A WHOLE', 'NORTH WEST INDIA', 'CENTRAL INDIA', 'SOUTH PENINSULA','EAST & NORTH_EAST INDIA'
    sizes = [152.6,65.6,180.5,180.1,227.7]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','pink']
    explode = (0, 0, 0, 0, 0.1)  # explode 5th slice
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
    autopct='%1.1f%%', shadow=True, startangle=140)
    plt.title("\n\n::SEPTEMBER::\n")
    plt.axis('equal')
    plt.show()
    
     #PIE CHART "OCTOBER"
    labels = 'COUNTRY AS A WHOLE', 'NORTH WEST INDIA', 'CENTRAL INDIA', 'SOUTH PENINSULA','EAST & NORTH_EAST INDIA'
    sizes = [129.3,40.7,138.4,193.3,201.8]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','pink']
    explode = (0, 0, 0, 0, 0.1)  # explode 5th slice
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
    autopct='%1.1f%%', shadow=True, startangle=140)
    plt.title("\n\n::OCTOBER::\n")
    plt.axis('equal')
    plt.show()
    
     #PIE CHART "NOVEMBER"
    labels = 'COUNTRY AS A WHOLE', 'NORTH WEST INDIA', 'CENTRAL INDIA', 'SOUTH PENINSULA','EAST & NORTH_EAST INDIA'
    sizes = [14.0,6.2,1.3,56.9,3.3]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','pink']
    explode = (0, 0, 0, 0.1, 0)  # explode 4th slice
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
    autopct='%1.1f%%', shadow=True, startangle=140)
    plt.title("\n\n::NOVEMBER::\n")
    plt.axis('equal')
    plt.show()
    
     #PIE CHART "DECEMBER"
    labels = 'COUNTRY AS A WHOLE', 'NORTH WEST INDIA', 'CENTRAL INDIA', 'SOUTH PENINSULA','EAST & NORTH_EAST INDIA'
    sizes = [6.7,9.3,1.4,14.4,3.0]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','pink']
    explode = (0, 0, 0, 0.1, 0)  # explode 4th slice
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
    autopct='%1.1f%%', shadow=True, startangle=140)
    plt.title("\n\n::DECEMBER::\n")
    plt.axis('equal')
    plt.show()






#--------------------------------------------------------------------------------------

def fun4(b3):
    print("\n...............::Region-Wise Monthly Rainfall Ratio of 2012(Milli Meter) in India::............")
    print("\n\n")
    j10=pd.read_csv('topi.csv')
    print("Data of 2012:::::\n",j10)


b=Button(r, text='2015', width=21,height=3, bg='red',  bd=10, activebackground='green',  highlightcolor='purple', command=lambda:fun1(b)) 
b.grid(row=0,column=3) 


b1=tk.Button(r, text='2014', width=21,height=3,bg='yellow',bd=10, activebackground='green', highlightcolor='purple', command=lambda:fun2(b1)) 
b1.grid(row=3,column=6) 


b2=tk.Button(r, text='2013', width=21,height=3,bg='yellow',bd=10, activebackground='green', highlightcolor='purple', command=lambda:fun3(b2)) 
b2.grid(row=6,column=9) 


b3=tk.Button(r, text='2012', width=21,height=3,bg='red',bd=10, activebackground='green', highlightcolor='purple', command=lambda:fun4(b3)) 
b3.grid(row=9,column=12) 

"""
b4=Button(r, text='2016', width=20,height=3, bg='yellow',  bd=10, activebackground='green',  highlightcolor='purple') 
b4.grid(row=10,column=13) 


b5=Button(r, text='2017', width=20,height=3, bg='orange',  bd=10, activebackground='green',  highlightcolor='purple') 
b5.grid(row=11,column=14) 


b6=Button(r, text='2018', width=20,height=3, bg='red',  bd=10, activebackground='green',  highlightcolor='purple') 
b6.grid(row=12,column=15) 


b7=Button(r, text='2019', width=20,height=3, bg='yellow',  bd=10, activebackground='green',  highlightcolor='purple') 
b7.grid(row=13,column=16) """
r.mainloop()
