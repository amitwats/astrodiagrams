class AngleDMS:
    def __init__(self, degrees=0, minutes=0, seconds=0):
        self.degrees = degrees
        self.minutes = minutes
        self.seconds = seconds

    def to_decimal_degrees(self):
        return self.degrees + self.minutes / 60 + self.seconds / 3600

    def from_decimal_degrees(decimal_degrees):
        degrees = int(decimal_degrees)
        decimal_minutes = (decimal_degrees - degrees) * 60
        minutes = int(decimal_minutes)
        seconds = (decimal_minutes - minutes) * 60
        return AngleDMS(degrees, minutes, seconds)

    def __add__(self, other):
        total_seconds = (self.to_decimal_degrees() + other.to_decimal_degrees()) * 3600
        degrees = int(total_seconds // 3600)
        remaining_seconds = total_seconds % 3600
        minutes = int(remaining_seconds // 60)
        seconds = remaining_seconds % 60
        return AngleDMS(degrees, minutes, seconds)

    def __gt__(self, other_angle_dms):
        return self.to_decimal_degrees()>other_angle_dms.to_decimal_degrees()

    def __lt__(self, other_angle_dms):
        return self.to_decimal_degrees()<other_angle_dms.to_decimal_degrees()

    def __le__(self, other_angle_dms):
        return self.to_decimal_degrees()<=other_angle_dms.to_decimal_degrees()

    def __ge__(self, other_angle_dms):
        return self.to_decimal_degrees()>=other_angle_dms.to_decimal_degrees()

    def __eq__(self, other_angle_dms):
        return self.to_decimal_degrees()==other_angle_dms.to_decimal_degrees()


    def __ne__(self, other_angle_dms):
        return self.to_decimal_degrees()!=other_angle_dms.to_decimal_degrees()


    def __repr__(self):
        return f"{self.degrees}° {self.minutes}' {self.seconds}\""
    

    def __str__(self):
        return f"{self.degrees}° {self.minutes}' {self.seconds}\""
    
