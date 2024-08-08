class Converter:
    def celsius_to_fahrenheit(self, c):
        return float(f"{(c * 9 / 5) + 32:.2f}")
    
    def fahrenheit_to_celsius(self, f):
        return float(f"{(f - 32) * 5 / 9:.2f}")

    def celsius_to_kelvin(self, c):
        return float(f"{c + 273.15:.2f}")

    def kelvin_to_celsius(self, k):
        if( k < 0 ):
            raise ValueError("Temperature cannot be below absolute zero in Kelvin")
    
        return float(f"{k - 273.15:.2f}")

    def fahrenheit_to_kelvin(self, f):
        k = (f - 32) * 5 / 9 + 273.15
        if(k < 0):
            raise ValueError("Temperature cannot be below absolute zero in Kelvin")
        
        return float(f"{k:.2f}")

    def kelvin_to_fahrenheit(self, k):
        return float(f"{(k - 273.15) * 9 / 5 + 32:.2f}")