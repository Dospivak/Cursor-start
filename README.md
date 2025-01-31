# 🚀 Getting Started with Python and MySQL in Cursor

Hey there! This is a starter kit to help you build websites using Python. We've set everything up to work with Cursor (a super-smart code editor) to make coding easier and more fun!

## 👋 First Things First

You'll need to install three things on your computer:
1. [Cursor](https://cursor.sh/) - Your new smart code editor
2. [MySQL](https://dev.mysql.com/downloads/) - Where we'll store our data
3. [Node.js](https://nodejs.org) - Helps with making the website look pretty

## �� Getting the Code

The easiest way to get started is to use Cursor's AI to help you:

### Using Cursor's AI (Recommended)
1. Open Cursor
2. Press `Cmd/Ctrl + K` (or click the chat button)
3. Type this in the chat:
   ```
   Pull the repository from https://github.com/Dospivak/Cursor-start
   ```
4. The AI will help you get the code and explain what's happening!

### Alternative Ways
If you prefer doing it manually:
- Click the green "Code" button on [this page](https://github.com/Dospivak/Cursor-start)
- Click "Download ZIP"
- Unzip the file where you want your project to be

## ✨ What's Special About This Template?

We've included lots of helpful stuff:
- Smart code suggestions
- Easy debugging tools
- Automatic code formatting
- Testing tools
- Error checking
- Beautiful styling with Tailwind CSS

## 🎯 Setting Up Your Project

### 1. Open in Cursor
- Open Cursor
- Click "Open Folder" (or press `Cmd/Ctrl + O`)
- Find and select the folder you just downloaded

### 2. Set Up Your Coding Environment
Open the terminal in Cursor (press ``Cmd/Ctrl + ` ``) and type these commands:

```bash
# Create a special environment for your project
python -m venv venv

# On Mac/Linux, type:
source venv/bin/activate
# On Windows, type:
venv\Scripts\activate

# Install Python packages
pip install -r requirements.txt

# Install styling tools
npm install

# Copy settings file
cp .env.example .env
```

### 3. Set Up Your Database
Open the `.env` file and fill in your database info:
```
DB_HOST=localhost
DB_PORT=3306
DB_NAME=your_database_name
DB_USER=your_username
DB_PASSWORD=your_password

DEBUG=True
APP_SECRET_KEY=make-up-a-random-string
```

### 4. Start the Project
In the terminal:
```bash
# Start the style builder
npm run watch:css

# In a new terminal, start the website
python src/main.py
```

Visit `http://localhost:5000` in your web browser to see your website!

## 🎨 Cool Things You Can Do with Cursor

### Ask AI for Help
- Type `/` and ask things like:
  - "Create a login page"
  - "Add a contact form"
  - "Fix this error"

### Get Code Explanations
- Select some code
- Press `Cmd/Ctrl + K`
- Ask "What does this code do?"

### Quick Keyboard Tricks
- `Cmd/Ctrl + P`: Find files
- `Cmd/Ctrl + K`: Chat with AI
- `Cmd/Ctrl + I`: Get code suggestions
- `Cmd/Ctrl + Shift + L`: Format your code

## 📁 Where to Find Things

```
your-project/
├── src/              # Your code lives here
│   ├── main.py      # The main program
│   ├── templates/   # Website pages
│   ├── static/      # Images, CSS, etc.
│   ├── models/      # Database stuff
│   └── utils/       # Helper tools
├── tests/           # Testing files
└── logs/            # Error logs
```

## 👩‍💻 Making Changes

### Adding a New Page
1. In Cursor, right-click on `templates/`
2. Click "New File"
3. Name it something like `about.html`
4. Add this code:
   ```html
   {% extends "base.html" %}
   
   {% block content %}
   <div class="container mx-auto px-4">
       <h1 class="text-2xl font-bold">My New Page</h1>
       <p>Hello there!</p>
   </div>
   {% endblock %}
   ```

### Working with the Database
Here's how to save user info:
```python
from src.models.user import User

user = User()
new_user = user.create({
    'username': 'john',
    'email': 'john@example.com'
})
```

### Making Things Look Pretty
Add styles in `src/static/css/input.css`:
```css
@layer components {
  .cool-button {
    @apply px-4 py-2 bg-blue-500 text-white rounded-lg 
           hover:bg-blue-600;
  }
}
```

## 🐞 When Things Go Wrong

1. Look for red error messages in the terminal
2. Check `logs/app.log` for more details
3. Add logging to see what's happening:
   ```python
   from loguru import logger
   logger.debug("What's happening:", my_variable=some_value)
   ```

## 🧪 Testing Your Code

In the terminal:
```bash
# Run all tests
pytest

# See how much of your code is tested
pytest --cov=src
```

## 🆘 Getting Help

### When You're Stuck
1. Ask Cursor's AI:
   - Select the problematic code
   - Press `Cmd/Ctrl + K`
   - Ask "What's wrong here?"

2. Check these websites:
   - [Cursor Help](https://cursor.sh/docs)
   - [Python Basics](https://docs.python.org/3/tutorial/)
   - [Flask Website Guide](https://flask.palletsprojects.com/)
   - [Tailwind CSS Help](https://tailwindcss.com/docs)

## 🌟 Try These First

Start with these simple tasks:
1. Change the website title
2. Add an "About" page
3. Create a contact form
4. Add some colorful buttons

Remember:
- Cursor's AI is there to help - use it!
- It's okay to experiment and make mistakes
- Ask for help when you need it
- Have fun building your website!
