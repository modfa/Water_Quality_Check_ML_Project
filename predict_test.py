# Making requests
import requests

url = 'http://localhost:9696/predict'

#Water sample to test 
water_sample = {
    "ph": 9.454119,
    "hardness": 224.817132,
    "solids": 21379.963927,
    "chloramines": 5.407692,
    "sulfate": 227.665635,
    "conductivity": 431.613001,
    "organic_carbon": 15.772334,
    "trihalomethanes": 52.033845,
    "turbidity": 4.058626,  
}


response = requests.post(url, json=water_sample).json()
print(response)