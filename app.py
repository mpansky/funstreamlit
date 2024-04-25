import streamlit as st
import pandas as pd

# Sample Data (Ideally, this would come from a CSV file or a database)
data = {
    'Make and Model': ['Toyota Camry', 'Honda Accord', 'Ford Mustang', 'Tesla Model 3', 'Chevrolet Malibu'],
    'Year': [2022, 2022, 2023, 2023, 2022],
    'Engine Type': ['Hybrid', 'Petrol', 'Petrol', 'Electric', 'Hybrid'],
    'Price': [30000, 28000, 35000, 45000, 25000],
    'Color': ['Red', 'Blue', 'Black', 'White', 'Silver'],
    'Mileage': [0, 0, 0, 0, 0]
}
car_data = pd.DataFrame(data)

# Create the Streamlit interface
st.title('Car Finder App')
st.sidebar.header('Filter Options')

# Creating filters
make_and_model = st.sidebar.multiselect('Make and Model', options=car_data['Make and Model'].unique())
year = st.sidebar.multiselect('Year', options=car_data['Year'].unique())
engine_type = st.sidebar.multiselect('Engine Type', options=car_data['Engine Type'].unique())
price = st.sidebar.slider('Price', min_value=int(car_data['Price'].min()), max_value=int(car_data['Price'].max()), value=(int(car_data['Price'].min()), int(car_data['Price'].max())))
color = st.sidebar.multiselect('Color', options=car_data['Color'].unique())

# Filtering the data based on selections
filtered_data = car_data[
    (car_data['Make and Model'].isin(make_and_model) if make_and_model else True) &
    (car_data['Year'].isin(year) if year else True) &
    (car_data['Engine Type'].isin(engine_type) if engine_type else True) &
    (car_data['Price'] >= price[0]) & (car_data['Price'] <= price[1]) &
    (car_data['Color'].isin(color) if color else True)
]

# Display filtered data
st.dataframe(filtered_data)
