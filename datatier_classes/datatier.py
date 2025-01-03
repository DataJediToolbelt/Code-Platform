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
    dataattribute_id: str
    datagentype_id:str
    param_value: str
    param_value_dtl: str
    maintained_date: str
    referenceapp_guid: str
    organization_guid: str