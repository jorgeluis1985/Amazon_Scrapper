import requests
import json
import csv
import pandas as pd
import matplotlib.pyplot as plt



# set up the request parameters
params = {
'api_key': '4B5C506FF9D84D679CC5334794EEEBEA',
  'type': 'category',
  'url': 'https://www.amazon.com/s?bbn=16225007011&rh=n%3A16225007011%2Cn%3A13896617011&dc&rnid=16225007011&ref=lp_16225007011_nr_n_2'
}

# make the http GET request to Rainforest API
api_result = requests.get('https://api.rainforestapi.com/request', params)

# print the JSON response from Rainforest API
#print(json.dumps(api_result.json()))

response_data = json.loads(api_result.content)
#print(response_data)


# Creating a dictionary to use when creating the csv file
data = []

for item in response_data['category_results']:
    title = item['title']
    price = item['prices'][0]['value']
    if 'rating' in item:
        rating = item['rating']
    else:
        rating = None
    data.append([title, price, rating])


#Creating the csv file
df = pd.DataFrame(data,columns=['Title', 'Price','Rating'])
df['Price'] = df['Price'].astype(float)

df.to_csv('response.csv', index=False)

df = pd.read_csv('response.csv')


#Constructing a hsitogram for prices
df['Price'].hist()  #HISTOGRAM FOR PRICES
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.title('Price Distribution')
plt.show()

#Constructing a scatter plot for the price and ratings
plt.scatter(df['Price'], df['Rating'])
plt.xlabel('Price')
plt.ylabel('Rating')
plt.title('Price vs Rating')
plt.show()


print(df.info())
print(df.describe())
print(df.tail())
print(df.tail(10))
print(df.tail())

#print('CSV data saved to response.csv')

