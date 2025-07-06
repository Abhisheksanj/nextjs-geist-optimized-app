# MobileOSINT Backend

This is the Django REST Framework backend for the MobileOSINT application.

## Features

- Mobile number lookup API
- User information aggregation
- Dataset integration
- CAPTCHA verification
- Abuse protection and logging

## Setup

1. Create a virtual environment and activate it.
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Run the development server: `python manage.py runserver`

## API Endpoints

- POST /api/lookup/ - Lookup mobile number information
- Admin panel for managing data sources and abuse reports

## Notes

- Integrates Kaggle datasets and public leaks
- Supports live data scraping and API connectors
