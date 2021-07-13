print("Celcius Converter")
Celcius = int(input("Input temperature (Celcius) : "))
Kelvin = Celcius + 273.15
Fahrenheit = Celcius*1.8  + 32
Rankine = 1.8*(Celcius + 491.67)
Delisle = (100 - Celcius)* 1.5
Newton = Celcius*33/100
Reaumur = Celcius*0.8
Romer = Celcius*21/40 + 7.5
print(Kelvin,Fahrenheit,Rankine,Delisle,Newton,Reaumur,Romer)
