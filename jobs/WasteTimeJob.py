from marshmallow import fields, Schema
import random
import spacewalk
import time

class WasteTimeJob(BaseExampleJob):
    NAME = "Waste Time Job"
    LEAF_NAME = "waste_time"
    DESCRIPTION = "Randomly logs while wasting time"

    class Params(Schema):
        delay = fields.Integer()

    def run(self):
        super().run()

        end = time.time() + self.delay
        logInterval = self.delay / 10

        while True:
            if time.time() > end:
                break

            logDelay = (random.random() + 0.5) * logInterval
            time.sleep(logDelay)
            self.add_to_completeness(logDelay / self.delay)
            self.job_log_info(f"{end - time.time():.2f} seconds remaining")

        return 200, None
