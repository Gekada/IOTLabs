from schema.gps_schema import GpsSchema
from marshmallow import Schema, fields 

class ParkingSchema(Schema): 
 empty_count = fields.Int() 
 gps = fields.Nested(GpsSchema) 
