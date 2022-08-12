# Real Estate Database

### Project description
The project is a database system for a large franchised real estate company. The company has many offices located all over the country. 
- Each office is responsible for selling houses in a particular area.
- An agent can be associated with one or more offices.
- The estate agent received a commission based on the sale price of the house they sell.
- There are house listings on the web, and when the sale happens, at least buyer details, sale price, date of sale, and the selling estate agent needs to be captured. 
- The original listing of the house contains all the information of the house, agent, office and status of the house (sold or not_sold).

### The files
- create.py: Creates tables and database relations
- insert.py: Inserting the manual data I have generated
- query_data.py: Runs the queries
- requirement.txt: The file has all the libraries with its versions that is necessary to run the project.

### The tables
- Agents: The estate agents' contact details
- Sellers: The house sellers' contact details
- Buyers: The house buyer's contact details
- Offices: The real estate company offices' name
- OfficesZipcode: The company offices' zipcodes. One office can have many zipcodes. 
- AgentsOffices: One agent can have many offices. The offices associated with the agent. 
- Listings: The listings of the houses with the house details, buyers, sellers, and agents
- Sales: When the house is sold, the Sales tables captures information about the details plus the saleprice, salelocation, and agent commission. 

### Running the project
- Commands for MacOS:
python3.6 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 create.py
python3 insert.py
python3 query_data.py

- Commands for Windows
python3.6 -m venv venv
venv\Scripts\activate.bat
pip3 install -r requirements.txt
python3 create.py
python3 insert.py
python3 query_data.py