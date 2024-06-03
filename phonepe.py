import streamlit as st
from streamlit_option_menu import option_menu
import psycopg2
import pandas as pd
import plotly.express as px
import requests
import json
from PIL import Image
from database import queries

# Dataframe creation 

#sql CONNECTION

mydb= psycopg2.connect(host= 'localhost',
                        user= 'postgres',
                        password= 'Joshie@0910',
                        database= 'phonepe_data',
                        port= '5432')
cursor= mydb.cursor()

#aggregated_insurance_df

#cursor.execute('SELECT * FROM aggregated_insurance')
# mydb.commit()
# table1= cursor.fetchall()

# Aggr_insurance= pd.DataFrame(table1, columns=('States', 'Years', 'Quarter', 'Transaction_type',
#                                               'Transaction_count', 'Transaction_amount'))

#aggregated_transaction_df

# cursor.execute('SELECT * FROM aggregated_transaction')
# mydb.commit()
# table2= cursor.fetchall()

# Aggr_transaction= pd.DataFrame(table2, columns=('States', 'Years', 'Quarter', 'Transaction_type',
#                                               'Transaction_count', 'Transaction_amount'))

# #aggregated_users_df

# cursor.execute('SELECT * FROM aggregated_users')
# mydb.commit()
# table3= cursor.fetchall()

# Aggr_users= pd.DataFrame(table3, columns=('States', 'Years', 'Quarter', 'Brand',
#                                               'Transaction_count', 'Percentage'))

# #map_insurance_df

# cursor.execute('SELECT * FROM map_insurance')
# mydb.commit()
# table4= cursor.fetchall()

# Map_insurance= pd.DataFrame(table4, columns=('States', 'Years', 'Quarter', 'Districts',
#                                               'Transaction_count', 'Transaction_amount'))

# #map_transaction_df

# cursor.execute('SELECT * FROM map_transaction')
# mydb.commit()
# table5= cursor.fetchall()

# Map_transaction= pd.DataFrame(table5, columns=('States', 'Years', 'Quarter', 'Districts',
#                                               'Transaction_count', 'Transaction_amount'))

# #map_users_df

# cursor.execute('SELECT * FROM map_users')
# mydb.commit()
# table6= cursor.fetchall()

# Map_users= pd.DataFrame(table6, columns=('States', 'Years', 'Quarter', 'Districts',
#                                               'RegisteredUsers', 'AppOpens'))

# #top_insurance_df

# cursor.execute('SELECT * FROM top_insurance')
# mydb.commit()
# table7= cursor.fetchall()

# Top_insurance= pd.DataFrame(table7, columns=('States', 'Years', 'Quarter', 'Pincodes',
#                                               'Transaction_count', 'Transaction_amount'))

# #top_transaction_df

# cursor.execute('SELECT * FROM top_transaction')
# mydb.commit()
# table8= cursor.fetchall()

# Top_transaction= pd.DataFrame(table8, columns=('States', 'Years', 'Quarter', 'Pincodes',
#                                               'Transaction_count', 'Transaction_amount'))

# #top_users_df

# cursor.execute('SELECT * FROM top_users')
# mydb.commit()
# table9= cursor.fetchall()

# Top_users= pd.DataFrame(table9, columns=('States', 'Years', 'Quarter', 'Pincodes',
#                                               'Registered_users'))

# #Transaction Year based
# def Transaction_amount_count_Y(table, column_name, column_value):

#     results= queries.query_table_by_column(table, column_name, column_value)

#     tacy= pd.DataFrame(results, columns=('States', 'Years', 'Quarter', 'Districts',
#                                               'RegisteredUsers', 'AppOpens'))
    
#     tacy.reset_index(drop = True, inplace = True)

#     tacyg= tacy.groupby('States')[['Transaction_count','Transaction_amount']].sum()
#     tacyg.reset_index(inplace = True)

#     col1, col2 =st.columns(2)
    
#     with col1:
#         fig_amount= px.bar(tacyg, x='States', y='Transaction_amount', title= f'{column_value} TRANSACTION AMOUNT',
#                         color_discrete_sequence= px.colors.sequential.Plasma, height= 650, width= 600)
#         st.plotly_chart(fig_amount)

#     with col2:
#         fig_count= px.bar(tacyg, x='States', y='Transaction_amount', title= f'{column_value} TRANSACTION COUNT',
#                         color_discrete_sequence= px.colors.sequential.Jet_r, height= 650, width= 600)
#         st.plotly_chart(fig_count)

#     col1, col2 =st.columns(2)

#     url= "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
#     response= requests.get(url)
#     data1= json.loads(response.content)

#     states_name=[]

#     for feature in data1['features']:
#         states_name.append(feature['properties']['ST_NM'])

#     states_name.sort()

#     with col1:
#         fig_india1= px.choropleth(tacyg, geojson=data1, locations='States', featureidkey= 'properties.ST_NM',
#                                 color= 'Transaction_amount', color_continuous_scale= 'Rainbow',
#                                 range_color= (tacyg['Transaction_amount'].min(), tacyg['Transaction_amount'].max()),
#                                 hover_name= 'States', title= f'{column_value} TRANSACTION AMOUNT', fitbounds= 'locations',
#                                 height= 600, width= 600)
#         fig_india1.update_geos(visible= False)
#         st.plotly_chart(fig_india1)

#     with col2:
#         fig_india2= px.choropleth(tacyg, geojson=data1, locations='States', featureidkey= 'properties.ST_NM',
#                                 color= 'Transaction_count', color_continuous_scale= 'Rainbow',
#                                 range_color= (tacyg['Transaction_count'].min(), tacyg['Transaction_count'].max()),
#                                 hover_name= 'States', title= f'{column_value} TRANSACTION COUNT', fitbounds= 'locations',
#                                 height= 600, width= 600)
#         fig_india2.update_geos(visible= False)
#         st.plotly_chart(fig_india2)

