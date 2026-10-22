# Event Management API

## Project Overview

The Event Management API is a backend application developed using Python, Django, and Django REST Framework (DRF). It provides functionality for user registration, event booking requests, event management, and booking history.

Users can register and log in to the application, submit requests for events, and view their previous bookings. Authorized staff or admin users can review booking requests and create or confirm events according to the application's workflow.

The project demonstrates REST API development, token-based authentication, database management, and user-specific data handling.

## Features

### 1. User Registration and Login
- Users can register for an account.
- Registered users can log in.
- Token Authentication is used to access protected endpoints.

### 2. Event Booking Requests
- Users can submit requests for events.
- Users can specify their event requirements.
- Booking requests are handled by authorized staff or admin users.

### 3. Booking Request Management
- Staff or admin users can review booking requests.
- Requests can be accepted according to the implemented workflow.
- Accepted requests can proceed to event creation or confirmation.

### 4. Event Management
- Authorized staff or admin users can create events.
- Users can view available events according to the application's permissions and workflow.

### 5. Booking History
- Users can view their previous bookings.
- Booking history can include bookings made several months earlier, provided the records are retained in the database.
- Access to booking history should be restricted according to the application's permission rules.

## Technologies Used

- **Programming Language:** Python
- **Backend Framework:** Django
- **API Framework:** Django REST Framework
- **Database:** SQLite
- **Authentication:** Token Authentication
- **API Testing:** Postman
- **Version Control:** Git and GitHub

## Project Workflow

1. A user registers for an account.
2. The user logs in and obtains an authentication token.
3. The user submits an event booking request with the required details.
4. An authorized staff or admin user reviews the request.
5. If the request is accepted, the staff or admin creates or confirms the event according to the application's workflow.
6. The event becomes available for users to view, subject to the implemented permissions.
7. Users can access their own booking history to view previous bookings.

## Installation and Setup

### Prerequisites

Before running the project, ensure that the following are installed:

- Python
- pip
- Git
- A code editor, such as Visual Studio Code

### 1. Clone the Repository

```bash
git clone https://github.com/mohammedadenan/eventhub
cd eventapi
```

**Note:** Confirm that `eventapi` is the correct project directory created by cloning the repository. If the folder has a different name, use that name instead.

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**macOS / Linux:**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

If a `requirements.txt` file is included in the repository, install the dependencies using:

```bash
pip install -r requirements.txt
```

If the file is not present, install the dependencies specified by the project.

### 5. Apply Database Migrations

Run the following command from the directory containing `manage.py`:

```bash
python manage.py migrate
```

If changes have been made to the models and new migrations are required, run:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser (Optional)

To access Django Admin, if it is enabled in the project:

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

The local development server is usually available at:

`http://127.0.0.1:8000/`

Use the actual API paths configured in the project's URL configuration.

## API Endpoints

The following table is based on the endpoint names provided for this project. Confirm the complete URL paths and supported HTTP methods in your Django `urls.py` files before publishing.

| Feature | HTTP Method | Endpoint |
|---|---|---|
| User Registration | POST | `register` |
| User Login / Token | POST | `token` |
| Submit Booking Request | POST | `booking` |
| View Booking Requests | GET | `booking` |
| Create Event | POST | `event` |
| View Events | GET | `event` |
| View Booking History | GET | `history/` |

**Important:** These are the endpoint paths as supplied for the README. They may require a prefix such as `/api/`, depending on your URL configuration. Confirm whether the booking list returns all permitted bookings or only the current user's bookings. Also confirm which staff/admin actions are implemented before documenting them as API endpoints.

## Authentication

This project uses **Django REST Framework Token Authentication**.

For endpoints that require authentication, include the token in the request header:

```http
Authorization: Token YOUR_TOKEN_HERE
```

Replace `YOUR_TOKEN_HERE` with a valid token obtained through the authentication flow implemented in the project.

Never publish real authentication tokens, passwords, or secret keys.

### Authentication Steps

1. Register a user.
2. Log in or request a token using the configured authentication endpoint.
3. Copy the token from the response.
4. Include the token in the `Authorization` header for protected requests.

The exact request fields and response format depend on the project's serializers and views.

## Booking History

The booking history functionality allows users to view their previous bookings.

Historical records can remain available even when a booking was made several months ago, as long as the records are retained in the database and the API retrieves them correctly.

For secure access, the API should ensure that users can access only the booking records they are authorized to view. Confirm the implemented filtering and permission rules in the project code.

## Testing

API endpoints can be tested using Postman.

### Suggested Testing Checklist

- [ ] Register a new user.
- [ ] Log in and obtain an authentication token.
- [ ] Submit an event booking request.
- [ ] Verify that authorized staff/admin users can review requests.
- [ ] Test the implemented request acceptance workflow.
- [ ] Verify that authorized staff/admin users can create or confirm events.
- [ ] Retrieve the available event list.
- [ ] Retrieve booking history.
- [ ] Verify that users cannot access other users' private booking information without authorization.
- [ ] Test invalid input and unauthenticated requests.

Only mark a test as successful after verifying the actual API response in Postman.

## Project Structure

The exact project structure has not been supplied. Replace the placeholders below with the actual directory and file names from your repository.

```text
eventhub/
├── manage.py
├── [DJANGO_PROJECT_DIRECTORY]/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── [APP_DIRECTORY]/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── [OTHER APP FILES]
├── requirements.txt
└── README.md
```

This is an illustrative structure, not a verified listing of the repository's files.

## Database

The project uses **SQLite** as its database.

SQLite stores application data in a database file and is supported by Django with minimal configuration. Database settings are managed through the project's `settings.py` file.

Do not commit a database containing private user data or production records to a public repository.

## Security Considerations

- Keep Django secret keys and passwords private.
- Never publish real authentication tokens.
- Protect endpoints that require authentication.
- Apply appropriate permissions to booking management and event creation.
- Ensure users can access only the data permitted by the application.
- Avoid exposing passwords or other sensitive user information in API responses.
- Use a production-appropriate configuration before deployment.

## Future Improvements

The following are possible enhancements and are not claimed as existing features:

- API documentation using Swagger or OpenAPI.
- Automated API tests.
- More detailed booking status tracking.
- Pagination and filtering.
- Deployment configuration.

## Author

- **Name:** Mohammed Adenan P. E.
- **GitHub:** https://github.com/mohammedadenan
- **LinkedIn:** https://www.linkedin.com/in/mohammed-adenan-p-e-9581922a4

