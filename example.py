from includes import buspreise
import datetime

instance = Buspreise()

data = instance.getLowestPrice('München', 'Berlin', datetime.datetime.now())

print("Provider: "+data['provider'])
print("Price: "+data['price'])
print("Departure: "+data['departure'])
print("Duration: "+data['duration'])
