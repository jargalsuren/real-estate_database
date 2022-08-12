from decimal import Inexact
from sqlalchemy import create_engine, Column, Text, Integer, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime, Numeric, String

Base = declarative_base()

#Agents
class Agents(Base):
    __tablename__ = 'agents'
    id = Column(Integer, primary_key=True)
    firstname = Column(Text)
    lastname = Column(Text)
    email = Column(Text)
    phone = Column(Text)

    def __repr__(self):
        return 'agents(id={}, firstname={}, lastname={}, email={}, phone={})\n'.format(self.id, self.firstname, self.lastname, self.email, self.phone)

#Sellers
class Sellers(Base):
    __tablename__ = 'sellers'
    id = Column(Integer, primary_key=True)
    firstname = Column(Text)
    lastname = Column(Text)
    email = Column(Text)
    phone = Column(Text)

    def __repr__(self):
        return 'sellers(id={}, firstname={}, lastname={}, email={}, phone={})\n'.format(self.id, self.firstname, self.lastname, self.email, self.phone)

#Buyers
class Buyers(Base):
    __tablename__ = 'buyers'
    id = Column(Integer, primary_key=True)
    firstname = Column(Text)
    lastname = Column(Text)
    email = Column(Text)
    phone = Column(Text)

    def __repr__(self):
        return 'buyers(id={}, firstname={}, lastname={}, email={}, phone={})\n'.format(self.id, self.firstname, self.lastname, self.email, self.phone)
    
#Offices
class Offices(Base):
    __tablename__ = 'offices'
    id = Column(Integer, primary_key=True)
    name = Column(Text)

    def __repr__(self):
        return 'offices(id={}, name={})\n'.format(self.id, self.name)
    
#One area (zipcode) has one office, and one office can have multiple areas (zipcodes)
class OfficesZipcode(Base):
    __tablename__ = 'officeszipcode'
    zipcode = Column(Integer, primary_key=True)
    officeid = Column(Integer, ForeignKey('offices.id'))
    offices = relationship(Offices)

    def __repr__(self):
        return 'OfficesZipcode(zipcode={}, officeid={})\n'.format(self.zipcode, self.officeid)
    
#One agent can be associated with one or more offices
class AgentsOffices(Base):
    __tablename__ = 'agentsoffices'
    agentid = Column(Integer, ForeignKey('agents.id'), primary_key=True)
    officeid = Column(Integer, ForeignKey('offices.id'), primary_key=True)
    offices = relationship(Offices)
    agents = relationship(Agents)

    def __repr__(self):
        return 'AgentsOffices(agentid={}, officeid={})\n'.format(self.agentid, self.officeid)

#The house listings
class Listings(Base):
    __tablename__ = 'listings'
    id = Column(Integer, primary_key=True)
    zipcode = Column(Integer, ForeignKey('officeszipcode.zipcode'))
    bedrooms = Column(Integer) #number of bedrooms
    bathrooms = Column(Integer) #number of bathrooms
    listingdate = Column(DateTime)
    listingmonth = Column(Integer)
    listingprice = Column(Integer)
    sellerid = Column(Integer, ForeignKey('sellers.id'))
    agentid = Column(Integer, ForeignKey('agents.id'))
    status = Column(String, default='not_sold')
    officeszipcode = relationship(OfficesZipcode)
    sellers = relationship(Sellers)
    agents = relationship(Agents)

    def __repr__(self):
        return '''Listings(id={}, zipcode={}, bedrooms={}, bathrooms={}, listingdate={}, 
        listingmonth={}, listingprice={}, sellerid={}, agentid={}, status={})\n'''.format(self.id, self.zipcode,self.bedrooms, self.bathrooms, self.listingdate, self.listingmonth, self.listingprice, self.sellerid, self.agentid, self.status)

#Sale details
class Sales(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True)
    listingid = Column(Integer, ForeignKey('listings.id'))
    saledate = Column(DateTime)
    salemonth = Column(Integer)
    saleprice = Column(Integer)
    buyerid = Column(Integer, ForeignKey('buyers.id'))
    commission = Column(Integer)
    listings = relationship(Listings)
    buyers = relationship(Buyers)
    

    def __repr__(self):
        return '''sales(id={}, listingid={}, saledate={}, salemonth={}, saleprice={}, 
        buyerid={}, commission={})\n'''.format(self.id, self.listingid, self.saledate, self.salemonth,self.saleprice, self.buyerid, self.commission)


def init_db(url='sqlite:///database.db'):
    engine = create_engine(url)
    engine.connect()
    Base.metadata.create_all(bind=engine)
    return engine


if __name__ == '__main__':
    engine = init_db()
