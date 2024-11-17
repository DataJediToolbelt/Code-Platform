from dataclasses import dataclass
from operator import concat

@dataclass
class connections_details:
    connection_name: str
    connection_type: str
    host_name: str
    port_number: int
    uid: str
    pwd: str
    key: str
    token:str
    additional_token: str
    additional_details: str