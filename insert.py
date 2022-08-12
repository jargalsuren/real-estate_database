from create import Agents, Sellers, Buyers, Offices, OfficesZipcode, AgentsOffices, Listings, Sales
from create import init_db
from sqlalchemy.orm import sessionmaker
from datetime import datetime

engine = init_db()
Session = sessionmaker(bind=engine)
session = Session()


def addAgent(id, firstname, lastname, email, phone):
    if session.query(Agents).filter(Agents.id == id).count() == 0:
        session.add(Agents(id=id, firstname=firstname,
                    lastname=lastname, email=email, phone=phone))
        session.commit()


def addSeller(id, firstname, lastname, email, phone):
    if session.query(Sellers).filter(Sellers.id == id).count() == 0:
        session.add(Sellers(id=id, firstname=firstname,
                    lastname=lastname, email=email, phone=phone))
        session.commit()

def addBuyer(id, firstname, lastname, email, phone):
    if session.query(Buyers).filter(Buyers.id == id).count() == 0:
        session.add(Buyers(id=id, firstname=firstname,
                    lastname=lastname, email=email, phone=phone))
        session.commit()
        
def addOffice(id, name):
    if session.query(Offices).filter(Offices.id == id).count() == 0:
        session.add(Offices(id=id, name=name))
        session.commit()

def addOfficesZipcode(zipcode, officeid):
    if session.query(OfficesZipcode).filter(OfficesZipcode.zipcode == zipcode).count() == 0:
        session.add(OfficesZipcode(zipcode=zipcode, officeid=officeid))
        session.commit()

def addListing(id, zipcode, bedrooms, bathrooms, listingdate, listingmonth, listingprice, sellerid, agentid, status='not_sold'):
    if session.query(Listings).filter(Listings.id == id).count() == 0:
        session.add(Listings(id=id, zipcode=zipcode, bedrooms=bedrooms, bathrooms=bathrooms, listingdate=listingdate, listingmonth=listingmonth,
                             listingprice=listingprice, sellerid=sellerid, agentid=agentid, status=status))
        officeid = session.query(OfficesZipcode.officeid).filter(
            OfficesZipcode.zipcode == zipcode).first()[0]
        agents_offices = session.query(AgentsOffices.agentid).filter(
            AgentsOffices.officeid == officeid, AgentsOffices.agentid == agentid).all()
        if agents_offices == []:
            session.add(AgentsOffices(agentid=agentid, officeid=officeid))
        session.commit()


def addSales(id, listingid, saledate, salemonth, saleprice, buyerid):
        
    if saleprice < 100000:
        commission = saleprice * 0.1
    elif saleprice >= 1000000:
        commission = saleprice * 0.075
    elif saleprice >= 200000:
        commission = saleprice * 0.06
    elif saleprice >= 500000:
        commission = saleprice * 0.05
    elif saleprice > 1000000:
        commission = saleprice * 0.04
        
    if session.query(Sales).filter(Sales.id == id).count() == 0:
        session.add(Sales(id=id, listingid=listingid, saledate=saledate,
                salemonth=salemonth, saleprice=saleprice, buyerid=buyerid, commission=commission))
    session.query(Listings).filter(
        Listings.id == listingid).update({'status': 'sold'})
    
    agentid = session.query(Listings.agentid).filter(
        Listings.id == listingid).first()[0]
    session.query(Sales).filter(
        Sales.id == id).update({'commission': commission})
    session.commit()


# Adding agents
addAgent(1, 'Jasu', 'Mandakh', 'jasu@yahoo.com', '5104586315')
addAgent(2, 'Trang', 'Tran', 'trang@yahoo.com', '6388287382')
addAgent(3, 'Tuan', 'Nguyen', 'tuan@yahoo.com', '337395934')
addAgent(4, 'Aiko', 'Shimizu', 'aiko@yahoo.com', '202928383')
addAgent(5, 'Eugene', 'Chan', 'eugene@yahoo.com', '383839333')
addAgent(6, 'Sterne', 'Phillip', 'sterne@gmail.com', '4152627378')

