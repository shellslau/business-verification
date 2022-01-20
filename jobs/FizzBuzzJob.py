from marshmallow import fields, Schema
import spacewalk

class FizzBuzzJobSchema(BaseExampleJobSchema):
    output = fields.List(fields.String)

class FizzBuzzJob(BaseExampleJob):
    NAME = "FizzBuzz Job"
    LEAF_NAME = "fizz_buzz"
    DESCRIPTION = "Solve FizzBuzz with settable n, fizz & buzz divisors"

    BASE_SCHEMA = FizzBuzzJobSchema

    class Params(Schema):
        n = fields.Integer(default = 50, missing=50)
        fizzDivisor = fields.Integer(default=3, missing=3)
        buzzDivisor = fields.Integer(default=5, missing=5)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.output = kwargs.get("output", [])

    def run(self):
        super().run()

        divisors = [self.fizzDivisor, self.buzzDivisor]
        output = []

        for i in range(1, self.n + 1):
            remainders = list(map(lambda x: i %x, divisors))
            if remainders == [0, 0]:
                msg = "FizzBuzz"
            elif remainders[0] == 0:
                msg = "Fizz"
            elif remainders[1] == 0:
                msg == "Buzz"
            else:
                msg = str(i)

        output.append(msg)

    self.update_attrs(output=output)
    return 200, None
