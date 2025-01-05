


**Pro-Path** is a revolutionary web platform designed to guide university students in defining their academic and professional trajectories. By leveraging data from previous cohorts, Pro-Path provides personalized recommendations based on student performance, interests, and aspirations, while also adapting to market needs. Additionally, the platform connects students with mentors for personalized guidance.

---

## Key Features

1. **Personalized Path Recommendations**:
   - Students input their grades, interests, and internship preferences.
   - The platform uses a K-Nearest Neighbors (KNN) algorithm to recommend academic paths tailored to individual profiles.

2. **Mentorship Connection**:
   - Students can browse mentors' profiles, view their expertise, and request mentorship sessions directly through the platform.

3. **Scalable Design**:
   - Initially implemented for *Ecole Centrale Casablanca*, Pro-Path can be adapted to any institution with appropriate data.

4. **Administrative Support**:
   - Administrators can upload curriculum PDFs for students to download and explore.

5. **Secure Login System**:
   - Passwords are hashed using `bcrypt` for secure authentication.

6. **Email Notifications**:
   - Mentors can accept or deny mentorship requests, with email notifications sent to students.

---

## Technologies Used

### Frontend
- **HTML & CSS**: Responsive design for user interfaces (`mentor.html`, `student.html`, `student_account.html`).
- **Jinja2**: Dynamic content rendering in Flask templates.

### Backend
- **Python (Flask)**: Handles routing, authentication, and core logic.
- **Pandas**: For data manipulation and CSV processing.
- **Scikit-Learn**: Implements KNN for recommendation logic.

### Database
- **CSV Files**: Stores student and mentor data (`Student1.csv`, `Mentor1.csv`, `BD_PROF.csv`).

### Others
- **Bcrypt**: Secure password hashing.
- **SMTP**: For sending email notifications to students and mentors.

---

## Installation and Setup

### Prerequisites
- Python 3.8 or later
- Required libraries: Flask, Pandas, Scikit-Learn, Bcrypt, PIL

### Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/pro-path.git
   cd pro-path
   ```

2. **Install Dependencies**:
   ```bash
   pip install flask pandas scikit-learn bcrypt pillow
   ```

3. **Set Up Data Files**:
   - Ensure `Student1.csv`, `Mentor1.csv`, `data_final.xlsx`, and `BD_PROF.csv` are in the root directory.

4. **Run the Application**:
   ```bash
   python app.py
   ```

5. **Access the Application**:
   - Open your browser and navigate to `http://127.0.0.1:5000`.

---

## User Workflow

### For Students
1. **Sign Up**:
   - Register with your name, email, and password.
2. **Log In**:
   - Use your credentials to access the student dashboard.
3. **Fill Out the Recommendation Form**:
   - Enter grades, interests, and internship preferences.
   - Receive a personalized academic and professional path.
4. **Request Mentorship**:
   - Browse mentors by domain and expertise.
   - Submit a request specifying the topic, date, and time.
5. **Track Requests**:
   - View your mentorship requests and their statuses on the `student_account.html` page.

### For Mentors
1. **Log In**:
   - Access the mentor dashboard.
2. **View Requests**:
   - See mentorship requests from students.
3. **Accept or Deny Requests**:
   - Respond to requests directly from the platform.
   - Students are notified via email.

---

## Testing Credentials

### Student Account
- **Email**: `chafik.elkihal@centrale-casablanca.ma`
- **Password**: `elkihal`

---

## Project Structure

```
pro-path/
│
├── app.py                   # Main Flask application
├── Core.py                  # Core logic for recommendations
├── Mentor.py                # Mentor-specific functionalities
├── templates/               # HTML templates
│   ├── mentor.html          # Mentor dashboard
│   ├── student.html         # Student dashboard
│   ├── student_account.html # Student account page
│   ├── Log_in.html          # Login page
│   ├── sign_up.html         # Sign-up page
├── static/                  # Static files (CSS, JS, images)
│   ├── css/style.css        # General styles
│   ├── css/style_M.css      # Mentor page styles
│   ├── css/style_S.css      # Student page styles
│   ├── css/style_sign_up.css # Sign-up page styles
├── Student1.csv             # Student data
├── Mentor1.csv              # Mentor data
├── BD_PROF.csv              # Mentor profile data
├── data_final.xlsx          # Dataset for KNN recommendations
├── mentoring_request1.csv   # Mentoring requests (runtime file)
└── README.md                # Project documentation
```

---

## Features in Action

### 1. **Mentor Dashboard (`mentor.html`)**
Mentors can:
- View student mentorship requests.
- Accept or deny requests with a single click.
- See student contact details for follow-ups.

### 2. **Student Dashboard (`student.html`)**
Students can:
- Fill out a recommendation form for personalized academic guidance.
- Browse available mentors by name, domain, and LinkedIn profile.
- Submit mentorship requests and track responses.

### 3. **Student Account (`student_account.html`)**
Students can:
- View all their mentorship requests in one place.
- Check the status of each request.

---

## Future Enhancements

- Integrate a full database system (e.g., MySQL) for better scalability.
- Add a chatbot for quick student queries.
- Incorporate a scheduling system for mentorship meetings.
- Expand machine learning models to include more complex recommendation algorithms.

---

## License

this project is a school project made by
Mouad Farhi 
Sara kabil El hak 
Meryem irghis 
Emina Fradi 
nouhalia Hanini