# Adding sellers
addSeller(1, 'Robert', 'Williams', 'robbie98@gmail.com', '6647483832')
addSeller(2, 'Lil', 'Nas X', 'lilnasx@gmail.com', '2938738837')
addSeller(7, 'Favour', 'Okeke', 'favourokeke@gmail.com', '6363552679')
addSeller(5, 'Lyon', 'Nishizawa', 'lyon_love@gmail.com', '938372782')
addSeller(4, 'Aarthi', 'Varshini', 'aarthi_varshini@gmail.com', '8272736332')
addSeller(3, 'Albin', 'Siriniqi', 'albin@yahoo.com', '028277633')
addSeller(6, 'Sona', 'Vardanyan', 'sona_var@hotmail.com', '62362627782')
addSeller(8, 'Rhythm', 'Beat', 'rhythm@uni.minerva.edu', '848489493')

# Adding buyers
addBuyer(1, 'Norika', 'Narimatsu', 'norichan@gmail.com', '99008892')
addBuyer(2, 'Precious', 'Ukaegbu', 'precious@nice.com', '6467828272')
addBuyer(3, 'Unurzaya', 'Bataa', 'unuruu99@gmail.com', '63518280398')
addBuyer(4, 'Tuya', 'Sonsoo', 'tuya2323233@gmail.com', '645372920')
addBuyer(5, 'Kylie', 'Jenner', 'kylie@kylieskin.com', '9900990099')
addBuyer(6, 'Kim', 'Kardashian', 'kim@kardashian.com', '5526635527')
addBuyer(7, 'Kris', 'Jenner', 'kris@jenner.com', '827378839')

# Adding offices
addOffice(1, 'San Francisco')
addOffice(2, 'Los Angeles')
addOffice(3, 'New York')
addOffice(4, 'Seattle')
addOffice(5, 'San Diego')
addOffice(6, 'Washington DC')
addOffice(7, 'Chicago')

# Adding Office zip codes. For one office there can multiple zip codes. 
addOfficesZipcode(94102, 1)
addOfficesZipcode(94103, 1)
addOfficesZipcode(90001, 2)
addOfficesZipcode(90023, 2)
addOfficesZipcode(90003, 2)
addOfficesZipcode(10001, 3)
addOfficesZipcode(10027 ,3)
addOfficesZipcode(98101, 4)
addOfficesZipcode(98111, 4)
addOfficesZipcode(91942, 5)
addOfficesZipcode(92071 ,5)
addOfficesZipcode(20006, 6)
addOfficesZipcode(20049, 6)
addOfficesZipcode(10008, 7)
addOfficesZipcode(60602, 7)
addOfficesZipcode(60603, 7)


# Agent offices table should be updated
print('''\n
AgentsOffices Table
-------------------''')
print(session.query(AgentsOffices).all())

# Adding Listings of houses
addListing(1, 92071, 2, 1, datetime(2022, 3, 24), 202203, 200000, 8, 1)
addListing(2, 20006, 4, 2, datetime(2022, 4, 1), 202204, 750000, 8, 2)
addListing(3, 98101, 3, 2, datetime(
    2019, 9, 1), 201909, 500000, 3, 3)
addListing(4, 90001, 1, 1, datetime(2020, 5, 7), 202005, 265000, 4, 4)
addListing(5, 94102, 2, 1, datetime(
    2022, 9, 12), 202209, 600000, 1, 5)
addListing(6, 94102, 1, 1, datetime(2022, 5, 8), 202205, 90000, 2, 6)
addListing(7, 90003, 5, 5, datetime(
    2022, 2, 8), 202202, 1550000, 6, 1)
addListing(8, 60602, 6, 5, datetime(
    2021, 12, 31), 202112, 2400000, 5, 2)
addListing(9, 10008, 7, 7, datetime(2022, 1, 1), 202201, 11540000, 7, 3)

# Adding Sales of houses
addSales(1, 1, datetime(2022, 4, 1), 202204, 190000, 1)
addSales(2, 2, datetime(2022, 5, 23), 202205, 780000, 3)
addSales(3, 3, datetime(2020, 1, 2), 202001, 450000,2)
addSales(4, 4, datetime(2020, 7, 31), 202007, 200000, 5)
addSales(5, 9, datetime(2022, 3, 23), 202203, 12000000, 7)
addSales(6, 8, datetime(2022, 1, 31), 202201, 2300000, 7)
addSales(7, 7, datetime(2022, 3, 4), 202203, 1600000, 6)
addSales(8, 5, datetime(2022, 10, 28), 202210, 620000, 4)

# need to check if the Listings table has been updated
print('''\n
    Listings Table
    -------------------''')
print(session.query(Listings).all())

# need to check if the Agents table has been updated
print('''\n
    Sales Table
    -------------------''')
print(session.query(Sales).all())