#     return tacy

# #Transaction Quarter based
# def Transaction_amount_count_Q(table, column_name, column_value):

#     results= queries.query_table_by_column(table, column_name, column_value)

#     tacy= pd.DataFrame(results, columns=('States', 'Years', 'Quarter', 'Districts',
#                                               'RegisteredUsers', 'AppOpens'))

#     tacyg= tacy.groupby('States')[['Transaction_count','Transaction_amount']].sum()
#     tacyg.reset_index(inplace = True)

#     col1, col2 =st.columns(2)

#     with col1:
#         fig_amount= px.bar(tacyg, x='States', y='Transaction_amount', title= f'YEAR {tacy['Years'].min()} QUARTER {column_value} TRANSACTION AMOUNT',
#                         color_discrete_sequence= px.colors.sequential.Plasma, height= 650, width= 600)
#         st.plotly_chart(fig_amount)

#     with col2:
#         fig_count= px.bar(tacyg, x='States', y='Transaction_amount', title= f'YEAR {tacy['Years'].min()} QUARTER {column_value} TRANSACTION COUNT',
#                         color_discrete_sequence= px.colors.sequential.Jet_r, height= 650, width= 600)
#         st.plotly_chart(fig_count)

#     col1, col2 =st.columns(2)

#     url= "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
#     response= requests.get(url)
#     data1= json.loads(response.content)

#     states_name=[]

#     for feature in data1['features']:
#         states_name.append(feature['properties']['ST_NM'])

#     states_name.sort()

#     with col1:
#         fig_india1= px.choropleth(tacyg, geojson=data1, locations='States', featureidkey= 'properties.ST_NM',
#                                 color= 'Transaction_amount', color_continuous_scale= 'Rainbow',
#                                 range_color= (tacyg['Transaction_amount'].min(), tacyg['Transaction_amount'].max()),
#                                 hover_name= 'States', title= f'YEAR {tacy['Years'].min()} QUARTER {column_value} TRANSACTION AMOUNT', fitbounds= 'locations',
#                                 height= 600, width= 600)
#         fig_india1.update_geos(visible= False)
#         st.plotly_chart(fig_india1)

#     with col2:
#         fig_india2= px.choropleth(tacyg, geojson=data1, locations='States', featureidkey= 'properties.ST_NM',
#                                 color= 'Transaction_count', color_continuous_scale= 'Rainbow',
#                                 range_color= (tacyg['Transaction_count'].min(), tacyg['Transaction_count'].max()),
#                                 hover_name= 'States', title= f'YEAR {tacy['Years'].min()} QUARTER {column_value} TRANSACTION COUNT', fitbounds= 'locations',
#                                 height= 600, width= 600)
#         fig_india2.update_geos(visible= False)
#         st.plotly_chart(fig_india2)

#     return tacy

def Transaction_amount_count(table, column_name, column_value):

    results= queries.query_table_by_column(table, column_name, column_value)

    tacy= pd.DataFrame(results)

    tacyg= tacy.groupby('States')[['Transaction_count','Transaction_amount']].sum()
    tacyg.reset_index(inplace = True)

    col1, col2 =st.columns(2)

    bar_title1= bar_title2= ''

    if column_name == 'years':
        bar_title1= f'{column_value} TRANSACTION AMOUNT'
        bar_title2= f'{column_value} TRANSACTION COUNT'
    
    elif column_name == 'quarter':
        bar_title1= f'YEAR {tacy['Years'].min()} QUARTER {column_value} TRANSACTION AMOUNT'
        bar_title2= f'YEAR {tacy['Years'].min()} QUARTER {column_value} TRANSACTION COUNT'
        

    with col1:
        fig_amount= px.bar(tacyg, x='States', y='Transaction_amount', title= bar_title1,
                        color_discrete_sequence= px.colors.sequential.Plasma, height= 650, width= 600)
        st.plotly_chart(fig_amount)

    with col2:
        fig_count= px.bar(tacyg, x='States', y='Transaction_amount', title= bar_title2,
                        color_discrete_sequence= px.colors.sequential.Jet_r, height= 650, width= 600)
        st.plotly_chart(fig_count)

    col1, col2 =st.columns(2)

    url= "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    response= requests.get(url)
    data1= json.loads(response.content)

    states_name=[]

    for feature in data1['features']:
        states_name.append(feature['properties']['ST_NM'])

    states_name.sort()

    with col1:
        fig_india1= px.choropleth(tacyg, geojson=data1, locations='States', featureidkey= 'properties.ST_NM',
                                color= 'Transaction_amount', color_continuous_scale= 'Rainbow',
                                range_color= (tacyg['Transaction_amount'].min(), tacyg['Transaction_amount'].max()),
                                hover_name= 'States', title= bar_title1, fitbounds= 'locations',
                                height= 600, width= 600)
        fig_india1.update_geos(visible= False)
        st.plotly_chart(fig_india1)

    with col2:
        fig_india2= px.choropleth(tacyg, geojson=data1, locations='States', featureidkey= 'properties.ST_NM',
                                color= 'Transaction_count', color_continuous_scale= 'Rainbow',
                                range_color= (tacyg['Transaction_count'].min(), tacyg['Transaction_count'].max()),
                                hover_name= 'States', title= bar_title2, fitbounds= 'locations',
                                height= 600, width= 600)
        fig_india2.update_geos(visible= False)
        st.plotly_chart(fig_india2)

    return tacy

