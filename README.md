# Package-Delivery-System

**About the Project:
**
Our project aims to enable drivers to earn extra money by utilizing the empty boot space they have in their vehicles to deliver parcels from customers. This involves a heavy spatial element where we as a host contain all the customer details and truck details, compute the most feasible customer for each trucker, and the revenue he can gain using an altered Travelling Salesman algorithm which runs on top of our original revenue calculation and genetic algorithm.

**Dependencies required to run the project:
**
1. Install the local version of MongoDB Compass to populate the database with the CSV containing the car boot space data and truck freight size.
2. Add CSV files to the database titled car_data and container for the car and truck respectively after running the Data preprocessing Jupyter Notebook implemented using Python 3.
3. Install Python 3 and Node JS.
4. Install Node JS dependencies such as express, ts, mongodb, etc.
5. Set Environment Variables for MongoDB bin path to start mongod server in CMD or terminal.
6. Get API Key for Google Maps API using the link:
https://console.cloud.google.com/projectselector2/google/maps-apis/credentials?pli=1

**Requirements to run UI:
**
1. Install the required python packages as mentioned in “app.py”
2. To display the User Interface, run the command “python app.py” and paste the localhost URL in a browser
to view the front end and Google Maps.
3. Add your own API Key to the Javascript file to display the map on the front end.
4. Enter details on the HTML form to check the working, retrieve the optimized route and show the profits
generated in US Dollars.
5. Ensure the connection is established between the front-end and the back-end connection with the local
version of MongoDB Compass installed on your system to receive alerts.
