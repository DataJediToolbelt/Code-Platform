from dataclasses import dataclass


@dataclass
class Audit_ErrorHandling:
        name: str
        event_type: str
        event_datetime: str
        event_date: str
        event_time: str
        component_name: str
        operation_name: str
        transaction_count: int
        processed_objectname: str
        event_special_comments: str
        start_datetime: str
        end_datetime: str
        error_id: str
        error_desc: str
        audit_details: str

        # def __init__(self):
        #     self.event_type = None
        #     self.event_datetime = None
        #     self.component_name = None
        #     self.operation_name = None
        #     self.processed_objectname = None
        #     self.event_count = 0
        #     self.event_output = None
        #     self.event_special_comments = None
        #     self.start_datetime = None
        #     self.end_datetime = None
        #     self.erorr_id = None
        #     self.error_desc = None