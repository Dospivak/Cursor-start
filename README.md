# 🚀 Python MySQL Template for Cursor

Welcome to your Python web project template optimized for Cursor! This template is designed to help you get started with web development using Python and Cursor's powerful features. Don't worry if some concepts are new - we'll explain everything step by step.

## 🎯 Prerequisites

Before you start, make sure you have:
1. [Cursor](https://cursor.sh/) installed on your computer
2. MySQL installed ([Download MySQL](https://dev.mysql.com/downloads/))
3. Node.js installed ([Download Node.js](https://nodejs.org))

## 🎨 What Makes This Template Special?

This template is specifically designed for Cursor users with:

- ✨ Pre-configured `.cursorrules` for optimal coding experience
- 🔍 Built-in code completion and suggestions
- 🐛 Advanced debugging capabilities
- 📝 Automatic code formatting
- 🧪 Integrated testing tools
- 🎯 Type checking and linting

## 🚀 Getting Started with Cursor

### 1️⃣ Open in Cursor

1. Open Cursor
2. Click "Open Folder" or use `Cmd/Ctrl + O`
3. Select the template directory

### 2️⃣ Using Cursor's Features

Cursor provides powerful AI assistance. Here are some tips:

- Type `/` to access AI commands
- Use `Cmd/Ctrl + K` to chat with AI
- Press `Cmd/Ctrl + I` for inline code suggestions
- Use `Cmd/Ctrl + Shift + L` for code formatting

### 3️⃣ Project Setup

Let Cursor help you set up the project. In the terminal (``Cmd/Ctrl + ` ``):

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
npm install

# Set up environment variables
cp .env.example .env
```

Edit `.env` with your database details:
```env
DB_HOST=localhost
DB_PORT=3306
DB_NAME=your_database_name
DB_USER=your_username
DB_PASSWORD=your_password

DEBUG=True
APP_SECRET_KEY=your-secret-key-here
```

### 4️⃣ Start Development

1. Build CSS (in terminal):
   ```bash
   npm run watch:css
   ```

2. Run the application (in a new terminal):
   ```bash
   python src/main.py
   ```

## 💡 Using Cursor's AI Features

### Code Generation
Type `/` and try these prompts:
- "Create a new Flask route for user profile"
- "Add a database model for blog posts"
- "Write a test for the user login function"

### Code Understanding
Select code and press `Cmd/Ctrl + K`, then ask:
- "Explain this code"
- "How can I improve this?"
- "What are potential bugs here?"

### Debugging
When you encounter errors:
1. Click the Debug icon in Cursor
2. Set breakpoints by clicking line numbers
3. Use the debug console to inspect variables

## 🗂️ Project Structure

```
your-project/
├── .cursorrules        # Cursor-specific settings
├── src/
│   ├── main.py        # Application entry point
│   ├── templates/     # HTML templates
│   ├── static/        # Assets (CSS, JS, images)
│   ├── models/        # Database models
│   └── utils/         # Helper functions
├── tests/             # Test files
└── logs/              # Application logs
```

## 👩‍💻 Development with Cursor

### Creating a New Page

1. Right-click on `templates/` → "New File"
2. Create `new_page.html`:
   ```html
   {% extends "base.html" %}
   
   {% block content %}
   <div class="container mx-auto px-4">
       <h1 class="text-2xl font-bold">My New Page</h1>
       <p>Hello, World!</p>
   </div>
   {% endblock %}
   ```

3. Use Cursor's AI to generate the route (type `/`):
   ```python
   @app.route('/new-page')
   def new_page():
       return render_template('new_page.html')
   ```

### Working with Database Models

Use Cursor's code completion while typing:
```python
from src.models.user import User

user = User()
new_user = user.create({
    'username': 'john',
    'email': 'john@example.com'
})
```

### Styling with Tailwind

Add styles in `src/static/css/input.css`:
```css
@layer components {
  .my-button {
    @apply px-4 py-2 bg-blue-500 text-white rounded-lg 
           hover:bg-blue-600 transition-colors;
  }
}
```

## 🐞 Debugging in Cursor

1. Set breakpoints by clicking line numbers
2. Use the Debug panel (bug icon)
3. Add logging:
   ```python
   from loguru import logger
   
   logger.debug("Debugging value:", value=my_variable)
   ```

## 🧪 Testing

Run tests using Cursor's integrated terminal:
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src
```

## 🔍 Cursor Tips & Tricks

- Use `Cmd/Ctrl + P` to quickly open files
- Use `Cmd/Ctrl + Shift + F` to search across all files
- Press `F2` to rename variables/functions across files
- Use `Alt + Up/Down` to move lines
- Type `///` for documentation generation

## 🆘 Getting Help

1. Use Cursor's AI help:
   - Select code and press `Cmd/Ctrl + K`
   - Ask "What's wrong with this code?"
   - Ask "How can I fix this error?"

2. Common issues:
   - Check the terminal for error messages
   - Look in `logs/app.log`
   - Use Cursor's debug console

3. External resources:
   - [Cursor Documentation](https://cursor.sh/docs)
   - [Python Tutorial](https://docs.python.org/3/tutorial/)
   - [Flask Documentation](https://flask.palletsprojects.com/)
   - [Tailwind CSS Documentation](https://tailwindcss.com/docs)

## 🌟 First Tasks in Cursor

Try these tasks using Cursor's features:
1. Use AI to generate a new database model
2. Add a new page with Cursor's file creation
3. Debug a function using breakpoints
4. Use code completion to write tests

Remember:
- Use Cursor's AI assistance whenever you're stuck
- Experiment with different AI prompts
- Take advantage of code completion
- Use the integrated debugger 