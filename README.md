# Weather API: Current Weather Information

## About the Project

This project demonstrates how to use **Django Rest Framework** & **Celery** to create an API for fetching real-time
weather data for various countries. **Flower** is also used for monitoring Celery tasks.

### Technologies Used

- **[Django](https://www.djangoproject.com/)**: A high-level Python web framework for rapid development.
- **[Django Rest Framework](https://www.django-rest-framework.org/)**: A powerful toolkit for building web APIs with
  Django.
- **[Celery](https://docs.celeryq.dev/en/stable/)**: A distributed task queue focused on real-time processing and task
  scheduling.
- **[Flower](https://flower.readthedocs.io/en/latest/)**: A web application for monitoring and managing Celery tasks.
- **[SQLite](https://www.sqlite.org/)**: A lightweight SQL database engine used for data storage.

---

## Production Release 🌍

### Project URL

[Project URL](https://yyx9kq-8000.csb.app/)

### Flower URL

[Flower URL](https://yyx9kq-5001.csb.app/)

To access the Django admin panel, use:

- **Username**: `admin`
- **Password**: `admin123`

---

## User Authentication Endpoints 🔗

### 1. **Sign Up**

**POST** `/api/v1/user/sign/up/`

This endpoint allows users to sign up for a new account. You need to provide the user's data in the request body.

#### Request Body:

```json
{
  "username": "username",
  "name": "User Name",
  "surname": "User Surname",
  "password": "password"
}
```

#### Response Format (Success - 201 Created):

```json
{
  "user": {
    "username": "username",
    "name": "User Name",
    "surname": "User Surname",
    "is_active": true
  },
  "token": "generated_token"
}
```

#### Response Format (Error - 400 Bad Request):

```json
{
  "username": [
    "This field is required."
  ]
}
```

---

### 2. **Sign In**

**POST** `/api/v1/user/sign/in/`

This endpoint allows users to sign in to their account and receive a token.

#### Request Body:

```json
{
  "username": "username",
  "password": "password"
}
```

#### Response Format (Success - 200 OK):

```json
{
  "user": {
    "username": "username",
    "name": "User Name",
    "surname": "User Surname",
    "is_active": true
  },
  "token": "generated_token"
}
```

#### Response Format (Error - 400 Bad Request):

```json
{
  "non_field_errors": [
    "Unable to log in with provided credentials."
  ]
}
```

---

## Weather Endpoints 🔗

**GET** `/weather/`

- **Description**: Retrieves a list of weather data for all available regions.

- **Response**:

  ```json
  [
    {
      "name": "Toshkent",
      "country": "Uzbekistan",
      "lat": 41.3167,
      "lon": 69.25,
      "temp_c": 1.1,
      "temp_color": "#E6F7FF",
      "wind_kph": 5.0,
      "wind_color": "#E0F7FA",
      "cloud": 100.0,
      "cloud_color": "#616161"
    },
    {
      "name": "City of London, Greater London",
      "country": "United Kingdom",
      "lat": 51.5171,
      "lon": -0.1062,
      "temp_c": 6.2,
      "temp_color": "#E6F7FF",
      "wind_kph": 9.0,
      "wind_color": "#E0F7FA",
      "cloud": 25.0,
      "cloud_color": "#FFF176"
    }
  ]
  ```

---

**GET** `/weather/retrieve/`

- **Description**: Retrieves weather data for specific regions. Use the `region` query parameter to specify one or more
  regions.

- **Query Parameter**: `region` (can be repeated to specify multiple regions)

- **Example Request**:

  ```bash
  GET /weather/retrieve/?region=Tokyo&region=London
  ```

- **Response**:

  ```json
  [
    {
      "region": "Tokyo",
      "country": "Japan",
      "lat": 35.6895,
      "lon": 139.6917,
      "temp_c": 25.4,
      "temp_color": "#FF5733",
      "wind_kph": 15.5,
      "wind_color": "#33FF57",
      "cloud": 70,
      "cloud_color": "#FF33FF"
    },
    {
      "region": "London",
      "country": "United Kingdom",
      "lat": 51.5074,
      "lon": -0.1278,
      "temp_c": 16.5,
      "temp_color": "#FFFF33",
      "wind_kph": 10.2,
      "wind_color": "#33FFFF",
      "cloud": 50,
      "cloud_color": "#FF33FF"
    }
  ]
  ```

- **Error Response**:

  ```json
  {
    "status": "error",
    "message": "Region is required"
  }
  ```

---

**POST** `/weather/retrieve-multiple/`

- **Description**: Retrieves weather data for multiple regions in a single request. Pass a list of regions in the
  request body.

- **Request Body**:

  ```json
  {
    "regions": ["Paris", "Berlin"]
  }
  ```

- **Response**:

  ```json
  [
    {
      "name": "Ile-de-France",
      "country": "France",
      "lat": 48.8667,
      "lon": 2.3333,
      "temp_c": 1.2,
      "temp_color": "#E6F7FF",
      "wind_kph": 7.2,
      "wind_color": "#E0F7FA",
      "cloud": 0,
      "cloud_color": "#FFF9C4"
    },
    {
      "name": "Berlin",
      "country": "Germany",
      "lat": 52.5167,
      "lon": 13.4,
      "temp_c": 3.0,
      "temp_color": "#E6F7FF",
      "wind_kph": 16.6,
      "wind_color": "#B2EBF2",
      "cloud": 75,
      "cloud_color": "#9E9E9E"
    }
  ]
  ```

- **Error Response**:

  ```json
  {
    "status": "error",
    "message": "At least one Region is required"
  }
  ```

---

<details>
  <summary style="font-size: 1.5em; font-weight: bold;"><strong>Setup Instructions ⚙️️</strong></summary>

## Clone Project

To get started, clone the repository:

```bash
git clone https://github.com/Abduraxmonnn/Weather-API.git
cd Weather-API
```

## Requirements Before Running

- **Redis**: Celery requires Redis for message brokering. Follow the
  official [Redis installation guide](https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/).

## API Key Setup

1. **Create a `.env` file** in the root directory.
2. **Add your API key** inside `.env`:

   ```plaintext
   WEATHER_API_KEY=your_api_key_here
   ```

## Install Dependencies & Migrate Database

### Linux

```bash
python3 -m venv venv 
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
```

### Windows

```bash
python3 -m venv ./venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
```

### MacOS

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
```

### Advanced: Using Poetry

```bash
poetry install
poetry shell
```

</details>


---

<details>
  <summary style="font-size: 1.5em; font-weight: bold;"><strong>Run the Project 🚀</strong></summary>

### 1. **Start Redis Server**

Make sure Redis is installed and running.

```bash
redis-server
```

### 2. **Start the Django Application**

Ensure your virtual environment is activated, then run:

```bash
python manage.py runserver
```

### 3. **Start Celery Worker**

Celery is responsible for executing background tasks.

```bash
celery -A config worker --loglevel=info
```

or in debug mode:

```bash
celery -A config worker -l debug
```

### 4. **Start Celery Beat**

Celery Beat is used for scheduled tasks.

```bash
celery -A config beat --loglevel=info
```

### 5. **Optional: Start Flower**

For monitoring Celery tasks:

```bash
celery -A config flower --port=5001
```

Then open [Flower Dashboard](http://localhost:5001/) in your browser.

---

### Summary of Commands:

```bash
redis-server
python manage.py runserver
celery -A config worker --loglevel=info
celery -A config beat --loglevel=info
celery -A config flower --port=5001  # Optional
```

</details>
