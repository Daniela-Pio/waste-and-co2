import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

import streamlit as st
from streamlit.logger import get_logger

# Page title
st.set_page_config(page_title='Waste detection', page_icon='🗑️')
st.title('🗑️ Waste detection')
 
LOGGER = get_logger(__name__)


with st.expander('About this app'):
 st.markdown('What can this app do?')
 st.info('This app gives you information about the composition of the contents of the waste bins and the further processing of the waste. It also gives you information about the CO2 emissions saved by recycling.')
 st.markdown('How to use the app?')
 st.warning('Select the desired waste bin and you will receive information about the recycling process. You can also add information about the amount of waste you have properly sorted to get information about CO2 emissions saved.')


# Load data
data = pd.DataFrame({
    'Mülltonne': ['Black bin', 'Yellow bin', 'Organic bin', 'Glass container', 'Paper container'],
    'Plastic': [0, 48, 0, 0, 0],
    'Problematic substances': [1, 0, 0, 0, 0],
    'Residual waste': [32.60, 28, 0, 0, 0],
    'Recyclable material': [27.60, 10, 0, 0, 0],
    'Composite': [0, 10, 0, 0, 0],
    'Organic waste': [39.30, 27.6, 100, 0, 0],
    'Metals': [0, 14, 0, 0, 0]
})

# Input widgets
## Bin selection
waste_type = st.selectbox('Select Trash bin', data['Mülltonne'])

if waste_type not in ['Organic bin', 'Glass container', 'Paper container']:
    selected_data = data[data['Mülltonne'] == waste_type].melt(var_name='Components', value_name='Procent')

    # Filter out rows where Procent is equal to zero
    selected_data = selected_data[selected_data['Procent'] != 0]

    if not selected_data.empty:
        # Display chart
        chart = alt.Chart(selected_data).mark_bar().encode(
            x='Procent:Q',
            y='Components:N'
        ).properties(
            width=600,
            height=400
        )

        st.altair_chart(chart)


#Infotext
if waste_type == 'Black bin':
 st.write("The diagram shows the contents of the garbage can by component. The waste from the black garbage can is incinerated in a waste incineration plant - only a small proportion goes to mechanicalbiogical.")
elif waste_type == 'Yellow bin':
 st.write("The diagram shows the contents of the garbage can by component. The plastic waste from the yellow garbage can is recycled and reused. Only 31% of the plastic waste generated ends up in the recycling yard, resulting in 509 kilotons of new raw material. Composite waste produces 125 kilotons of new raw material and the reprocessing of metals produces 250 kilotons of new raw material. Everything that was sorted incorrectly is incinerated.")
elif waste_type == 'Organic bin':
 st.write("The organic waste from the brown garbage can is turned into compost in composting plants as a substitute for mineral fertilizer.")
elif waste_type == 'Glass container':
  st.write("The used glass is sorted and reused to produce new raw materials approx. 84% of the used glass is reused.")
elif waste_type == 'Paper container':
  st.write("The waste paper and cardboard is used to produce new raw materials approx. 77%.")

chart_data = pd.DataFrame({
    "Waste": ["Household waste", "Bulky waste", "Organic waste", "Biodegradable waste", "glass","Conductive packaging", "Paper, cardboard and cardboard packaging", "Aluminium ", "Copper", "Steel", "Wood", "Polyethylene PE ", "Polyethylene terephthalate PET ", "Polypropylene PP", "Mixed plastic", "Textiles", "Electrical devices", "Household appliances( washing machines and tumble dryers)", "Refrigerators and freezers", "Televisions and monitors", "Small household devices (toasters, shavers, hoovers and mobile phones)"],
    "saved CO2- kg per kg of the material": [0.6, 0.19, 0.073, 0.058, 0.175, 0.46, 0.43, 9.87, 3.42, 0.97, 0.91, 0.64, 1.2, 0.56, 0.4, 0.53, 0.97, 1.15, 0.97, 0.24, 1.37]  
})
st.bar_chart(chart_data,x="Waste",y="saved CO2- kg per kg of the material")
 
 
st.write("How much Co2 have you saved this week using this app ? Summerize how much waste you put in the correct bin and see how much your action impacted the enviorment.")
st.write("Saved CO2 in kg")
 
st.write("")
st.write("")
 
st.write("Input your amount of recycled materia here:")
col1,col2,col3,col4,col5 = st.columns(5)
Bulky_waste = col1.number_input("kg of Bulky waste", min_value=0, value=1000)
Organic_waste = col1.number_input("kg of Organic waste", min_value=0, value=100)
Biodegradable_waste = col1.number_input("kg of Biodegradable waste", min_value=0, value=100)
glass =  col2.number_input("kg of glass", min_value=0, value=100)
Textiles = col2.number_input("kg of Textiles", min_value=0, value=100)
Household_appliances= col2.number_input("kg of washing machines and tumble dryers", min_value=0, value=100)
Refrigerators_and_freezers = col3.number_input("kg of Refrigerators and freezers", min_value=0, value=100)
Televisions_and_monitors = col3.number_input("kg of Televisions and monitors devices", min_value=0, value= 100)
Small_household_devices = col3.number_input("kg of toasters, shavers, hoovers and mobile phones devices", min_value=0, value=100)
Conductive_packaging = col4.number_input("kg of tinplate, aluminium, beverage carton composites", min_value=0, value=100)
Paper_cardboard_and_cardboard_packaging = col4.number_input("kg of Paper, cardboard and cardboard packaging", min_value=0, value=100)
Polyethylene_terephthalate_PET= col4.number_input("kg of Polyethylene terephthalate PET ", min_value=0, value=100)
Residual_household_waste=col5.number_input("kg of Residual household waste ", min_value=0, value=100)
 
