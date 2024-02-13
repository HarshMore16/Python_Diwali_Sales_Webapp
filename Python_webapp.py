import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import plotly.express as  px
import seaborn as sns 
col1, col2 = st.columns(2)
with col1:
     st.image("images.png",use_column_width="auto")
with col2:
     st.title(":rainbow[Analysis]")

     
st.divider()
data1=pd.read_csv("Book1.csv")
data=data1[['Product_ID','Gender','Age_Group','Marital_Status','State','Orders','Amount']]
with st.sidebar:
     st.sidebar.info("PARTS OF THE ANALYSIS")
     selected_tab = st.sidebar.radio("Select",["Home","Data","charts","Data Summary"])
     
if selected_tab == "Data":
     st.sidebar.divider()
     st.sidebar.info("The Add Data tab allows users to input new data, while the Login to See Data tab provides access to view the existing data upon successful authentication.")
     tab1, tab2 = st.tabs(["Add Data","Login"])
     with tab1:
          col3, col4 =st.columns(2)
          with col3:
               x1=st.text_input("Enter Product_ID")
               x3=st.selectbox("Age_Group",("Select","0-17","18-25","26-35","36-45","46-50","55+"))
               x5=st.selectbox("State",["Maharashtra", "Andhra Pradesh","Uttar Pradesh","Karnataka","Gujarat","Himachal Pradesh","Delhi","Jharkhand","Kerala","Haryana","Madhya Pradesh","Bihar","Rajasthan","Uttarakhand","Telangana","Punjab"])
               x7=st.text_input("Amount")
          with col4:
               x2=st.selectbox("Gender",("Select","M","F"))
               x4=st.selectbox("Marital_Status,0(Unmarried),1(Married)",(0,1))
               x6=st.text_input("Orders")
     
         
     with tab2:
        x=st.text_input("Enter Username")
        y=st.text_input("Enter Password")
        if x=="harsh" and y=="Harsh@12345":
               st.write(":green[login succesful!!]")
               new_row={'Product_ID':x1,'Gender':x2,'Age_Group':x3,'Marital_Status':x4,'State':x5,'Orders':x6,'Amount':x7}
               data=data.append(new_row, ignore_index=True)
               
               st.table(data[::-1])
        else :
             st.write("enter valid username and password")
elif selected_tab == "Data Summary":
     st.sidebar.divider()
     st.sidebar.info("Provides the Short & Sweet summary of data")
     selected_column=st.multiselect("Columns",['Product_ID','Gender','Age_Group','Marital_Status','State','Orders','Amount'])
     st.write(data[selected_column].describe())
     st.subheader("This is type of selcted Columns")
     st.info( type(data[selected_column[0]]))

elif selected_tab == "charts":
     st.sidebar.divider()
     st.sidebar.info("Unlock profound insights from your data through the power of compelling data visualizations.")
     col6, col7 = st.columns(2)
     with col6:
          Age_Group_pie = data["Age_Group"].value_counts().sort_values(ascending= False)
          fig_Age_Group_pie = px.pie(values=Age_Group_pie, names=Age_Group_pie.index,title="Pie chart of Age_Groups",labels={} )
     col6.plotly_chart(fig_Age_Group_pie, use_container_width=True)
     with col7:
          Gender_pie = data["Gender"].value_counts()
          fig_Gender_pie = px.pie(values=Gender_pie, names=Gender_pie.index,title="Pie chart of Gender",labels={} )
     col7.plotly_chart(fig_Gender_pie,use_container_width=True)
     st.divider()
     st.line_chart(data["Amount"])
     st.divider()
     Orders_states=data.groupby(["State"], as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False)
     fig2=px.bar(Orders_states,x='State',y='Orders',title="Bar charts Of Orders")
     st.plotly_chart(fig2)
     st.divider()
     Orders_Gender=data.groupby(["Gender"], as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False)
     fig3=px.bar(Orders_Gender,x='Gender',y='Orders',title="Bar charts Of Orders")
     st.plotly_chart(fig3)
     st.divider()
     Amount_State=data.groupby(["State"], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
     fig4=px.bar(Amount_State,x='State',y='Amount',title="Bar charts Of Orders")
     st.plotly_chart(fig4)


else:
     st.sidebar.divider()
     st.sidebar.info("Choose the option that captivates your interest.")
     selected_tab="Home"
     
     col10,col12,col13=st.columns(3)
     with col10:
          N=data["Amount"].mean()
          st.metric(label="Average diwali sale",value=N.round(2))
     with col12:
          L=data['Orders'].sum()
          st.metric(label="Total Orders",value=L)
     with col13:
          p=data["Amount"].sum()
         
          st.metric(label="Total Sales in Diwali",value=int(p))      


             
          
         