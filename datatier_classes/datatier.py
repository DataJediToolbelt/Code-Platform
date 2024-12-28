from dataclasses import dataclass
from operator import concat

@dataclass
class datatier:
    datatier_name: str
    datatier_description: str
    datatier_type: str
    datatier_source: str
    datatier_source_type: str
    datatier_source_location: str

@dataclass
class datatier_sdp_datagenerated:
    datatier_sdp_datagenerated_name: str