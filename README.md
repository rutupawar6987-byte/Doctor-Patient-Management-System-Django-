PROJECT TITLE: Doctor–Patient Management System (Django)

DESCRIPTION:
This project is a web-based application developed using Django. 
It allows three types of users:
1. Admin
2. Doctor
3. Patient

Each user has their own dashboard after login. 
The admin can manage all doctors and patients.
Doctors can view their profile, update details, and see assigned patient history.
Patients can view their profile, edit personal details, and see list of available doctors.

---------------------------------------------------------
FEATURES:

1. USER AUTHENTICATION
   - Registration and login for Doctor and Patient
   - Role-based redirection:
       Doctor → doctor dashboard
       Patient → patient dashboard
       Admin → admin panel

2. DOCTOR MODULE
   - Add doctor profile
   - Edit doctor profile
   - View list of patients (if assigned)
   - View doctor dashboard with profile information

3. PATIENT MODULE
   - Add patient profile
   - Edit patient profile
   - View patient dashboard
   - View available doctors list
   - View patient history

4. PATIENT HISTORY
   - Add patient history
   - Update patient history
   - Delete patient history
   - View history list

5. DASHBOARDS
   - Doctor Dashboard: shows doctor info and patient list
   - Patient Dashboard: shows patient info and all doctors list

6. ROLE-BASED ACCESS CONTROL
   - Only doctors can access doctor management pages
   - Only patients can access patient pages
   - Both can view doctor list

---------------------------------------------------------
TECHNOLOGIES USED:
- Python 3
- Django Framework
- HTML, CSS, Bootstrap
- SQLite (default Django database)

---------------------------------------------------------
FOLDER STRUCTURE:

project_folder/
│
├── manage.py
├── db.sqlite3
├── project_name/            → main project settings
│
├── doctor1/                 → doctor app
│   ├── models.py
│   ├── views.py
│   └── templates/doctor1/
│       ├── doctor_list.html
│       ├── doctor_form.html
│       ├── dashboard.html
│       └── doctor_confirm_delete.html
│
├── patient1/                → patient app
│   ├── models.py
│   ├── views.py
│   └── templates/patient1/
│       ├── dashboard.html
│       ├── patient_list.html
│       ├── patient_form.html
│       ├── patient_detail.html
│       └── patienthistory_xxx.html
│
├── templates/
│   ├── base.html
│   ├── registration/
│       ├── login.html
│       └── register.html
│   ├── _navbar.html
│   └── _messages.html
│
└── static/                  → CSS, JS, images

---------------------------------------------------------
HOW TO RUN THE PROJECT:

1. Install required dependencies:
   pip install django

2. Run database migrations:
   python manage.py makemigrations
   python manage.py migrate

3. Start the development server:
   python manage.py runserver

4. Open in browser:
   http://127.0.0.1:8000/

---------------------------------------------------------
DEFAULT SUPPORT LINKS:
- Admin Login: /admin/
- User Login: /accounts/login/
- Registration: /accounts/register/

---------------------------------------------------------
NOTES:
- Make sure to create a superuser for admin:
  python manage.py createsuperuser
- Doctor and Patient profile must be created after user registration.

