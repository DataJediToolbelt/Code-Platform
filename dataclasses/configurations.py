from dataclasses import dataclass
from operator import concat

@dataclass
class configuration_details:
    """Class for keeping track of an item in inventory."""
    configuration_value: str
    configuration_detail: str

    def complete_configuration(self) -> float:
        return concat(self.configuration_value+":"+self.configuration_detail)
