import requests
import json

# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = "http://47c8d7fa-9e0b-47eb-86f6-c347c59a61ae.westus.azurecontainer.io/score"

# If the service is authenticated, set the key or token
key = "e3U7IX9NYQNm4BlbaNVRhcwIv6UxpEQV"

# Two sets of data to score, so we get two results back
data = {"data": [{
"customerID": "7590-VHVEG",
 "gender": "Female",
  "SeniorCitizen": 0,
   "Partner": "No",
    "Dependents": "No", 
    "tenure": 45, 
    "PhoneService": "No", 
    "MultipleLines": "No phone service", 
    "InternetService": "DSL", 
    "OnlineSecurity": "Yes", 
    "OnlineBackup": "No", 
    "DeviceProtection": "Yes", 
    "TechSupport": "Yes",
    "StreamingTV": "No",
    "StreamingMovies": "No", 
    "Contract": "One year",
    "PaperlessBilling": "No",
    "PaymentMethod": "Bank transfer (automatic)", 
    "MonthlyCharges": 42.3, 
    "TotalCharges": 1840.75
    },
    {
"customerID": "7591-VHVEG",
 "gender": "Male",
  "SeniorCitizen": 1,
   "Partner": "Yes",
    "Dependents": "Yes", 
    "tenure": 20, 
    "PhoneService": "Yes", 
    "MultipleLines": "Yes", 
    "InternetService": "DSL", 
    "OnlineSecurity": "Yes", 
    "OnlineBackup": "Yes", 
    "DeviceProtection": "Yes", 
    "TechSupport": "Yes",
    "StreamingTV": "No",
    "StreamingMovies": "No", 
    "Contract": "One year",
    "PaperlessBilling": "No",
    "PaymentMethod": "Bank transfer (automatic)", 
    "MonthlyCharges": 20.3, 
    "TotalCharges": 1000.75
    }]}
# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {"Content-Type": "application/json"}
# If authentication is enabled, set the authorization header
headers["Authorization"] = f"Bearer {key}"

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())

