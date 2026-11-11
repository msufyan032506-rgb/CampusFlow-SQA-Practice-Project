# CampusFlow — SQA Manual Testing Practice Website

CampusFlow is a web-based Campus Management System developed using **Python Flask, HTML, CSS, and JavaScript**. It is designed as a Software Quality Assurance (SQA) manual testing practice project.

The application provides a simple campus management environment where users can explore student records, courses, attendance, announcements, and reports.

## Features

1. **Dashboard** — Overview of campus information.
2. **Student Management** — Search, add, and delete student records with duplicate email validation.
3. **Course Management** — Browse and search available courses.
4. **Course Details** — View course outlines, instructors, and enrolment information.
5. **Attendance Management** — Record attendance and validate required fields.
6. **Announcements** — View campus announcements.
7. **Reports** — Access campus management reports.
8. **Help / Contact** — Submit contact forms with input validation.
9. **Admin Login** — Secure access to portal pages through administrator sign-in.

## Technologies Used

- Python 3
- Flask
- HTML5
- CSS3
- JavaScript
- Git and GitHub

## Requirements

- Python 3.10 or later
- pip
- Web browser

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/msufyan032506-rgb/CampusFlow-SQA-Practice-Project.git
```

### 2. Open the project folder

```bash
cd CampusFlow-SQA-Practice-Project
```

### 3. Create a virtual environment

```bash
py -m venv .venv
```

### 4. Activate the virtual environment

```powershell
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 6. Download website images

```bash
python download_images.py
```

### 7. Run the application

```bash
python app.py
```

Open your browser and visit:

`http://127.0.0.1:5000`

## Administrator Login

The project includes a demonstration administrator login for local testing.

Use the locally configured demo credentials. Do not publish passwords or secret keys in a public repository. Configure credentials and Flask secret keys securely before deployment.

## SQA Manual Testing Scope

This project can be used to practice:

- Positive and negative test scenarios
- Login validation
- Required field validation
- Invalid email validation
- Duplicate student email validation
- Student search functionality
- Student deletion confirmation
- Course search and course details
- Attendance status validation
- Contact form validation
- UI and navigation testing

## Project Limitations

- Data is stored in Python memory and resets when the server restarts.
- This application is developed for learning and manual testing practice.
- Flask debug mode is intended for local development only.
- The application is not production-ready.

## Future Improvements

- Database integration
- Automated testing using Selenium or Pytest
- Improved authentication and authorization
- Responsive UI enhancements
- Deployment to a cloud hosting platform

## Author

**Muhammad Sufyan**

GitHub: [msufyan032506-rgb](https://github.com/msufyan032506-rgb)

---

*CampusFlow — A practical project for learning Software Quality Assurance and Manual Testing.*