##Transaction type
def Agg_tran_transaction_type(table, column_name, column_value):

    results= queries.query_table_by_column(table, column_name, column_value)
    
    tacy= pd.DataFrame(results)

    tacyg= tacy.groupby('States')[['Transaction_count','Transaction_amount']].sum()
    tacyg.reset_index(inplace = True)

    col1, col2 =st.columns(2)

    with col1:
        fig_pie1= px.pie(data_frame= tacyg, names= 'Transaction_type', values= 'Transaction_amount',
                            width= 600, title= f'{results.upper()} TRANSACTION AMOUNT', hole= 0.5, color_discrete_sequence= px.colors.sequential.Blackbody)
        st.plotly_chart(fig_pie1)
    with col2:
        fig_pie2= px.pie(data_frame= tacyg, names= 'Transaction_type', values= 'Transaction_count',
                            width= 600, title= f'{results.upper()} TRANSACTION COUNT', hole= 0.5, color_discrete_sequence= px.colors.sequential.Blackbody)
        st.plotly_chart(fig_pie2)

#Aggregated user analysis
def Agg_user_plot(table, column_name, column_value):

    results= queries.query_table_by_column(table, column_name, column_value)

    aguy= pd.DataFrame(results)

    aguyg= aguy.groupby('Brand')['Transaction_count'].sum()
    aguyg.reset_index(inplace= True)

    fig_bar1= px.bar(aguyg, x= 'Brand', y= 'Transaction_count', title= f'BRANDS AND TRANSACTION COUNT FOR THE YEAR {column_value}',
                    width= 1000, color_discrete_sequence= px.colors.sequential.Agsunset, hover_name= 'Brand')
    st.plotly_chart(fig_bar1)

    fig_bar2= px.bar(aguyg, x= 'Brand', y= 'Transaction_count', title= f'BRANDS AND TRANSACTION COUNT FOR QUARTER {column_value}',
                    width= 1000, color_discrete_sequence= px.colors.sequential.Sunsetdark, hover_name= 'Brand')
    st.plotly_chart(fig_bar2)

    fig_line1= px.line(aguyg, x= 'Brand', y= 'Transaction_count', hover_data= 'Percentage',
                        title= f'{column_value.upper()} BRANDS, TRANSACTION COUNT, PERCENTAGE', width= 1000, markers= True,
                        color_discrete_sequence= px.colors.sequential.haline_r)
    
    st.plotly_chart(fig_line1)

    return aguy

#Aggregated user analysis quarter
# def agg_user_plot2(df, quarter):
#     aguq= df[df['Quarter'] == quarter]
#     aguq.reset_index(drop= True, inplace= True)

#     aguq_g= pd.DataFrame(aguq.groupby('Brand')['Transaction_count'].sum())
#     aguq_g.reset_index(inplace= True)

#     fig_bar1= px.bar(aguq_g, x= 'Brand', y= 'Transaction_count', title= f'BRANDS AND TRANSACTION COUNT FOR QUARTER {quarter}',
#                     width= 1000, color_discrete_sequence= px.colors.sequential.Sunsetdark, hover_name= 'Brand')
#     st.plotly_chart(fig_bar1)

#     return aguq

#Aggregated user analysis 3
# def agg_user_plot3(df, state):
#     agus= df[df['States'] == state]
#     agus.reset_index(drop= True, inplace= True)

#     fig_line1= px.line(agus, x= 'Brand', y= 'Transaction_count', hover_data= 'Percentage',
#                         title= f'{state.upper()} BRANDS, TRANSACTION COUNT, PERCENTAGE', width= 1000, markers= True,
#                         color_discrete_sequence= px.colors.sequential.haline_r)
    
#     st.plotly_chart(fig_line1)

#map insurance district
def map_insurance_District(table, column_name, column_value):

    results= queries.query_table_by_column(table, column_name, column_value)

    tacy= pd.DataFrame(results)

    tacyg= tacy.groupby('Districts')[['Transaction_count','Transaction_amount']].sum()
    tacyg.reset_index(inplace = True)

    col1, col2 =st.columns(2)

    with col1:
        fig_bar1= px.bar(tacyg, x= 'Transaction_amount', y= 'Districts', orientation= 'h', height= 600,
                        title= f'{column_value.upper()} DISTRICT AND TRANSACTION AMOUNT', color_discrete_sequence= px.colors.sequential.Electric)
        st.plotly_chart(fig_bar1)

    with col2:
        fig_bar2= px.bar(tacyg, x= 'Transaction_count', y= 'Districts', orientation= 'h', height= 600,
                        title= f'{column_value.upper()} DISTRICT AND TRANSACTION COUNT', color_discrete_sequence= px.colors.sequential.Emrld_r)
        st.plotly_chart(fig_bar2)

#Map user analysis1
def map_user_plot(table, column_name, column_value):

    results= queries.query_table_by_column(table, column_name, column_value)
    
    muy= pd.DataFrame(results)

    muyg= muy.groupby('States')[['RegisteredUsers', 'AppOpens']].sum()
    muyg.reset_index(inplace= True)

    fig_line1= px.line(muyg, x= 'States', y= ['RegisteredUsers', 'AppOpens'], color_discrete_sequence= px.colors.sequential.Rainbow_r, 
                        title= f'{column_value} REFISTERED USERS, APPOPENS', width= 1000, height=800, markers= True)
    st.plotly_chart(fig_line1)

    fig_line2= px.line(muyg, x= 'States', y= ['RegisteredUsers', 'AppOpens'], color_discrete_sequence= px.colors.sequential.Blackbody_r,
                        title= f'QUARTER {column_value} REFISTERED USERS, APPOPENS', width= 1000, height=800, markers= True)
    st.plotly_chart(fig_line2)

    col1, col2= st.columns(2)

    with col1:
        fig_MU_bar1= px.bar(muyg, x= 'RegisteredUsers', y= 'Districts', orientation= 'h',
                            title= f'{column_value.upper()} REGISTERED USER', height= 800, color_discrete_sequence= px.colors.sequential.Blugrn_r)
        st.plotly_chart(fig_MU_bar1)

    with col2:
        fig_MU_bar2= px.bar(muyg, x= 'AppOpens', y= 'Districts', orientation= 'h',
                            title= f'{column_value.upper()} APPOPENS', height= 800, color_discrete_sequence= px.colors.sequential.Brwnyl)
        st.plotly_chart(fig_MU_bar2)

    return muy

