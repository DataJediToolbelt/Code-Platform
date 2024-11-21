from dataclasses import dataclass


@dataclass
class Audit_ErrorHandling:
        name: str
        event_type: str
        event_datetime: str
        component_name: str
        processing_run_datetime: str
        operation_name: str
        processing_objectname: str
        event_count: str
        event_output: str
        event_special_comments: str
        processing_start_time: str
        processing_end_time: str
        processing_duration_time_seconds: str
        processing_duration_time_milliseconds: str

        def __init__(self):
            self.event_type = None
            self.event_datetime = None
            self.component_name = None
            self.processing_run_datetime = None
            self.operation_name = None
            self.processing_objectname = None
            self.event_count = None
            self.event_output = None
            self.event_special_comments = None
            self.processing_start_time = None
            self.processing_end_time = None
            self.processing_duration_time_seconds = None
            self.processing_duration_time_milliseconds = None