st.write("")
st.write("")
 
saved_CO2_from_recycled_Bulky_waste = Bulky_waste *0.19
saved_CO2_from_recycled_Organic_waste_waste = Organic_waste *0.073
saved_CO2_from_recycled_Biodegradable_waste = Biodegradable_waste *0.058
saved_CO2_from_recycled_glass = glass *0.175
saved_CO2_from_recycled_Textiles = Textiles *0.53
saved_CO2_from_recycled_Household_appliances = Household_appliances *1.15
saved_CO2_from_recycled_Refrigerators_and_freezers = Refrigerators_and_freezers *0.97
saved_CO2_from_recycled_Televisions_and_monitors = Televisions_and_monitors *0.24
saved_CO2_from_recycled_Small_household_devices = Small_household_devices *1.37
saved_CO2_from_recycled_Conductive_packaging = Conductive_packaging *0.46
saved_CO2_from_recycled_Paper_cardboard_and_cardboard_packaging = Paper_cardboard_and_cardboard_packaging*0.43
saved_CO2_from_recycled_Polyethylene_terephthalate_PET = Polyethylene_terephthalate_PET*1.2
saved_CO2_from_recycled_Residual_household_waste= Residual_household_waste *0.6
 
st.write("")
st.write("")


 
col1.metric(label= " Bulky waste", value=f"{saved_CO2_from_recycled_Bulky_waste:,.2f} kg")
col1.metric(label= "Organic waste", value=f"{saved_CO2_from_recycled_Organic_waste_waste:,.2f} kg")
col1.metric(label= " Biodegradable waste", value=f"{saved_CO2_from_recycled_Biodegradable_waste:,.2f} kg")
col2.metric(label= "glass", value=f"{saved_CO2_from_recycled_glass:,.2f} kg")
col2.metric(label= " Textiles", value=f"{saved_CO2_from_recycled_Textiles:,.2f} kg")
col2.metric(label= " Household appliances", value=f"{saved_CO2_from_recycled_Household_appliances:,.2f} kg")
col3.metric(label= " Refrigerators and freezers", value=f"{saved_CO2_from_recycled_Refrigerators_and_freezers:,.2f} kg")
col3.metric(label= "Televisions and monitors", value=f"{saved_CO2_from_recycled_Televisions_and_monitors:,.2f} kg")
col3.metric(label= " small household devices", value=f"{saved_CO2_from_recycled_Small_household_devices:,.2f} kg")
col4.metric(label= " Conductive packaging", value=f"{saved_CO2_from_recycled_Conductive_packaging:,.2f} kg")
col4.metric(label= " Paper cardboard and cardboard packaging", value=f"{saved_CO2_from_recycled_Paper_cardboard_and_cardboard_packaging:,.2f} kg")
col4.metric(label= " Polyethylene terephthalate PET", value=f"{saved_CO2_from_recycled_Polyethylene_terephthalate_PET:,.2f} kg")
col5.metric(label= "Residual household waste ", value=f"{saved_CO2_from_recycled_Residual_household_waste:,.2f} kg")
 
st.write("")
st.write("")
 
st.write("Saved CO2 catregorized ")
 
CO2_brown_bin = saved_CO2_from_recycled_Organic_waste_waste + saved_CO2_from_recycled_Biodegradable_waste
CO2_glass_recycling_bin = saved_CO2_from_recycled_glass = glass
CO2_textile_recycling_centre = saved_CO2_from_recycled_Textiles
CO2_recycling_centre = saved_CO2_from_recycled_Household_appliances + saved_CO2_from_recycled_Refrigerators_and_freezers + saved_CO2_from_recycled_Televisions_and_monitors + saved_CO2_from_recycled_Small_household_devices + saved_CO2_from_recycled_Bulky_waste
CO2_yellow_bin= saved_CO2_from_recycled_Conductive_packaging
CO2_blue_bin = saved_CO2_from_recycled_Paper_cardboard_and_cardboard_packaging
CO2_supermarket = saved_CO2_from_recycled_Polyethylene_terephthalate_PET
CO2_black_bin = saved_CO2_from_recycled_Residual_household_waste
 
chart_data = pd.DataFrame({
    "recycling location": ["brown bin", "glass recycling bin", "textile recycling centre", "recycling centre", "yellow bin", "blue bin", "supermarket", "black bin"],
     "saved CO2": ["CO2_brown_bin", "CO2_glass_recycling_bin", "CO2_textile_recycling_centre", "CO2_recycling_centre", "CO2_yellow_bin", "CO2_blue_bin","CO2_supermarket", "CO2_black_bin"]                
 })
st.bar_chart(chart_data, x="recycling location", y="saved CO2")
