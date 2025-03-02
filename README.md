# Spatial Data API

## Overview
A simple API to manage spatial data (points and polygons) using Django and DRF.

## Base URL
```
http://<your-domain>/api/
```

## Endpoints

### Spatial Points
- **GET** `/api/points/` - List all points
- **GET** `/api/points/{id}/` - Retrieve a point
- **POST** `/api/points/` - Create a new point
- **PUT/PATCH** `/api/points/{id}/` - Update a point
- **DELETE** `/api/points/{id}/` - Delete a point

### Spatial Polygons
- **GET** `/api/polygons/` - List all polygons
- **GET** `/api/polygons/{id}/` - Retrieve a polygon
- **POST** `/api/polygons/` - Create a new polygon
- **PUT/PATCH** `/api/polygons/{id}/` - Update a polygon
- **DELETE** `/api/polygons/{id}/` - Delete a polygon

## Setup
```sh
git clone <repo-url>
cd <project-folder>
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

- Data formats:
  - **Points:** `POINT(longitude latitude)`
  - **Polygons:** `POLYGON((x1 y1, x2 y2, ..., x1 y1))`
]
