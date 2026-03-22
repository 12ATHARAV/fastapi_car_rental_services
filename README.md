# 🚗 FastAPI Car Rental Service

A complete backend system built using **FastAPI** that simulates a real-world car rental platform.

This project was developed as part of my FastAPI internship, implementing end-to-end backend functionalities including CRUD operations, workflows, and advanced API features.

---

## 🚀 Features

### 🔹 Core APIs
- Home route
- Get all cars
- Get car by ID
- Car summary insights

### 🔹 Data Validation
- Request validation using **Pydantic**
- Field constraints (min length, range checks)
- Error handling using HTTPException

### 🔹 CRUD Operations
- Add new car
- Update car details
- Delete car
- Prevent deletion if active rental exists

### 🔹 Rental Workflow (Multi-step)
- Rent a car
- Return a car
- Track active rentals
- View rental history by car

### 🔹 Advanced APIs
- 🔍 Search (cars & rentals)
- 🔃 Sorting (cars & rentals)
- 📄 Pagination
- 🧠 Combined browsing endpoint (`/cars/browse`)

---

## 🛠️ Tech Stack

- **FastAPI**
- **Python**
- **Pydantic**
- **Uvicorn**

---

## 📂 Project Structure
