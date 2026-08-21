# OrderIQ Architecture

Version: 1.0

Status: Active

Last Updated: August 2026

---

# Overview

OrderIQ follows a modular, layered architecture designed for maintainability, scalability, and future enterprise deployment.

The application is divided into independent layers where each layer has a clear responsibility.

```
Frontend (React + TypeScript)
        │
        ▼
REST API (FastAPI)
        │
        ▼
Business Logic
        │
        ▼
Database Layer
        │
        ▼
SQLite (Current)
PostgreSQL (Future)
```

---

# Technology Stack

## Frontend

- React
- TypeScript
- Vite
- Tailwind CSS
- React Router
- Axios

---

## Backend

- Python
- FastAPI
- Uvicorn

---

## Database

Current

SQLite

Future

PostgreSQL

---

## AI & Processing

Python

PDF Processing

Text Extraction

Data Validation

AI Assisted Parsing

---

# Project Structure

```
api/
    API Endpoints

database/
    Database
    Search Engine

frontend/
    React Application

docs/
    Product Documentation

data/
    Raw Files
    Processed Files
    Downloads
```

---

# Backend Layers

API Layer

↓

Validation

↓

Business Logic

↓

Database

↓

Response

Each endpoint should perform only one responsibility.

---

# Frontend Layers

Pages

↓

Layouts

↓

Reusable Components

↓

Services

↓

API

Pages should never communicate directly with the backend.

All requests must go through Service files.

---

# Database Principles

Single source of truth

No duplicated information

Normalized tables where appropriate

Indexes on searchable fields

Soft delete support in future

Audit history in future

---

# API Principles

RESTful endpoints

Consistent naming

Proper HTTP methods

Meaningful status codes

JSON responses

Validation before database operations

---

# Component Strategy

Every reusable UI element belongs inside:

frontend/src/components/ui

Examples

Button

Card

Table

Modal

Badge

Sidebar

Topbar

StatCard

PDFViewer

No duplicate UI implementations.

---

# Security

Input validation

Parameterized queries

Role-based permissions

Authentication layer

Audit logs

Secure file access

---

# Performance Goals

Fast page loads

Lazy loading where appropriate

Reusable components

Efficient database queries

Minimal unnecessary API calls

---

# Future Architecture

```
React

↓

FastAPI

↓

Background Workers

↓

PostgreSQL

↓

Redis

↓

AI Services

↓

Analytics
```

---

# Development Workflow

Architecture

↓

Implementation

↓

Compilation

↓

Browser Testing

↓

Git Commit

Every feature follows this workflow.

---

# End of Architecture