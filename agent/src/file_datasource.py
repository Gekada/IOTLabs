from datetime import datetime
from domain.accelerometer import Accelerometer
from domain.gps import Gps
from domain.parking import Parking
from domain.aggregated_data import AggregatedData
import config


class FileDatasource:
    def __init__(
        self,
        accelerometer_filename: str,
        gps_filename: str,
        parking_filename: str,
    ) -> None:
        self.accelerometer_filename = accelerometer_filename
        self.gps_filename = gps_filename
        self.parking_filename = parking_filename
        self.accel_file = None
        self.gps_file = None
        self.parking_file = None

    def _read_line_or_restart(self, file_obj, filename) -> str:
        line = file_obj.readline()
        if not line:
            file_obj.seek(0)
            file_obj.readline()
            line = file_obj.readline()
        return line.strip()

    def read(self) -> AggregatedData:
        coords = [int(x) for x in self._read_line_or_restart(self.accel_file, self.accelerometer_filename).split(',')]
        gps = [float(x) for x in self._read_line_or_restart(self.gps_file, self.gps_filename).split(',')]
        parking_fields = self._read_line_or_restart(self.parking_file, self.parking_filename).split(',')

        parking = Parking(
            int(parking_fields[0]),
            Gps(float(parking_fields[1]), float(parking_fields[2]))
        )

        return AggregatedData(
            Accelerometer(*coords),
            Gps(*gps),
            datetime.now(),
            config.USER_ID,
        )

    def startReading(self):
        self.accel_file = open(self.accelerometer_filename)
        self.accel_file.readline()
        self.gps_file = open(self.gps_filename)
        self.gps_file.readline() 
        self.parking_file = open(self.parking_filename)
        self.parking_file.readline() 

    def stopReading(self):
        for f in (self.accel_file, self.gps_file, self.parking_file):
            if f:
                f.close()