#Map user analysis2
# def map_user_plot2(df, quarter):
#     muq= df[df['Quarter'] == quarter]
#     muq.reset_index(drop= True, inplace= True)

#     muqg= muq.groupby('States')[['RegisteredUsers', 'AppOpens']].sum()
#     muqg.reset_index(inplace= True)

#     fig_line1= px.line(muqg, x= 'States', y= ['RegisteredUsers', 'AppOpens'], color_discrete_sequence= px.colors.sequential.Blackbody_r,
#                         title= f'QUARTER {quarter} REFISTERED USERS, APPOPENS', width= 1000, height=800, markers= True)
#     st.plotly_chart(fig_line1)

#     return muq

# #Map user analysis3
# def map_user_plot3(df, states):
#     muyqs= df[df['States'] == states]
#     muyqs.reset_index(drop= True, inplace= True)

#     col1, col2= st.columns(2)

#     with col1:
#         fig_MU_bar1= px.bar(muyqs, x= 'RegisteredUsers', y= 'Districts', orientation= 'h',
#                             title= f'{states.upper()} REGISTERED USER', height= 800, color_discrete_sequence= px.colors.sequential.Blugrn_r)
#         st.plotly_chart(fig_MU_bar1)

#     with col2:
#         fig_MU_bar2= px.bar(muyqs, x= 'AppOpens', y= 'Districts', orientation= 'h',
#                             title= f'{states.upper()} APPOPENS', height= 800, color_discrete_sequence= px.colors.sequential.Brwnyl)
#         st.plotly_chart(fig_MU_bar2)

#Top insurance analysis 1
def top_insurance_plot(table, column_name, column_value):
    
    results= queries.query_table_by_column(table, column_name, column_value)

    tiy= pd.DataFrame(results)
    col1, col2= st.columns(2)

    with col1:
        fig_Ti_bar1= px.bar(tiy, x= 'Quarter', y= 'Transaction_amount', hover_data= 'Pincodes',
                            title= 'TRANSACTION AMOUNT', height= 800, color_discrete_sequence= px.colors.sequential.Oranges_r)
        st.plotly_chart(fig_Ti_bar1)

    with col2:
        fig_Ti_bar2= px.bar(tiy, x= 'Quarter', y= 'Transaction_count', hover_data= 'Pincodes',
                            title= 'TRANSACTION COUNT', height= 800, color_discrete_sequence= px.colors.sequential.Pinkyl)
        st.plotly_chart(fig_Ti_bar2)

def top_user_plot(table, column_name, column_value):

    results= queries.query_table_by_column(table, column_name, column_value)

    tuy= pd.DataFrame(results)

    tuyg= tuy.groupby(['States', 'Quarter'])['Registered_users'].sum()
    tuyg.reset_index(inplace= True)

    fig_top_bar1= px.bar(tuyg, x= 'States', y= 'Registered_users', color= 'Quarter', hover_name= 'States',
                        width =1000, height= 800, color_discrete_sequence= px.colors.sequential.Purples)
    st.plotly_chart(fig_top_bar1)

    fig_top_bar2= px.bar(tuy, x= 'Quarter', y= 'Registered_users', title= 'REFITERED USERS, PINCODES, QUARTER',
                        width= 1000, height= 800, color= 'Registered_users', hover_data= 'Pincodes',
                        color_continuous_scale= px.colors.sequential.Redor_r)
    st.plotly_chart(fig_top_bar2)

    return tuy

# def top_user_plot2(df, state):
#     tuys= df[df['States'] == state]
#     tuys.reset_index(drop= True, inplace= True)

#     fig_top_bar2= px.bar(tuys, x= 'Quarter', y= 'Registered_users', title= 'REFITERED USERS, PINCODES, QUARTER',
#                         width= 1000, height= 800, color= 'Registered_users', hover_data= 'Pincodes',
#                         color_continuous_scale= px.colors.sequential.Redor_r)
#     st.plotly_chart(fig_top_bar2)


def top_chart_transaction_amount(table_name):
    mydb= psycopg2.connect(host= 'localhost',
                            user= 'postgres',
                            password= 'Joshie@0910',
                            database= 'phonepe_data',
                            port= '5432')
    cursor= mydb.cursor()

    col1, col2= st.columns(2)

    #plot1
    query1= f'''select states, sum(transaction_amount) as transaction_amount 
                from {table_name}
                group by states
                order by transaction_amount desc 
                limit 10;'''

    cursor.execute(query1)
    table= cursor.fetchall()
    mydb.commit()

    df_1= pd.DataFrame(table, columns= ('states', 'transaction_amount'))

    with col1:
        fig_1= px.bar(df_1, x='states', y='transaction_amount', title= 'TOP 10 OF TRANSACTION AMOUNT', hover_data= 'states',
                            color_discrete_sequence= px.colors.sequential.dense_r, height= 650, width= 600)
        st.plotly_chart(fig_1)

    #plot2
    query2= f'''select states, sum(transaction_amount) as transaction_amount 
                from {table_name} 
                group by states
                order by transaction_amount
                limit 10;'''

    cursor.execute(query2)
    table= cursor.fetchall()
    mydb.commit()
    with col2:
        df_2= pd.DataFrame(table, columns= ('states', 'transaction_amount'))

        fig_2= px.bar(df_2, x='states', y='transaction_amount', title= 'LAST 10 OF TRANSACTION AMOUNT', hover_data= 'states',
                            color_discrete_sequence= px.colors.sequential.Mint_r, height= 650, width= 600)
        st.plotly_chart(fig_2)

    #plot3
    query3= f'''select states, avg(transaction_amount) as transaction_amount 
                from {table_name} 
                group by states
                order by transaction_amount;'''

    cursor.execute(query3)
    table= cursor.fetchall()
    mydb.commit()

    df_3= pd.DataFrame(table, columns= ('states', 'transaction_amount'))

    fig_3= px.bar(df_3, x='transaction_amount', y='states', title= 'AVERAGE OF TRANSACTION AMOUNT', hover_data= 'states',
                        color_discrete_sequence= px.colors.sequential.deep_r, height= 800, width= 1000, orientation= 'h')
    st.plotly_chart(fig_3)

