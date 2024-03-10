import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

print("\033[1;36;40m╔════════════════════════════════════════════════════╗")
print("║ \033[1;35m🌦️ 💧 \033[1;33mWeather and Air Quality Index Analysis \033[1;35m💧 🌦️ \033[1;36m║")
print("╚════════════════════════════════════════════════════╝\033[0;0m")
city_choices=[]
print("\n")

print("COMPARISION BETWEEN THE 5 MAJOR CITIES OF INDIA") 
print("\nSelect any two cities to compare their attributes") 

while(1):
    print("\nSELECT THE CITY")
    
    print("\n1.Bangalore\n2.Chennai\n3.Delhi\n4.Jaipur\n5.Mumbai\nAfter choosing 2 cities , press 1 - 5 for Done")
    c1=input("\nEnter your choice : ")

    if c1<'1' or c1>'5':
        print("\nEnter a valid choice from 0-5")
    elif len(city_choices)==2:
        break 
    else:    
        city_choices.append(c1)

if '1' in city_choices and '2' in city_choices:
    w1 = pd.read_csv('Bangalore.csv')
    w2 = pd.read_csv('Chennai.csv')

elif '1' in city_choices and '3' in city_choices:
    w1 = pd.read_csv('Bangalore.csv')
    w2 = pd.read_csv('Delhi.csv')

elif '1' in city_choices and '4' in city_choices:
    w1 = pd.read_csv('Bangalore.csv')
    w2 = pd.read_csv('Jaipur.csv')

elif '1' in city_choices and '5' in city_choices:
    w1 = pd.read_csv('Bangalore.csv')
    w2 = pd.read_csv('Mumbai.csv')

elif '2' in city_choices and '3' in city_choices:
    w1 = pd.read_csv('Chennai.csv')
    w2 = pd.read_csv('Delhi.csv')

elif '2' in city_choices and '4' in city_choices:
    w1 = pd.read_csv('Chennai.csv')
    w2 = pd.read_csv('Jaipur.csv')

elif '2' in city_choices and '5' in city_choices:
    w1 = pd.read_csv('Chennai.csv')
    w2 = pd.read_csv('Mumbai.csv')

elif '3' in city_choices and '4' in city_choices:
    w1 = pd.read_csv('Delhi.csv')
    w2 = pd.read_csv('Jaipur.csv')

elif '3' in city_choices and '5' in city_choices:
    w1 = pd.read_csv('Delhi.csv')
    w2 = pd.read_csv('Mumbai.csv')

elif '4' in city_choices and '5' in city_choices:
    w1 = pd.read_csv('Jaipur.csv')
    w2 = pd.read_csv('Mumbai.csv')
else:
    print("Invalid city combination")

title_mapping = {
        '1': 'Bangalore',
        '2': 'Chennai',
        '3': 'Delhi',
        '4': 'Jaipur',
        '5': 'Mumbai'
    }

selected_cities1 = [title_mapping[city] for city in city_choices[:1]]
selected_cities2 = [title_mapping[city] for city in city_choices[1:]] 

title1 = ", ".join(selected_cities1)
title2 = ", ".join(selected_cities2)

while(1):
    print("\n1.TEMPERATURE COMPARISION\n2.PM INDEX COMPARISION\n3.POLLUTANTS COMPARISION\n4.AQI\n5.EXIT")
    choice=int(input("ENTER YOUR CHOICE : "))
    if(choice==1):
        tempcolm = ['tavg', 'tmin', 'tmax']
        selected_columns1 = w1[tempcolm]
        selected_columns2 = w2[tempcolm]

        fig1=px.line(selected_columns1,title=title1)
        fig2=px.line(selected_columns2,title=title2)

        fig1.update_layout(xaxis=dict(range=[0, 900]))
        fig2.update_layout(xaxis=dict(range=[0, 900]))

        fig1.update_xaxes(title='Days')
        fig1.update_yaxes(title='Temperature')

        fig2.update_xaxes(title='Days')
        fig2.update_yaxes(title='Temperature')

        fig1.add_shape(type="line", x0=0, x1=900, y0=35, y1=35, line=dict(color="red", width=2))
        fig2.add_shape(type="line", x0=0, x1=900, y0=35, y1=35, line=dict(color="red", width=2))

        fig1.show()
        fig2.show()

    elif(choice==2):
        pmcolm=['pm2_5','pm10']

        pm_columns1=w1[pmcolm]
        pm_columns2=w2[pmcolm]
        
        pm1=px.line(pm_columns1,title=title1)
        pm2=px.line(pm_columns2,title=title2)

        pm1.update_layout(xaxis=dict(range=[0, 500]))
        pm2.update_layout(xaxis=dict(range=[0, 500]))

        pm1.update_xaxes(title='Days')
        pm1.update_yaxes(title='PM INDEX')

        pm2.update_xaxes(title='Days')
        pm2.update_yaxes(title='PM INDEX')

        pm1.show()
        pm2.show()
    elif(choice==3):
        polcolm=['no','no2','so2']

        polselected1=w1[polcolm]
        polselected2=w2[polcolm]

        pol1=px.line(polselected1,title=title1)
        pol2=px.line(polselected2,title=title2)

        pol1.update_layout(xaxis=dict(range=[0, 500]))
        pol2.update_layout(xaxis=dict(range=[0, 500]))

        pol1.update_xaxes(title='Days')
        pol1.update_yaxes(title='POLLUTANTS INTENSITY')

        pol2.update_xaxes(title='Days')
        pol2.update_yaxes(title='POLLUTANTS INTENSITY')

        pol1.show()
        pol2.show()


    if choice == 4:
        aqicol = ['aqi']

        aqiselected1 = w1[aqicol]
        aqiselected2 = w2[aqicol]

        fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, linewidth=0.8, edgecolor='black')

        ax1.bar(range(len(aqiselected1)), aqiselected1['aqi'], label=title1)
        ax1.setx_label('Days')
        ax1.set_ylabel('AQI')
        ax1.set_xlim(0, 50)
        ax1.set_ylim(0, 8)

        
        ax2.bar(range(len(aqiselected2)), aqiselected2['aqi'], label=title2)
        ax2.set_ylabel('AQI')
        ax2.set_xlabel('Days')
        ax2.set_xlim(0, 50)
        ax2.set_ylim(0, 8) 

        ax1.axhline(y=1, color='green', linestyle='--', linewidth=2, label='Safe')
        ax1.axhline(y=3, color='orange', linestyle='--', linewidth=2, label='Moderate')
        ax1.axhline(y=4.5, color='red', linestyle='--', linewidth=2, label='High')

        ax2.axhline(y=1, color='green', linestyle='--', linewidth=2, label='Safe')
        ax2.axhline(y=3, color='orange', linestyle='--', linewidth=2, label='Moderate')
        ax2.axhline(y=4.5, color='red', linestyle='--', linewidth=2, label='High')

        ax1.legend(loc='upper right')
        ax2.legend(loc='upper right')

        fig.suptitle('AQI Comparison between '+title1+' and '+title2)
        plt.show()

    elif(choice==5):
        print("\nExiting.....")
        exit(0)
    else:
        print("\nEnter a valid choice from 1-4")




