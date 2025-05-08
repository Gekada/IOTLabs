from marshmallow import Schema, fields


class GpsSchema(Schema):
    longitude = fields.Float()
    latitude = fields.Float()
