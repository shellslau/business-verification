from marshmallow import fields, Schema
import spacewalk

class BaseExampleJobSchema(spacewalk.BaseJobSchema):
    pass

class BaseExampleJob(spacewalk.BaseJob):
    NAME = "Spacewalk Example"
    BRANCH_NAME = "examples"
    DESCRIPTION = "example Spacewalk jobs"

    BASE_SCHEMA = BaseExampleJobSchema

    def run(self):
        self.job_log_info(f"starting {self.jobType} job {self.uuid}")
