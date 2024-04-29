from typing import List
from typing import Optional
from sqlalchemy import Column, Float, String, Integer, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base 
from base_model import Base

class CSCIDS2017_balanced_attk(Base):
    """CSCIDS2017_balanced_attack model"""
    __tablename__ = "CSCIDS2017_balanced_attk"
    
    FLOW_ID = Column(Float)
    SOURCE_IP = Column(Float)
    SOURCE_PORT = Column(Float)
    DESTINATION_IP = Column(Float)
    DESTINATION_PORT = Column(Float)
    PROTOCOL = Column(Float)
    TIMESTAMP = Column(Float)
    FLOW_DURATION = Column(Float)
    TOTAL_FWD_PACKETS = Column(Float)
    TOTAL_BACKWARD_PACKETS = Column(Float)
    TOTAL_LENGTH_OF_FWD_PACKETS = Column(Float)
    TOTAL_LENGTH_OF_BWD_PACKETS = Column(Float)
    FWD_PACKET_LENGTH_MAX = Column(Float)
    FWD_PACKET_LENGTH_MIN = Column(Float)
    FWD_PACKET_LENGTH_MEAN = Column(Float)
    FWD_PACKET_LENGTH_STD = Column(Float)
    BWD_PACKET_LENGTH_MAX = Column(Float)
    BWD_PACKET_LENGTH_MIN = Column(Float)
    BWD_PACKET_LENGTH_MEAN = Column(Float)
    BWD_PACKET_LENGTH_STD = Column(Float)
    FLOW_BYTES_S = Column(Float)
    FLOW_PACKETS_S = Column(Float)
    FLOW_IAT_MEAN = Column(Float)
    FLOW_IAT_STD = Column(Float)
    FLOW_IAT_MAX = Column(Float)
    FLOW_IAT_MIN = Column(Float)
    FWD_IAT_TOTAL = Column(Float)
    FWD_IAT_MEAN = Column(Float)
    FWD_IAT_STD = Column(Float)
    FWD_IAT_MAX = Column(Float)
    FWD_IAT_MIN = Column(Float)
    BWD_IAT_TOTAL = Column(Float)
    BWD_IAT_MEAN = Column(Float)
    BWD_IAT_STD = Column(Float)
    BWD_IAT_MAX = Column(Float)
    BWD_IAT_MIN = Column(Float)
    FWD_PSH_FLAGS = Column(Float)
    BWD_PSH_FLAGS = Column(Float)
    FWD_URG_FLAGS = Column(Float)
    BWD_URG_FLAGS = Column(Float)
    FWD_HEADER_LENGTH = Column(Float)
    BWD_HEADER_LENGTH = Column(Float)
    FWD_PACKETS_S = Column(Float)
    BWD_PACKETS_S = Column(Float)
    MIN_PACKET_LENGTH = Column(Float)
    MAX_PACKET_LENGTH = Column(Float)
    PACKET_LENGTH_MEAN = Column(Float)
    PACKET_LENGTH_STD = Column(Float)
    PACKET_LENGTH_VARIANCE = Column(Float)
    FIN_FLAG_COUNT = Column(Float)
    SYN_FLAG_COUNT = Column(Float)
    RST_FLAG_COUNT = Column(Float)
    PSH_FLAG_COUNT = Column(Float)
    ACK_FLAG_COUNT = Column(Float)
    URG_FLAG_COUNT = Column(Float)
    CWE_FLAG_COUNT = Column(Float)
    ECE_FLAG_COUNT = Column(Float)
    DOWN_UP_RATIO = Column(Float)
    AVERAGE_PACKET_SIZE = Column(Float)
    AVG_FWD_SEGMENT_SIZE = Column(Float)
    AVG_BWD_SEGMENT_SIZE = Column(Float)
    FWD_AVG_BYTES_BULK = Column(Float)
    FWD_AVG_PACKETS_BULK = Column(Float)
    FWD_AVG_BULK_RATE = Column(Float)
    BWD_AVG_BYTES_BULK = Column(Float)
    BWD_AVG_PACKETS_BULK = Column(Float)
    BWD_AVG_BULK_RATE = Column(Float)
    SUBFLOW_FWD_PACKETS = Column(Float)
    SUBFLOW_FWD_BYTES = Column(Float)
    SUBFLOW_BWD_PACKETS = Column(Float)
    SUBFLOW_BWD_BYTES = Column(Float)
    INIT_WIN_BYTES_FORWARD = Column(Float)
    INIT_WIN_BYTES_BACKWARD = Column(Float)
    ACT_DATA_PKT_FWD = Column(Float)
    MIN_SEG_SIZE_FORWARD = Column(Float)
    ACTIVE_MEAN = Column(Float)
    ACTIVE_STD = Column(Float)
    ACTIVE_MAX = Column(Float)
    ACTIVE_MIN = Column(Float)
    IDLE_MEAN = Column(Float)
    IDLE_STD = Column(Float)
    IDLE_MAX = Column(Float)
    IDLE_MIN = Column(Float)
    LABE = Column(Float)


class CSCIDS2017_fri_pm(Base):
    __tablename__ = "CSCIDS2017_fri_pm"
    
    
    
class CSCIDS2017_fri_pm(Base):
    __tablename__ = "CSCIDS2017_fri_pm"
class CSCIDS2017_fri_pm(Base):
    __tablename__ = "CSCIDS2017_fri_pm"       
class CSCIDS2017_fri_pm(Base):
    __tablename__ = "CSCIDS2017_fri_pm"
class CSCIDS2017_fri_pm(Base):
    __tablename__ = "CSCIDS2017_fri_pm"
class CSCIDS2017_fri_pm(Base):
    __tablename__ = "CSCIDS2017_fri_pm"
class CSCIDS2017_fri_pm(Base):
    __tablename__ = "CSCIDS2017_fri_pm"
class CSCIDS2017_fri_pm(Base):
    __tablename__ = "CSCIDS2017_fri_pm"    