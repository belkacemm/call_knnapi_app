import streamlit as st
import requests

st.title("Calling knnapi fastapi")
st.header("Get the input data from the user")
neighbors = st.number_input("Enter a number of neighbors", min_value=1, max_value=50)
p = st.number_input("Enter 1 for Manhattan, 2 for Euclidean and any other number for Minkowski", min_value=1, max_value=50)
BASE_URL = "https://knnapi-1-w3784165.deta.app/knn/create?"
url = BASE_URL + "neighbors=" + str(neighbors) + "&p=" + str(p)
response = requests.get(url).json()
st.write(response)