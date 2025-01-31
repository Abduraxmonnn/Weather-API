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

## Clone Project

To get started, clone the repository:

```bash
git clone https://github.com/Abduraxmonnn/Weather-API.git
cd Weather-API
```

---

## Requirements Before Running

- **Redis**: Celery requires Redis to be installed for message brokering. You can follow the
  official [Redis installation guide](https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/) for
  your platform.

---

## API Key Setup

To securely store and use your API key for a third-party weather service (e.g., WeatherAPI), follow these steps:

1. **Create a `.env` file**  
   In the root directory of your project (where `manage.py` is located), create a file named `.env`.

2. **Add your API key**  
   Open the `.env` file and add the following line:

   ```plaintext
   WEATHER_API_KEY=your_api_key_here
   ```

---

## Setup the Project

### Installation Instructions

1. **Linux**:

   ```bash
   virtualenv -p /usr/bin/python3 .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   python manage.py migrate
   ```

2. **Windows**:

   ```bash
   python -m venv ./venv
   venv\Scripts\activate
   pip install -r requirements.txt
   python manage.py migrate
   ```

3. **MacOS**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python manage.py migrate
   ```

---

## Advanced Setup

For advanced users, you can use **[Poetry](https://python-poetry.org/)** for managing dependencies and virtual
environments:

1. Install dependencies with Poetry:
   ```bash
   poetry install
   ```

2. Activate the Poetry environment:
   ```bash
   poetry shell
   ```

---

## User Authentication Endpoints

### 1. **Sign Up**

### `POST /api/v1/user/sign/up/`

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

### `POST /api/v1/user/sign/in/`

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

## Weather Endpoints

### `GET /weather/`

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

### `GET /weather/retrieve/`

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

### `POST /weather/retrieve-multiple/`

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

## Views Methods

- **`list()`**: Returns a list of weather data for all regions.
- **`retrieve()`**: Retrieves weather data for specific regions (based on query parameters).
- **`retrieve_multiple()`**: Retrieves weather data for multiple regions in one request.

---

## Additional Notes

- The weather data and color codes are fetched from the database. Ensure your database is populated with weather and
  color code data.

- The `get_weather_data_service()` function fetches the weather data for a given region from a third-party service or
  another internal source.
  Sure! Here's the updated **Additional Notes** section with your cron job instructions added:

- **Weather Data Fetching Task**:
    - The weather data fetching task (`save_weather_data_in_db`) is scheduled using **Celery** and **Cron Jobs**.
    - By default, the task is set to run **once every day at midnight** (00:00) using a **Cron Job**. This is configured
      with the following code:

      ```python
      schedule, created = CrontabSchedule.objects.get_or_create(
          minute='0',
          hour='0',
          day_of_week='*',
          day_of_month='*',
          month_of_year='*',
          timezone=zoneinfo.ZoneInfo('Asia/Tashkent')
      )
      ```

    - If you want to **test the task every 60 seconds** (instead of daily), you can use the **interval-based schedule**
      by uncommenting the following code:

      ```python
      # schedule, interval_created = IntervalSchedule.objects.get_or_create(
      #     every=60,
      #     period=IntervalSchedule.SECONDS,
      # )
      ```

    - After uncommenting the interval-based schedule, the task will run every 60 seconds for testing purposes.

- **Task Path**: The Celery task that fetches and saves the weather data is located in the following path:
  ```plaintext
  apps.weather.tasks.save_weather_data_in_db
  ```

## Run the Project

To run the project, you will need to start the following services:

1. **Django Application** (the web server)
2. **Redis** (the message broker for Celery)
3. **Celery Worker** (to execute background tasks)
4. **Celery Beat** (to schedule periodic tasks)
5. **Flower** (optional) - For monitoring Celery tasks.

### 1. **Start Redis Server**

First, make sure you have Redis installed and running. Redis is used as the message broker for Celery.

- **On Linux/macOS**:

  You can start Redis with the following command:

  ```bash
  redis-server
  ```

- **On Windows**:

  You can download and run Redis from [Redis for Windows](https://github.com/microsoftarchive/redis/releases).

### 2. **Start the Django Application**

To run the Django app, ensure your virtual environment is activated and the required dependencies are installed. Then,
run the Django development server:

This will start the Django application on `http://127.0.0.1:8000/`.

### 3. **Start the Celery Worker**

Celery is responsible for executing background tasks. To start the Celery worker, run:

```bash
celery -A config worker --loglevel=info
```

or

```bash
celery -A config worker -l debug
```

### 4. **Start Celery Beat**

Celery Beat is used to schedule periodic tasks. To start Celery Beat, run:

```bash
celery -A config beat --loglevel=info
```

or

```bash
celery -A config beat -l debug
```

This will start the scheduler and execute tasks according to the periodic schedules you’ve set (e.g., the cron job for
fetching weather data).

### 5. **Optional: Start Flower (For Monitoring Celery Tasks)**

**Flower** is an optional web-based tool for monitoring and managing Celery tasks in real-time. To start Flower, run:

```bash
celery -A config flower --port=5001
```

Once Flower is running, you can access the dashboard at `http://localhost:5001/` to monitor the status of your Celery
workers and tasks.

---

### 6. **Django Admin Panel Authentication**

To access the Django admin panel, use the following credentials:

- **Username**: `admin`
- **Password**: `admin123`

---

Let me know if you'd like to adjust anything further!

### Summary of Commands

1. **Start Redis server**: `redis-server`
2. **Run Django app**: `python manage.py runserver`
3. **Start Celery Worker**: `celery -A config worker --loglevel=info`
4. **Start Celery Beat**: `celery -A config beat --loglevel=info`
5. **Optional: Start Flower**: `celery -A config flower --port=5555`

Make sure all of these processes are running in separate terminals to keep everything working smoothly.