#Transaction count top chart
def top_chart_transaction_count(table_name):
    mydb= psycopg2.connect(host= 'localhost',
                            user= 'postgres',
                            password= 'Joshie@0910',
                            database= 'phonepe_data',
                            port= '5432')
    cursor= mydb.cursor()

    #plot1
    query1= f'''select states, sum(transaction_count) as transaction_count 
                from {table_name}
                group by states
                order by transaction_count desc 
                limit 10;'''

    cursor.execute(query1)
    table= cursor.fetchall()
    mydb.commit()

    col1,col2= st.columns(2)

    df_1= pd.DataFrame(table, columns= ('states', 'transaction_count'))

    with col1:
        fig_1= px.bar(df_1, x='states', y='transaction_count', title= 'TOP 10 OF TRANSACTION COUNT', hover_data= 'states',
                            color_discrete_sequence= px.colors.sequential.algae_r, height= 650, width= 600)
        st.plotly_chart(fig_1)

    #plot2
    query2= f'''select states, sum(transaction_count) as transaction_count 
                from {table_name} 
                group by states
                order by transaction_count
                limit 10;'''

    cursor.execute(query2)
    table= cursor.fetchall()
    mydb.commit()

    df_2= pd.DataFrame(table, columns= ('states', 'transaction_count'))

    with col2:
        fig_2= px.bar(df_2, x='states', y='transaction_count', title= 'LSDT 20 OF TRANSACTION COUNT', hover_data= 'states',
                            color_discrete_sequence= px.colors.sequential.Electric_r, height= 650, width= 600)
        st.plotly_chart(fig_2)

    #plot3
    query3= f'''select states, avg(transaction_count) as transaction_count 
                from {table_name} 
                group by states
                order by transaction_count;'''

    cursor.execute(query3)
    table= cursor.fetchall()
    mydb.commit()

    df_3= pd.DataFrame(table, columns= ('states', 'transaction_count'))

    fig_3= px.bar(df_3, x='transaction_count', y='states', title= 'AVERAGE 10 OF TRANSACTION COUNT', hover_data= 'states',
                        color_discrete_sequence= px.colors.sequential.ice_r, height= 800, width= 1000, orientation= 'h')
    st.plotly_chart(fig_3)

#Top chart registered users
def top_chart_registered_users(table_name, state):
    mydb= psycopg2.connect(host= 'localhost',
                            user= 'postgres',
                            password= 'Joshie@0910',
                            database= 'phonepe_data',
                            port= '5432')
    cursor= mydb.cursor()

    #plot1
    query1= f'''Select districts, sum(registeredusers) as registeredusers
                from {table_name}
                where states= '{state}'
                group by districts
                order by registeredusers desc
                limit 10;'''

    cursor.execute(query1)
    table= cursor.fetchall()
    mydb.commit()

    col1,col2= st.columns(2)

    df_1= pd.DataFrame(table, columns= ('districts', 'registeredusers'))

    with col1:
        fig_1= px.bar(df_1, x='districts', y='registeredusers', title= 'TOP 10 OF REGISTERED USERS', hover_data= 'districts',
                            color_discrete_sequence= px.colors.sequential.Purp_r, height= 650, width= 600)
        st.plotly_chart(fig_1)

    #plot2
    query2= f'''Select districts, sum(registeredusers) as registeredusers
                from {table_name}
                where states= '{state}'
                group by districts
                order by registeredusers
                limit 10;'''

    cursor.execute(query2)
    table= cursor.fetchall()
    mydb.commit()

    df_2= pd.DataFrame(table, columns= ('districts', 'registeredusers'))

    with col2:
        fig_2= px.bar(df_2, x='districts', y='registeredusers', title= 'LAST 10 OF REGISTERED USERS', hover_data= 'districts',
                            color_discrete_sequence= px.colors.sequential.Brwnyl_r, height= 650, width= 600)
        st.plotly_chart(fig_2)

    #plot3
    query3= f'''Select districts, avg(registeredusers) as registeredusers
                from {table_name}
                where states= '{state}'
                group by districts
                order by registeredusers;'''

    cursor.execute(query3)
    table= cursor.fetchall()
    mydb.commit()

    df_3= pd.DataFrame(table, columns= ('districts', 'registeredusers'))

    fig_3= px.bar(df_3, x='registeredusers', y='districts', title= 'AVERAGE OF REGISTERED USERS', hover_data= 'districts',
                        color_discrete_sequence= px.colors.sequential.amp_r, height= 800, width= 1000, orientation= 'h')
    st.plotly_chart(fig_3)

