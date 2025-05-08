from domain.gps import Gps 
from dataclasses import dataclass

@dataclass
class Parking: 
 empty_count: int 
 gps: Gps 
