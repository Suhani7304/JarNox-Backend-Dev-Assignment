# JarNox Backend Dev Assignment

A FastAPI backend project for stock metrics and related API services.  
This repository implements a Python backend with a clean structure for routes, services, and utilities.

---

## 🚀 Project Overview

This project is built using **FastAPI**, a modern Python web framework for building REST APIs with automatic documentation. It includes:

- API routes for stocks and metrics
- Modular project structure
- Async support via Uvicorn
- Clean separation of services and utilities

---

## 📁 Project Structure

app/
│── main.py
├── routes/
│ └── stocks.py
├── services/
│ └── metrics_service.py
│ └── stock_services.py
└── utils/
└── cleaner.py

requirement.txt
test_fetch.py

---

## 🛠️ Requirements

Make sure you have Python installed (3.10+ recommended).

Install dependencies:
pip install -r requirement.txt

---

## 🚀 Run the Application

To run the FastAPI development server:

uvicorn app.main:app --reload
