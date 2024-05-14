from sqlalchemy import Column, Integer, String, DateTime
from database import Base


class AgentName(Base):
    __tablename__ = "agentname"

    name_id = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String(255), nullable=False)
    lastname = Column(String(255), nullable=False)
    email = Column(String(255))
    phone = Column(String(13), nullable=False)
    pollingunit_uniqueid = Column(Integer, nullable=False)


class AnnouncedLGAResults(Base):
    __tablename__ = "announced_lga_results"

    result_id = Column(Integer, primary_key=True, autoincrement=True)
    lga_name = Column(String(50), nullable=False)
    party_abbreviation = Column(String(4), nullable=False)
    party_score = Column(Integer, nullable=False)
    entered_by_user = Column(String(50), nullable=False)
    date_entered = Column(DateTime, nullable=False)
    user_ip_address = Column(String(50), nullable=False)


class AnnouncedPUResults(Base):
    __tablename__ = "announced_pu_results"

    result_id = Column(Integer, primary_key=True, autoincrement=True)
    polling_unit_uniqueid = Column(String(50), nullable=False)
    party_abbreviation = Column(String(4), nullable=False)
    party_score = Column(Integer, nullable=False)
    entered_by_user = Column(String(50), nullable=False)
    date_entered = Column(DateTime, nullable=False)
    user_ip_address = Column(String(50), nullable=False)


class AnnouncedStateResults(Base):
    __tablename__ = "announced_state_results"

    result_id = Column(Integer, primary_key=True, autoincrement=True)
    state_name = Column(String(50), nullable=False)
    party_abbreviation = Column(String(4), nullable=False)
    party_score = Column(Integer, nullable=False)
    entered_by_user = Column(String(50), nullable=False)
    date_entered = Column(DateTime, nullable=False)
    user_ip_address = Column(String(50), nullable=False)


class AnnouncedWardResults(Base):
    __tablename__ = "announced_ward_results"

    result_id = Column(Integer, primary_key=True, autoincrement=True)
    ward_name = Column(String(50), nullable=False)
    party_abbreviation = Column(String(4), nullable=False)
    party_score = Column(Integer, nullable=False)
    entered_by_user = Column(String(50), nullable=False)
    date_entered = Column(DateTime, nullable=False)
    user_ip_address = Column(String(50), nullable=False)


class LGA(Base):
    __tablename__ = "lga"

    uniqueid = Column(Integer, primary_key=True, autoincrement=True)
    lga_id = Column(Integer, nullable=False)
    lga_name = Column(String(50), nullable=False)
    state_id = Column(Integer, nullable=False)
    lga_description = Column(String, nullable=True)
    entered_by_user = Column(String(50), nullable=False)
    date_entered = Column(DateTime, nullable=False)
    user_ip_address = Column(String(50), nullable=False)


class Party(Base):
    __tablename__ = "party"

    id = Column(Integer, primary_key=True, autoincrement=True)
    partyid = Column(String(11), nullable=False)
    partyname = Column(String(11), nullable=False)


class PollingUnit(Base):
    __tablename__ = "polling_unit"

    uniqueid = Column(Integer, primary_key=True, autoincrement=True)
    polling_unit_id = Column(Integer, nullable=False)
    ward_id = Column(Integer, nullable=False)
    lga_id = Column(Integer, nullable=False)
    uniquewardid = Column(Integer)
    polling_unit_number = Column(String(50))
    polling_unit_name = Column(String(50))
    polling_unit_description = Column(String)
    lat = Column(String(255))
    long = Column(String(255))
    entered_by_user = Column(String(50))
    date_entered = Column(DateTime)
    user_ip_address = Column(String(50))


class State(Base):
    __tablename__ = "states"

    state_id = Column(Integer, primary_key=True)
    state_name = Column(String(50), nullable=False)


class Ward(Base):
    __tablename__ = "ward"

    uniqueid = Column(Integer, primary_key=True, autoincrement=True)
    ward_id = Column(Integer, nullable=False)
    ward_name = Column(String(50), nullable=False)
    lga_id = Column(Integer, nullable=False)
    ward_description = Column(String)
    entered_by_user = Column(String(50), nullable=False)
    date_entered = Column(DateTime, nullable=False)
    user_ip_address = Column(String(50), nullable=False)
