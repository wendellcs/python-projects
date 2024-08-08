class Converter:
    def celsius_to_fahrenheit(self, c):
        f = (c * 9 / 5) + 32
        return float(f"{f:.2f}")
    
    def fahrenheit_to_celsius(self, f):
        c = (f - 32) * 5 / 9
        return float(f"{c:.2f}")


    def celsius_to_kelvin(self, c):
        k = c + 273.15
        return float(f"{k:.2f}")

    def kelvin_to_celsius(self, k):
        if( k < 0 ):
            raise ValueError("Temperature cannot be below absolute zero in Kelvin")
        
        c = k - 273.15
        return float(f"{c:.2f}")

    def fahrenheit_to_kelvin(self, f):
        k = (f - 32) * 5 / 9 + 273.15
        if(k < 0):
            raise ValueError("Temperature cannot be below absolute zero in Kelvin")
        
        return float(f"{k:.2f}")

    def kelvin_to_fahrenheit(self, k):
        f = (k - 273.15) * 9 / 5 + 32
        return float(f"{f:.2f}")