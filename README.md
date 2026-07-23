# Students Performance Prediction Using Machine Learning

A modern Django web application designed to predict student performance in Massive Open Online Courses (MOOCs) based on learning patterns, demographics, and assessment grades. The project is built using Python, Django, SQLite, and CanvasJS for data visualization.

---

## 🚀 Key Features

* **Unified Login Portal**: A modern, single login interface with smooth tab switches between Student and Service Provider login.
* **Responsive Visual Charts**: Interactive and fully visible Pie, Line, Spline, and Bar charts displaying student performance predictions and search metrics.
* **Pre-Populated Data**: Automatic database seeding from local Excel datasets (`College_DataSets.xlsx`).
* **Zero-Setup SQLite Database**: Uses a local SQLite database (`db.sqlite3`), eliminating the need for complex MySQL server configurations.
* **Case-Insensitive & Robust Authentication**: Supports whitespace trimming and case-insensitive usernames to prevent login errors.
* **Secure Searches**: Handles search query outcomes safely (prevents crashes when query matches multiple records).

---

## 🛠️ Tech Stack

* **Backend**: Python 3.13+, Django 6.0+
* **Database**: SQLite3
* **Frontend**: HTML5, CSS3, Bootstrap 4.0, Outfit Google Font
* **Libraries**: openpyxl, CanvasJS, SQLParse, Asgiref

---

## 🔑 Default Credentials

### 1. Student / Remote User Login
* **Username**: `Govind` | **Password**: `Govind`
* **Username**: `Manjunath` | **Password**: `Manjunath`
* **Username**: `Arvind` | **Password**: `Arvind`
* **Username**: `tmksmanju` | **Password**: `tmksmanju`

### 2. Service Provider Login (Admin Portal)
* **Username**: `sprovider`
* **Password**: `sprovider`

---

## 💻 Installation & How to Run

### Method A: One-Click Execution (Windows)
Double-click the **`run.bat`** file located in the root of the project. This will automatically activate the Python virtual environment and start the development server.

### Method B: Manual Commands
1. **Activate the virtual environment**:
   ```powershell
   .venv\Scripts\activate
   ```
2. **Start the Django server**:
   ```powershell
   python manage.py runserver
   ```
3. Open your browser and go to:
   **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

---

## 📊 Seeding the Database (Optional)
If you ever want to re-populate or import student records manually:
1. Log in under the **Student** tab.
2. Navigate to **Post Student Data Sets**.
3. Browse and upload the local **`College_DataSets.xlsx`** file included in the root directory.
