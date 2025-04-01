EventManagementApp/       # 📂 Main project folder (GitHub repository)
│── manage.py             # 🎯 Django management script (runserver, migrate, etc.)
│── Database.sqlite3      # 🗄️ Database file (renamed for clarity)
│── GlobalConfigs/        # ⚙️ Project configuration folder (previously EventApp)
│   ├── __init__.py       # 🏗️ Marks this as a Python package
│   ├── settings.py       # ⚙️ Main project settings (apps, database, static files)
│   ├── urls.py           # 🌍 Main URL routing (includes app URLs)
│   ├── asgi.py           # ⚡ ASGI configuration (for async support)
│   ├── wsgi.py           # 🚀 WSGI configuration (for deployment)
│── events/               # 📂 Main app folder (previously event_app)
│   ├── __init__.py       # 🏗️ Marks this as a Python package
│   ├── admin.py          # 🔑 Registers models for Django admin panel
│   ├── models.py         # 🏛️ Defines database models (Event, User, etc.)
│   ├── views.py          # 🎭 Handles page requests (renders templates, APIs)
│   ├── urls.py           # 🔗 App-specific URLs (connects views to routes)
│   ├── forms.py          # 📝 Handles form submissions (if using Django Forms)
│   ├── tests.py          # 🧪 Automated tests for the app
│   ├── templates/        # 🎨 Stores HTML templates for rendering pages
│   │   ├── events/       # 🔹 Keeps event-related templates organized
│   │   │   ├── home.html # 🏠 Home page template
│   │   │   ├── event.html # 📅 Single event page
│   ├── static/           # 🎨 Stores CSS, JavaScript, images
│   │   ├── css/          # 🎨 CSS stylesheets
│   │   ├── js/           # ⚡ JavaScript files
│   │   ├── images/       # 🖼️ Event-related images
