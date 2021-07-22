import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

#recup des données
data=pd.read_csv("https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv")
data["continent_color"]=data["continent"].replace(' US.',"cornflowerblue")
data["continent_color"]=data["continent_color"].replace(' Europe.',"darkorange")
data["continent_color"]=data["continent_color"].replace(' Japan.',"yellowgreen")

st.title("Challenge")

st.header("Objectives")
st.write("From the motors dataset, show correlation and distribution analyses trought different visualizations and comments.")
st.write("Add different button to filter the data by region")

st.header("A correletion matrix of all the data showing the distribution and the correlation between the traits")

fig=sns.pairplot(data,hue="continent")
st.pyplot(fig)
st.write("The color legend corresponds to the continent.")

st.header("A positive correlation, when the weight increase the hp also increase")

fig2 = plt.figure()
ax = fig2.add_subplot(1,1,1)
ax.scatter(data=data,x="weightlbs",y="hp",marker="+",color="continent_color")
ax.set_title("weight vs hp")
ax.set_xlabel("Weight in lbs")
ax.set_ylabel("hp")
st.write(fig2)


st.header("A negative correlation, when the weight increase the mpg decrease")

fig3 = plt.figure()
ax = fig3.add_subplot(1,1,1)
ax.scatter(data=data,x="weightlbs",y="mpg",marker="*",color="continent_color")
ax.set_title("weight vs mpg")
ax.set_xlabel("Weight in lbs")
ax.set_ylabel("mpg")
st.write(fig3)


st.header("To go further, we can select the plot and the continent")
select_plot=st.radio("select a plot",["pairplot","weight vs hp","weight vs mpg"])
select_continent=st.radio('select a continent',[' US.',' Europe.',' Japan.'])

if select_plot == "pairplot":
    fig=sns.pairplot(data[data["continent"]==select_continent])
    st.pyplot(fig)

if select_plot == "weight vs hp":
    fig2 = plt.figure()
    ax = fig2.add_subplot(1,1,1)
    ax.scatter(data=data[data["continent"]==select_continent],x="weightlbs",y="hp",marker="+",color="continent_color")
    ax.set_title("weight vs hp")
    ax.set_xlabel("Weight in lbs")
    ax.set_ylabel("hp")
    st.write(fig2)
    
if select_plot == "weight vs mpg":
    fig4 = plt.figure()
    ax = fig4.add_subplot(1,1,1)
    ax.scatter(data=data[data["continent"]==select_continent],x="weightlbs",y="mpg",marker="*",color="continent_color")
    ax.set_title("weight vs mpg")
    ax.set_xlabel("Weight in lbs")
    ax.set_ylabel("mpg")
    st.write(fig4)