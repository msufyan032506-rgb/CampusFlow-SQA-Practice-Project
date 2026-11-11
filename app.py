from flask import Flask, render_template, request, redirect, url_for, flash, session
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "campusflow-sqa-local-demo-secret-change-before-deployment"
admin_user = {"username": "Sufyan", "password_hash": generate_password_hash("Sufyan@123")}

students = [
    {"id": 1001, "name": "Ayesha Khan", "email": "ayesha@example.com", "program": "Computer Science", "status": "Active"},
    {"id": 1002, "name": "Hamza Ali", "email": "hamza@example.com", "program": "Information Technology", "status": "Active"},
    {"id": 1003, "name": "Sara Ahmed", "email": "sara@example.com", "program": "Software Engineering", "status": "Inactive"},
]
courses = [
    {"code": "CS101", "name": "Introduction to Programming", "instructor": "Mr. Usman", "students": 42, "description": "Learn programming fundamentals, problem solving, and structured programming.", "outline": ["Introduction to programming and problem solving", "Algorithms, pseudocode, and flowcharts", "Variables, data types, and operators", "Conditional statements and loops", "Functions and modular programming", "Arrays, strings, and basic data structures", "Debugging, testing, and a mini project"]},
    {"code": "IT204", "name": "Database Systems", "instructor": "Ms. Hira", "students": 35, "description": "Study relational database concepts, SQL, design, and database management.", "outline": ["Database concepts and DBMS architecture", "Entity Relationship (ER) modelling", "Relational model and keys", "Normalization (1NF, 2NF, 3NF)", "SQL: DDL, DML, and queries", "Joins, views, and subqueries", "Transactions, security, and backup"]},
    {"code": "SE301", "name": "Software Quality Assurance", "instructor": "Mr. Bilal", "students": 28, "description": "Understand software quality practices, testing levels, test design, and defect management.", "outline": ["Introduction to software quality and SQA", "Software development life cycle and quality models", "Verification, validation, and reviews", "Testing fundamentals and testing principles", "Black-box and white-box testing techniques", "Unit, integration, system, and acceptance testing", "Test planning, test cases, and test reports", "Defect life cycle and bug tracking", "Automation testing overview", "SQA standards, metrics, and project"]},
]
announcements = [
    {"title": "Mid-term examination schedule", "date": "2026-11-18", "category": "Exams"},
    {"title": "Library will remain open until 8 PM", "date": "2026-11-12", "category": "Campus"},
    {"title": "SQA workshop registrations are open", "date": "2026-11-20", "category": "Events"},
]
attendance = [
    {"student": "Ayesha Khan", "course": "CS101", "date": "2026-11-10", "status": "Present"},
    {"student": "Hamza Ali", "course": "IT204", "date": "2026-11-10", "status": "Absent"},
    {"student": "Sara Ahmed", "course": "SE301", "date": "2026-11-10", "status": "Present"},
]

@app.before_request
def require_login():
    if request.endpoint not in {"login", "static"} and not session.get("admin_logged_in"):
        return redirect(url_for("login", next=request.path))

@app.context_processor
def inject_user():
    return {"current_admin": session.get("admin_username", "Sufyan")}

@app.route("/login", methods=["GET", "POST"])
def login():
    if session.get("admin_logged_in"):
        return redirect(url_for("dashboard"))
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        if username.casefold() == admin_user["username"].casefold() and check_password_hash(admin_user["password_hash"], password):
            session.clear()
            session["admin_logged_in"] = True
            session["admin_username"] = "Sufyan"
            flash("Welcome back, Sufyan!", "success")
            next_url = request.args.get("next") or url_for("dashboard")
            if not next_url.startswith("/") or next_url.startswith("//"):
                next_url = url_for("dashboard")
            return redirect(next_url)
        flash("Incorrect username or password. Please try again.", "error")
    return render_template("login.html")

@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    flash("You have been signed out.", "success")
    return redirect(url_for("login"))

@app.route("/")
def dashboard():
    return render_template("dashboard.html", active="dashboard", students=students, courses=courses, announcements=announcements)

@app.route("/students", methods=["GET", "POST"])
def student_list():
    if request.method == "POST":
        name = request.form.get("name", "").strip(); email = request.form.get("email", "").strip(); program = request.form.get("program", "").strip()
        if len(name) < 3 or "@" not in email or "." not in email.split("@")[-1] or not program:
            flash("Please enter a valid name, email address, and program.", "error")
        elif any(s["email"].lower() == email.lower() for s in students):
            flash("A student with this email already exists.", "error")
        else:
            students.append({"id": max([s["id"] for s in students], default=1000)+1, "name": name, "email": email, "program": program, "status": "Active"})
            flash("Student added successfully.", "success"); return redirect(url_for("student_list"))
    q = request.args.get("q", "").strip().lower()
    filtered = [s for s in students if q in (s["name"]+" "+s["email"]+" "+s["program"]).lower()]
    return render_template("students.html", active="students", students=filtered, total=len(students), q=q)

@app.post("/students/<int:student_id>/delete")
def delete_student(student_id):
    match = next((s for s in students if s["id"] == student_id), None)
    if match: students.remove(match); flash("Student record deleted.", "success")
    else: flash("Student record was not found.", "error")
    return redirect(url_for("student_list"))

@app.route("/courses")
def course_list():
    q = request.args.get("q", "").strip().lower()
    filtered = [c for c in courses if q in (c["code"]+" "+c["name"]+" "+c["instructor"]).lower()]
    return render_template("courses.html", active="courses", courses=filtered, q=q)

@app.route("/courses/<course_code>")
def course_detail(course_code):
    course = next((c for c in courses if c["code"].lower() == course_code.lower()), None)
    if not course:
        flash("The selected course could not be found.", "error"); return redirect(url_for("course_list"))
    return render_template("course_detail.html", active="courses", course=course)

@app.route("/attendance", methods=["GET", "POST"])
def attendance_page():
    if request.method == "POST":
        student=request.form.get("student","").strip(); course=request.form.get("course","").strip(); day=request.form.get("date","").strip(); status=request.form.get("status","").strip()
        if not student or not course or not day or status not in ("Present", "Absent", "Late"): flash("Complete all fields with valid values.", "error")
        else: attendance.insert(0, {"student":student,"course":course,"date":day,"status":status}); flash("Attendance saved.", "success"); return redirect(url_for("attendance_page"))
    return render_template("attendance.html", active="attendance", attendance=attendance, students=students, courses=courses, today=date.today().isoformat())

@app.route("/announcements")
def announcement_page(): return render_template("announcements.html", active="announcements", announcements=announcements)

@app.route("/reports")
def reports():
    present=sum(1 for a in attendance if a["status"]=="Present"); absent=sum(1 for a in attendance if a["status"]=="Absent")
    return render_template("reports.html", active="reports", students=students, courses=courses, attendance=attendance, present=present, absent=absent)

@app.route("/help", methods=["GET", "POST"])
def help_page():
    if request.method == "POST":
        name=request.form.get("name","").strip(); email=request.form.get("email","").strip(); message=request.form.get("message","").strip()
        if len(name)<2 or "@" not in email or len(message)<10: flash("Enter your name, a valid email, and a message of at least 10 characters.", "error")
        else: flash("Your support request has been submitted (demo only).", "success"); return redirect(url_for("help_page"))
    return render_template("help.html", active="help")

if __name__ == "__main__":
    app.run(debug=True)
