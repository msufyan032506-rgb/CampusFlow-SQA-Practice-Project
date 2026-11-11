# CampusFlow — SQA Manual Testing Practice Website

A Flask + HTML + CSS campus management demo. This is intentionally different from an e-commerce website and includes 7 main interfaces:

1. Dashboard
2. Students (search, add, duplicate-email validation, delete)
3. Courses (search)
4. Attendance (record attendance and validate fields)
5. Announcements
6. Reports
7. Help / Contact (form validation)

## Requirements
- Python 3.10+
- Internet connection only for the optional image download step

## Windows setup (VS Code terminal / PowerShell)
Open the folder containing `app.py`, then run:

```powershell
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python download_images.py
python app.py
```

If PowerShell blocks activation, skip activation and run:
```powershell
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe download_images.py
.venv\Scripts\python.exe app.py
```

Open `http://127.0.0.1:5000`.

## Image behavior
`download_images.py` downloads the website photos into `static/images/`. Run it once after setup. If a photo host is unavailable, the website still loads and its layout remains usable.

## Important demo notes
- Data is stored in Python memory; restarting the server resets changes.
- This is a learning/testing application, not a production student information system.
- Flask debug mode is enabled for local practice only. Do not deploy it publicly as-is.

## Suggested SQA practice
Test positive and negative paths, required fields, invalid email, duplicate student email, search with matching/non-matching terms, delete confirmation, attendance status values, and help form minimum message length. Record actual results and screenshots in your test-case sheet.

## Administrator sign-in (demo)
- Username: `Sufyan`
- Password: `Sufyan@123`

All portal pages now require administrator sign-in. Use the Sign out icon in the sidebar to end the session. This is a local demonstration account; change the password and secret key before any public deployment. The demo account is configured in `app.py` and its password is stored as a Werkzeug password hash.

## Course details
Select any course card from the Courses page to open its course detail page and view the course outline, instructor, and enrolment count.

## Superior University visual theme
The sign-in page uses the included campus photo as a full-screen background and applies a Superior University maroon-and-navy visual theme. Run `python download_images.py` once to populate the image assets before launching the application.
