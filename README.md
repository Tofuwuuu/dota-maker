# Dota Tournament Bracket Maker

A Flask-based web application for creating and managing Dota 2 tournaments with user authentication and role-based access control.

## 🎮 Overview

This application provides a platform for organizing Dota 2 tournaments with two distinct user roles:
- **Organizers**: Can create and manage tournaments
- **Players**: Can view tournaments and participate

## 🚀 Features

### Authentication System
- User registration with role selection (Player/Organizer)
- Secure login/logout functionality
- Session management with Flask-Login
- Role-based access control

### Tournament Management
- Tournament creation interface for organizers
- Dynamic tournament details form with JavaScript
- Tournament information including:
  - Tournament name
  - Date
  - Venue
  - Team registration
- In-line editing capabilities for tournament details

### User Interface
- Dark theme with modern design
- Responsive navigation bar
- Role-specific dashboard views
- Interactive forms with validation

## 🛠️ Technology Stack

### Backend
- **Flask**: Web framework
- **SQLAlchemy**: Database ORM
- **Flask-Login**: User session management
- **Flask-WTF**: Form handling and CSRF protection
- **WTForms**: Form validation

### Frontend
- **HTML5**: Markup
- **CSS3**: Styling with dark theme
- **JavaScript**: Interactive functionality
- **Jinja2**: Template engine

### Database
- **SQLite**: Lightweight database for development

## 📁 Project Structure

```
dota-maker/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── static/               # Static assets
│   └── css/
│       ├── base.css      # Navigation and base styles
│       ├── main.css      # Main application styles
│       └── register.css  # Registration page styles
└── templates/            # HTML templates
    ├── base/
    │   └── base.html     # Base template with navigation
    ├── main.html         # Main layout template
    ├── login.html        # Login page
    ├── register.html     # Registration page
    ├── dashboard.html    # User dashboard
    ├── create_tournament.html      # Tournament creation
    └── create_tournament_2.html    # Extended tournament creation
```

## 🔧 Installation & Setup

### Prerequisites
- Python 3.7+
- pip (Python package installer)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd dota-maker
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the application**
   - Open your browser and navigate to `http://localhost:5000`

## 🎯 Usage

### For New Users
1. **Register**: Click "Register" and select your role (Player or Organizer)
2. **Login**: Use your credentials to access the dashboard

### For Organizers
1. **Dashboard**: Access tournament creation tools
2. **Create Tournament**: Fill in tournament details (name, date, venue, teams)
3. **Manage**: Edit tournament details dynamically

### For Players
1. **Dashboard**: View available tournaments
2. **Participate**: Access tournament information

## 🗄️ Database Schema

### User Model
```python
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    role = db.Column(db.String(15), nullable=False)  # 'player' or 'organizer'
```

## 🎨 Design Features

- **Dark Theme**: Modern dark interface with red accents (#741c18, #701616)
- **Responsive Design**: Works on desktop and mobile devices
- **Interactive Elements**: Hover effects and smooth transitions
- **Form Validation**: Client and server-side validation
- **Dynamic Content**: JavaScript-powered tournament detail editing

## 🔒 Security Features

- **CSRF Protection**: Flask-WTF integration
- **Session Management**: Secure user sessions
- **Role-based Access**: Organizer-only tournament creation
- **Input Validation**: Form validation with WTForms

## 🚧 Current Limitations

- Password storage is not hashed (development only)
- No persistent tournament storage
- Limited tournament management features
- No bracket generation functionality yet

## 🔮 Future Enhancements

- [ ] Password hashing and encryption
- [ ] Tournament database persistence
- [ ] Bracket generation and management
- [ ] Team registration system
- [ ] Tournament scheduling
- [ ] Results tracking
- [ ] Email notifications
- [ ] Advanced tournament formats (single/double elimination)

## 📝 Development Notes

- The application runs in debug mode by default
- Database file (`db.sqlite3`) is created automatically
- Some template files contain placeholder content (e.g., "wew", "ewewew")
- Tournament creation has a two-step process (create_tournament.html → create_tournament_2.html)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

**Note**: This is a development version of the application. For production use, ensure proper security measures including password hashing, environment variable configuration, and database security.