#Top chart registered users
def top_chart_appopens(table_name, state):
    mydb= psycopg2.connect(host= 'localhost',
                            user= 'postgres',
                            password= 'Joshie@0910',
                            database= 'phonepe_data',
                            port= '5432')
    cursor= mydb.cursor()

    #plot1
    query1= f'''Select districts, sum(appopens) as appopens
                from {table_name}
                where states= '{state}'
                group by districts
                order by appopens desc
                limit 10;'''

    cursor.execute(query1)
    table= cursor.fetchall()
    mydb.commit()

    col1,col2= st.columns(2)

    df_1= pd.DataFrame(table, columns= ('districts', 'appopens'))

    with col1:
        fig_1= px.bar(df_1, x='districts', y='appopens', title= 'TOP 10 OF APPOPENS', hover_data= 'districts',
                            color_discrete_sequence= px.colors.sequential.Emrld_r, height= 650, width= 600)
        st.plotly_chart(fig_1)

    #plot2
    query2= f'''Select districts, sum(appopens) as appopens
                from {table_name}
                where states= '{state}'
                group by districts
                order by appopens
                limit 10;'''

    cursor.execute(query2)
    table= cursor.fetchall()
    mydb.commit()

    df_2= pd.DataFrame(table, columns= ('districts', 'appopens'))

    with col2:
        fig_2= px.bar(df_2, x='districts', y='appopens', title= 'LAST 10 OF APPOPENS', hover_data= 'districts',
                            color_discrete_sequence= px.colors.sequential.Turbo_r, height= 650, width= 600)
        st.plotly_chart(fig_2)

    #plot3
    query3= f'''Select districts, avg(appopens) as appopens
                from {table_name}
                where states= '{state}'
                group by districts
                order by appopens;'''

    cursor.execute(query3)
    table= cursor.fetchall()
    mydb.commit()

    df_3= pd.DataFrame(table, columns= ('districts', 'appopens'))

    fig_3= px.bar(df_3, x='appopens', y='districts', title= 'AVERAGE OF APPOPENS', hover_data= 'districts',
                        color_discrete_sequence= px.colors.sequential.ice_r, height= 800, width= 1000, orientation= 'h')
    st.plotly_chart(fig_3)

#Top chart registered users
def top_chart_top_users(table_name):
    mydb= psycopg2.connect(host= 'localhost',
                            user= 'postgres',
                            password= 'Joshie@0910',
                            database= 'phonepe_data',
                            port= '5432')
    cursor= mydb.cursor()

    #plot1
    query1= f'''select states, sum(registered_users) as registeredusers
                from {table_name}
                group by states
                order by registeredusers desc
                limit 10;'''

    cursor.execute(query1)
    table= cursor.fetchall()
    mydb.commit()

    col1,col2= st.columns(2)

    df_1= pd.DataFrame(table, columns= ('states', 'registeredusers'))

    with col1:
        fig_1= px.bar(df_1, x='states', y='registeredusers', title= 'TOP 10 OF REGISTERED USERS', hover_data= 'states',
                            color_discrete_sequence= px.colors.sequential.algae_r, height= 650, width= 600)
        st.plotly_chart(fig_1)

    #plot2
    query2= f'''select states, sum(registered_users) as registeredusers
                from {table_name}
                group by states
                order by registeredusers
                limit 10;;'''

    cursor.execute(query2)
    table= cursor.fetchall()
    mydb.commit()

    df_2= pd.DataFrame(table, columns= ('states', 'registeredusers'))

    with col2:
        fig_2=  px.bar(df_2, x='states', y='registeredusers', title= 'LAST 10 OF REGISTERED USERS', hover_data= 'states',
                            color_discrete_sequence= px.colors.sequential.Blugrn_r, height= 650, width= 600)
        st.plotly_chart(fig_2)

    #plot3
    query3= f'''select states, avg(registered_users) as registeredusers
                from {table_name}
                group by states
                order by registeredusers;'''

    cursor.execute(query3)
    table= cursor.fetchall()
    mydb.commit()

    df_3= pd.DataFrame(table, columns= ('states', 'registeredusers'))

    fig_3= px.bar(df_3, x='registeredusers', y='states', title= 'AVERAGE OF REGISTERED USERS', hover_data= 'states',
                        color_discrete_sequence= px.colors.sequential.OrRd_r, height= 800, width= 1000, orientation= 'h')
    st.plotly_chart(fig_3)

#Streamlit part

st.set_page_config(layout= 'wide')
st.title('PHONEPE DATA VISUALIZATION AND EXPLORATION')

with st.sidebar:
    select= option_menu('Main Menu',['HOME', 'DATA EXPLORATION', 'TOP CHARTS'])

if select == 'HOME':
    col1, col2= st.columns(2) 

    with col1:
        st.header('PHONEPE')
        st.subheader("INDIA'S BEST TRANSACTION APP")
        st.markdown('PhonePe is an Indian digital payments and financial technology company')
        st.write('****FEATURES****')
        st.write('****Credit & Debit card linking****')
        st.write('****Bank Balance Check****')
        st.write('****Money Storage****')
        st.write('****Pin Authorization****')
        st.download_button('DOWNLOAD THE APP NOW', "https://www.phonepe.com/app-download/")
    
    with col2:
        st.image(Image.open(r"C:\Users\Jonathan Simon\Desktop\New folder\download.png"), width= 600)

    col3,col4= st.columns(2)
    
    with col3:
        st.image(Image.open(r"C:\Users\Jonathan Simon\Desktop\New folder\download.jpeg"),width=600)

    with col4:
        st.write("****Easy Transactions****")
        st.write("****One App For All Your Payments****")
        st.write("****Your Bank Account Is All You Need****")
        st.write("****Multiple Payment Modes****")
        st.write("****PhonePe Merchants****")
        st.write("****Multiple Ways To Pay****")
        st.write("****1. Direct Transfer & More****")
        st.write("****2. QR Code****")
        st.write("****Earn Great Rewards****")

    col5,col6= st.columns(2)

    with col5:
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.write("****No Wallet Top-Up Required****")
        st.write("****Pay Directly From Any Bank To Any Bank A/C****")
        st.write("****Instantly & Free****")

    with col6:
        st.image(Image.open(r"C:\Users\Jonathan Simon\Desktop\New folder\download 2.jpeg"),width= 600)

