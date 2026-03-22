from fastapi import FastAPI, status, Response, Query
from typing import Optional
from pydantic import BaseModel, Field

app = FastAPI()

# Q1
@app.get('/')
def home():
    return {'message': 'Welcome to SpeedRide Car Rentals'}


# Q2
cars = [
    {"id": 1, "model": "City", "brand": "Honda", "type": "Sedan", "price_per_day": 2500, "fuel_type": "Petrol", "is_available": True},
    {"id": 2, "model": "i20", "brand": "Hyundai", "type": "Hatchback", "price_per_day": 1500, "fuel_type": "Petrol", "is_available": True},
    {"id": 3, "model": "Nexon", "brand": "Tata", "type": "SUV", "price_per_day": 3000, "fuel_type": "Diesel", "is_available": False},
    {"id": 4, "model": "Model 3", "brand": "Tesla", "type": "Luxury", "price_per_day": 8000, "fuel_type": "Electric", "is_available": True},
    {"id": 5, "model": "Fortuner", "brand": "Toyota", "type": "SUV", "price_per_day": 5000, "fuel_type": "Diesel", "is_available": True},
    {"id": 6, "model": "3 Series", "brand": "BMW", "type": "Luxury", "price_per_day": 7000, "fuel_type": "Petrol", "is_available": False},
    {"id": 7, "model": "Thar", "brand": "Mahindra", "type": "SUV", "price_per_day": 3500, "fuel_type": "Petrol", "is_available": True},
    {"id": 8, "model": "E-Class", "brand": "Mercedes-Benz", "type": "Luxury", "price_per_day": 9500, "fuel_type": "Diesel", "is_available": True},
    {"id": 9, "model": "ZS EV", "brand": "MG", "type": "SUV", "price_per_day": 4000, "fuel_type": "Electric", "is_available": True},
    {"id": 10, "model": "Swift", "brand": "Maruti", "type": "Hatchback", "price_per_day": 1200, "fuel_type": "Petrol", "is_available": True}
]

@app.get('/cars')
def get_all_cars():
    total = len(cars)
    
    available_cars = [car for car in cars if car['is_available'] == True]
    available_count = len(available_cars)
    
    return{
        'cars': cars,
        'total': total,
        'available_count': available_count,
    }
    
    
# Q3
@app.get('/cars/{car_id}')
def get_car(car_id: int):
    for car in cars:
        if car['id'] == car_id:
            return {'cars': car}
    return {'error': 'Car not found.'}
    
    
# Q4
