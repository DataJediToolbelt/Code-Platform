from dataclasses import dataclass
from operator import concat

@dataclass
class configuration_details:
    configuration_value: str
    configuration_detail: str

    #def complete_configuration(self) -> float:
    #    return concat(self.configuration_value+":"+self.configuration_detail)
    #def __init__(self,  configuration_value,  configuration_detail):
    #    self. configuration_value =  configuration_value
    #    self.configuration_detail = configuration_detail