elif select == 'DATA EXPLORATION':
    tab1, tab2, tab3= st.tabs(['Aggregated Analysis', 'Map Analysis', 'Top Analysis'])

    with tab1:
        method1= st.radio('Select the Method', ['Insurance Analysis', 'Transaction Analysis', 'User Analysis'])

        if method1 == 'Insurance Analysis':

            col1, col2, col3= st.columns(3)
            yearlist= queries.query_table('aggregated_insurance', 'years')

            with col1:
                years= st.slider('Select the Year',yearlist.min(), yearlist.max(), yearlist.min())
            
            Transaction_amount_count('aggregated_insurance', 'years', years)

            col1, col2, col3= st.columns(3)
            quarterlist= queries.query_table('aggregated_insurance', 'quarter')

            with col1:
                quarters= st.slider('Select the Quarter', quarterlist.min(), quarterlist.max(), quarterlist.min())

            Transaction_amount_count('aggregated_insurance', 'quarter', quarters)

        elif method1 == 'Transaction Analysis':
            
            col1, col2, col3= st.columns(3)
            yearlist= queries.query_table('aggregated_transaction', 'years')

            with col1:
                years= st.slider('Select the Year',yearlist.min(), yearlist.max(),yearlist.min())
            
            Transaction_amount_count('aggregated_transaction', 'years', years)

            col1, col2, col3= st.columns(3)

            statelist= queries.query_table('aggregated_transaction', 'states')
            with col1:
                states= st.selectbox('Select the State', statelist.unique())

            Agg_tran_transaction_type('aggregated_transaction', 'states', states)

            col1, col2, col3= st.columns(3)
           
            quarterlist= queries.query_table('aggregated_transaction', 'quarter')
            with col1:
                quarters= st.slider('Select the Quarter_Ty', quarterlist.min(), quarterlist.max(), quarterlist.min())

            Transaction_amount_count('aggregated_transaction', 'quarters', quarters)

            col1, col2, col3= st.columns(3)

            statelist= queries.query_table('aggregated_transaction', 'states')
            with col1:
                states= st.selectbox('Select the State_Ty', statelist.unique())

            Agg_tran_transaction_type('aggregated_transaction', 'states', states)

        elif method1 == 'User Analysis':

            yearlist= queries.query_table('aggregated_users', 'years')
            col1, col2, col3= st.columns(3)
            with col1:
                years= st.slider('Select the Year_Ua',yearlist.min(), yearlist.max(), yearlist.min())
            
            Agg_user_plot('aggregated_users', 'years', years)

            col1, col2, col3= st.columns(3)
            
            quarterlist= queries.query_table('aggregated_users', 'quarter')
            with col1:
                quarters= st.slider('Select the Quarter', quarterlist.min(), quarterlist.max(), quarterlist.min())

            Agg_user_plot('aggregated_users', 'quarters', quarters)

            col1, col2, col3= st.columns(3)

            statelist= queries.query_table('aggregated_users', 'states')
            with col1:
                states= st.selectbox('Select the State_Ty', statelist.unique())

            Agg_user_plot('aggregated_users', 'quarters', states)
    
    with tab2:
        method2= st.radio('Select the Method', ['Map Insurance', 'Map Transaction', 'Map User'])

        if method2 == 'Map Insurance':
            
            col1, col2, col3= st.columns(3)
            yearlist= queries.query_table('map_insurance', 'years')
            with col1:
                years= st.slider('Select the Year_mi',yearlist.min(), yearlist.max(), yearlist.min())
            
            Transaction_amount_count('map_insurance', 'years', years)

            col1, col2, col3= st.columns(3)

            statelist= queries.query_table('map_insurance', 'states')
            with col1:
                states= st.selectbox('Select the State_mi',statelist.unique())

            map_insurance_District('map_insurance', 'states', states)

            col1, col2, col3= st.columns(3)
           
            quarterlist= queries.query_table('map_insurance', 'quarter')
            with col1:
                quarters= st.slider('Select the Quarter_Mi',quarterlist.min(), quarterlist.max(), quarterlist.min())

            Transaction_amount_count('map_insurance', 'quarters', quarters)

            col1, col2, col3= st.columns(3)

            statelist= queries.query_table('map_insurance', 'states')
            with col1:
                states= st.selectbox('Select the State_Mi', statelist.unique())

            map_insurance_District('map_insurance', 'states', states)

        elif method2 == 'Map Transaction':
            col1, col2, col3= st.columns(3)

            yearlist= queries.query_table('map_transaction', 'years')
            with col1:
                years= st.slider('Select the Year_mt', yearlist.min(), yearlist.max(), yearlist.min())
            
            Transaction_amount_count('map_transaction', 'years', years)

            col1, col2, col3= st.columns(3)

            statelist= queries.query_table('map_transaction', 'states')
            with col1:
                states= st.selectbox('Select the State_mt', statelist.unique())

            map_insurance_District('map_transaction', 'states', states)

            col1, col2, col3= st.columns(3)
           
            quarterlist= queries.query_table('map_transaction', 'quarter')
            with col1:
                quarters= st.slider('Select the Quarter_Mt', quarterlist.min(), quarterlist.max(), quarterlist.min())

            Transaction_amount_count('map_transaction', 'quarters', quarters)

            col1, col2, col3= st.columns(3)

            statelist= queries.query_table('map_transaction', 'states')
            with col1:
                states= st.selectbox('Select the State_Mt', statelist.unique())

            map_insurance_District('map_transaction', 'states', states)

        elif method2 == 'Map User':

            col1, col2, col3= st.columns(3)

            yearlist= queries.query_table('map_users', 'years')
            with col1:
                years= st.slider('Select the Year_mu',yearlist.min(), yearlist.max(), yearlist.min())
            
            map_user_plot('map_users', 'years', years)

            col1, col2, col3= st.columns(3)

            quarterlist= queries.query_table('map_users', 'quarter')
            with col1:
                quarters= st.slider('Select the Quarter_mu', quarterlist.min(), quarterlist.max(), quarterlist.min())

            map_user_plot('map_users', 'quarters', quarters)

            col1, col2, col3= st.columns(3)

            statelist= queries.query_table('map_users', 'states')
            with col1:
                states= st.selectbox('Select the State_mu', statelist.unique())

            map_user_plot('map_users', 'states', states)

    with tab3:
        method3= st.radio('Select the Method', ['Top Insurance', 'Top Transaction', 'Top User'])

        if method3 == 'Top Insurance':

            col1, col2, col3= st.columns(3)

            yearlist= queries.query_table('top_insurance', 'years')
            with col1:
                years= st.slider('Select the Year_ti',yearlist.min(), yearlist.max(), yearlist.min())
            
            Transaction_amount_count('top_insurance', 'years', years)

            col1, col2, col3= st.columns(3)

            statelist= queries.query_table('top_insurance', 'states')
            with col1:
                states= st.selectbox('Select the State_tt', statelist.unique())

            top_insurance_plot('top_insurance', 'states', states)

            col1, col2, col3= st.columns(3)

            quarterlist= queries.query_table('top_insurance', 'quarter')
            with col1:
                quarters= st.slider('Select the Quarter_ti', quarterlist.min(), quarterlist.max(), quarterlist.min())

            Transaction_amount_count('top_insurance', 'quarters', quarters)

        elif method3 == 'Top Transaction':
            col1, col2, col3= st.columns(3)

            yearlist= queries.query_table('top_transaction', 'years')
            with col1:
                years= st.slider('Select the Year_tt',yearlist.min(), yearlist.max(), yearlist.min())
            
            Transaction_amount_count('top_transaction', 'years', years)

            col1, col2, col3= st.columns(3)

            statelist= queries.query_table('top_transaction', 'states')
            with col1:
                states= st.selectbox('Select the State_tt', statelist.unique())

            top_insurance_plot('top_transaction', 'states', states)

            col1, col2, col3= st.columns(3)
           
            quarterlist= queries.query_table('top_transaction', 'quarter')
            with col1:
                quarters= st.slider('Select the Quarter_tt',quarterlist.min(), quarterlist.max(), quarterlist.min())

            Transaction_amount_count('top_transaction', 'quarters', quarters)

        elif method3 == 'Top User':
            col1, col2, col3= st.columns(3)

            yearlist= queries.query_table('top_users', 'years')
            with col1:
                years= st.slider('Select the Year_tu',yearlist.min(), yearlist.max(), yearlist.min())
            
            top_user_plot('top_users', 'years', years)

            col1, col2, col3= st.columns(3)

            statelist= queries.query_table('top_transaction', 'states')
            with col1:
                states= st.selectbox('Select the State_tu', statelist.unique())

            top_user_plot('top_users', 'states', states)

