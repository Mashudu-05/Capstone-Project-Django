# Vogue Maternity

This is a Django-based application for managing maternity dress rentals. Users can browse available dresses, register, log in, and manage their rentals. The project allows users to browse and rent maternity dresses from a collection, providing an easy-to-use platform for managing their rental history and account information.

---

## Setup Instructions

### 1. Set Up the Virtual Environment

**For Windows:**
```sh
python -m venv venv
.\venv\Scripts\activate
```

**For macOS/Linux:**
```sh
python3 -m venv venv
source venv/bin/activate
```

Once activated, your terminal should show the virtual environment name `(venv)`.

---

### 2. Install Dependencies

With the virtual environment activated, install all the necessary dependencies:
```sh
pip install -r requirements.txt
```

This command installs all the required Python packages listed in `requirements.txt`.

---

### 3. Set Up Environment Variables

To securely store your sensitive information, like Django's `SECRET_KEY` or database credentials, create a `.env` file in your project root directory.

**Example `.env` file:**
```ini
SECRET_KEY=your-django-secret-key
DEBUG=True
DATABASE_URL=your-database-url
```

Make sure to exclude the `.env` file from version control by adding it to your `.gitignore` file.

---

### 4. Running the Project Locally

#### 4.1. Apply Database Migrations

Ensure your database is set up correctly by running Django's migration commands:
```sh
python manage.py migrate
```

#### 4.2. Create a Superuser

If you want to access the Django admin interface, create a superuser by running:
```sh
python manage.py createsuperuser
```
Follow the prompts to set up the superuser account.

#### 4.3. Run the Development Server

Now, you can start the Django development server:
```sh
python manage.py runserver
```
The application will be available at [http://localhost:8000](http://localhost:8000).  
To access the admin interface, visit [http://localhost:8000/admin](http://localhost:8000/admin) and log in using the superuser credentials you created earlier.

---

## Docker Setup

If you prefer to run the project in a Docker container instead of setting it up locally, follow these steps:

### 5.1. Build the Docker Image

In the project directory, build the Docker image using the following command:
```sh
docker build -t vogue-maternity .
```
This will create the image with the tag `vogue-maternity`.

### 5.2. Run the Docker Container

Once the image is built, you can run the container and map port 8000 from the container to your local machine:
```sh
docker run -p 8000:8000 vogue-maternity
```
The application will now be available at [http://localhost:8000](http://localhost:8000) in your browser.

---

## GitHub Repository

You can find the source code for this project on GitHub:  
[https://github.com/Mashudu-05/Capstone-Project-Django](https://github.com/Mashudu-05/Capstone-Project-Django)