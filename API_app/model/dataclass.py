import uuid
from pydantic import BaseModel, Field

""" DB model connect sqlalchemy """

class Base_model(BaseModel):
    """Base_model"""
    pk: uuid.UUID
    name: str
    
    class Config:
        from_attributes : True


""" model Input Data specify """

class DataInput(BaseModel):
    NM : str = Field(min_length=4, max_length=10)
    x : list[float] = Field()

class PredictOutput(BaseModel):
    prediction : int

""" 
data name : CSCIDS2017
target file count : 8 -> table 8
columns count  : 79 * 8  : 632
total row count : ??    

sample :> balance data file : 1

"""
class CSCIDS_balanced(BaseModel):
    """CSCIDS_balanced"""
    Index : int      
    FLOW_ID : float
    SOURCE_IP : float
    SOURCE_PORT : float
    DESTINATION_IP : float
    DESTINATION_PORT : float
    PROTOCOL : float
    TIMESTAMP : float
    FLOW_DURATION : float
    TOTAL_FWD_PACKETS : float
    TOTAL_BACKWARD_PACKETS : float
    TOTAL_LENGTH_OF_FWD_PACKETS : float
    TOTAL_LENGTH_OF_BWD_PACKETS : float
    FWD_PACKET_LENGTH_MAX : float
    FWD_PACKET_LENGTH_MIN : float
    FWD_PACKET_LENGTH_MEAN : float
    FWD_PACKET_LENGTH_STD : float
    BWD_PACKET_LENGTH_MAX : float
    BWD_PACKET_LENGTH_MIN : float
    BWD_PACKET_LENGTH_MEAN : float
    BWD_PACKET_LENGTH_STD : float
    FLOW_BYTES_S : float
    FLOW_PACKETS_S : float
    FLOW_IAT_MEAN : float
    FLOW_IAT_STD : float
    FLOW_IAT_MAX : float
    FLOW_IAT_MIN : float
    FWD_IAT_TOTAL : float
    FWD_IAT_MEAN : float
    FWD_IAT_STD : float
    FWD_IAT_MAX : float
    FWD_IAT_MIN : float
    BWD_IAT_TOTAL : float
    BWD_IAT_MEAN : float
    BWD_IAT_STD : float
    BWD_IAT_MAX : float
    BWD_IAT_MIN : float
    FWD_PSH_FLAGS : float
    BWD_PSH_FLAGS : float
    FWD_URG_FLAGS : float
    BWD_URG_FLAGS : float
    FWD_HEADER_LENGTH : float
    BWD_HEADER_LENGTH : float
    FWD_PACKETS_S : float
    BWD_PACKETS_S : float
    MIN_PACKET_LENGTH : float
    MAX_PACKET_LENGTH : float
    PACKET_LENGTH_MEAN : float
    PACKET_LENGTH_STD : float
    PACKET_LENGTH_VARIANCE : float
    FIN_FLAG_COUNT : float
    SYN_FLAG_COUNT : float
    RST_FLAG_COUNT : float
    PSH_FLAG_COUNT : float
    ACK_FLAG_COUNT : float
    URG_FLAG_COUNT : float
    CWE_FLAG_COUNT : float
    ECE_FLAG_COUNT : float
    DOWN_UP_RATIO : float
    AVERAGE_PACKET_SIZE : float
    AVG_FWD_SEGMENT_SIZE : float
    AVG_BWD_SEGMENT_SIZE : float
    FWD_AVG_BYTES_BULK : float
    FWD_AVG_PACKETS_BULK : float
    FWD_AVG_BULK_RATE : float
    BWD_AVG_BYTES_BULK : float
    BWD_AVG_PACKETS_BULK : float
    BWD_AVG_BULK_RATE : float
    SUBFLOW_FWD_PACKETS : float
    SUBFLOW_FWD_BYTES : float
    SUBFLOW_BWD_PACKETS : float
    SUBFLOW_BWD_BYTES : float
    INIT_WIN_BYTES_FORWARD : float
    INIT_WIN_BYTES_BACKWARD : float
    ACT_DATA_PKT_FWD : float
    MIN_SEG_SIZE_FORWARD : float
    ACTIVE_MEAN : float
    ACTIVE_STD : float
    ACTIVE_MAX : float
    ACTIVE_MIN : float
    IDLE_MEAN : float
    IDLE_STD : float
    IDLE_MAX : float
    IDLE_MIN : float
    LABE : float
    
    class Config:
        from_attributes : True

    