elif select == 'TOP CHARTS':
    question= st.selectbox('Select the Question', ['1. Transaction Amount and Count of Aggregated Insurance',
                                                   '2. Transaction Amount and Count of Map Insurance',
                                                   '3. Transaction Amount and Count of Top Insurance',
                                                   '4. Transaction Amount and Count of Aggregated Transaction',
                                                   '5. Transaction Amount and Count of of Map Transaction',
                                                   '6. Transaction Amount and Count of of Top Transaction',
                                                   '7. Transaction Count of Aggregated User',
                                                   '8. Registered users of Map User',
                                                   '9. App opens of Map USer',
                                                   '10. Registered users of Top User'])
    
    if question == '1. Transaction Amount and Count of Aggregated Insurance':

        st.subheader('TRANSACTION AMOUNT')
        top_chart_transaction_amount('aggregated_insurance')

        st.subheader('TRANSACTION COUNT')
        top_chart_transaction_count('aggregated_insurance')

    elif question == '2. Transaction Amount and Count of Map Insurance':

        st.subheader('TRANSACTION AMOUNT')
        top_chart_transaction_amount('map_insurance')

        st.subheader('TRANSACTION COUNT')
        top_chart_transaction_count('map_insurance')

    elif question == '3. Transaction Amount and Count of Top Insurance':

        st.subheader('TRANSACTION AMOUNT')
        top_chart_transaction_amount('top_insurance')

        st.subheader('TRANSACTION COUNT')
        top_chart_transaction_count('top_insurance')

    elif question == '4. Transaction Amount and Count of Aggregated Transaction':

        st.subheader('TRANSACTION AMOUNT')
        top_chart_transaction_amount('aggregated_transaction')

        st.subheader('TRANSACTION COUNT')
        top_chart_transaction_count('aggregated_transaction')

    elif question == '5. Transaction Amount and Count of of Map Transaction':

        st.subheader('TRANSACTION AMOUNT')
        top_chart_transaction_amount('map_transaction')

        st.subheader('TRANSACTION COUNT')
        top_chart_transaction_count('map_transaction')

    elif question == '6. Transaction Amount and Count of of Top Transaction':

        st.subheader('TRANSACTION AMOUNT')
        top_chart_transaction_amount('top_transaction')

        st.subheader('TRANSACTION COUNT')
        top_chart_transaction_count('top_transaction')

    elif question ==  '7. Transaction Count of Aggregated User':

        st.subheader('TRANSACTION COUNT')
        top_chart_transaction_count('aggregated_users')
       
    elif question ==  '8. Registered users of Map User':
        
        statelist= queries.query_table('map_users', 'states')
        states= st.selectbox('Select the State',statelist.unique())
        st.subheader('REGISTERED USERS')
        top_chart_registered_users('map_users', states)

    elif question ==  '9. App opens of Map User':
        
        statelist= queries.query_table('map_users', 'states')
        states= st.selectbox('Select the State',statelist.unique())
        st.subheader('APPOPENS')
        top_chart_appopens('map_users', states)

    elif question ==  '10. Registered users of Top User':
        
        st.subheader('REGISTERED USERS')
        top_chart_top_users('top_users')
    