from datetime import date
from marshmallow import Schema, fields,validate


class SensorSchema(Schema):
    id = fields.Int()
    # measurement_type = fields.Str(validate=validate.OneOf(["celsius"]), required=True)
    measurement_type = fields.Str(required=True)
    timestamp = fields.DateTime()
    value = fields.Float(required = True)

class DesiredoutputSchema(Schema):
    MAX_VALUE = fields.Float()
    MIN_VALUE = fields.Float()
    MEAN_VALUE = fields.Float()
    timestamps = fields.List(fields.DateTime())
    
    




