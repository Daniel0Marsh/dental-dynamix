#!/bin/bash

# CodeBlock.io Deployment Script
# This script handles the complete deployment process including gunicorn service management

set -e  # Exit on any error

echo "🚀 Starting CodeBlock.io deployment..."

# Configuration
PROJECT_DIR="/home/daniel/codeblock-website-v3"
SERVICE_NAME="gunicorn-codeblock"
SERVICE_FILE="/etc/systemd/system/${SERVICE_NAME}.service"

# Navigate to project directory
cd "$PROJECT_DIR"

# Backup current state
echo "📦 Creating backup..."
BACKUP_DIR="source.backup.$(date +%Y%m%d_%H%M%S)"
cp -r source "$BACKUP_DIR"

# Pull latest changes
echo "⬇️ Pulling latest changes..."
git pull origin main

# Poetry handles virtual environment management
echo "🔧 Setting up Poetry environment..."

# Install Poetry if not already installed
echo "📦 Installing Poetry..."
if ! command -v poetry &> /dev/null; then
    echo "Installing Poetry..."
    curl -sSL https://install.python-poetry.org | python3 - || {
        echo "❌ Poetry installation failed. Trying alternative method..."
        pip install poetry
    }
    export PATH="$HOME/.local/bin:$PATH"
    
    # Verify Poetry installation
    if ! command -v poetry &> /dev/null; then
        echo "❌ Poetry installation failed completely"
        exit 1
    fi
fi

echo "✅ Poetry version: $(poetry --version)"

# Install dependencies using Poetry
echo "📦 Installing dependencies with Poetry..."
echo "🔍 Poetry virtual environment location:"
poetry env info --path
echo "🔧 Forcing Poetry to create virtual environment in project..."
poetry config virtualenvs.in-project true --local
poetry env remove --all || true
poetry install --only main --no-interaction || {
    echo "❌ Poetry install failed"
    exit 1
}
echo "🔍 After installation - Poetry virtual environment location:"
poetry env info --path
echo "📁 Checking if .venv directory exists:"
ls -la .venv/ || echo "❌ .venv directory not found"

# Verify Django installation
echo "🔍 Verifying Django installation..."
poetry run python -c "import django; print(f'Django version: {django.get_version()}')" || {
    echo "❌ Django verification failed"
    exit 1
}

# Check for any missing dependencies
echo "🔍 Checking for missing dependencies..."
poetry run python -c "
import sys
required_modules = ['django', 'captcha', 'django_ckeditor_5', 'psycopg2', 'requests', 'decouple']
missing = []
for module in required_modules:
    try:
        __import__(module)
    except ImportError:
        missing.append(module)
if missing:
    print(f'Missing modules: {missing}')
    sys.exit(1)
else:
    print('All required modules found!')
" || {
    echo "❌ Dependency check failed"
    exit 1
}

# Run migrations
echo "🗄️ Running migrations..."
cd source
poetry run python manage.py migrate --noinput || {
    echo "❌ Migration failed"
    exit 1
}

# Collect static files
echo "📁 Collecting static files..."
poetry run python manage.py collectstatic --noinput --clear || {
    echo "❌ Static files collection failed"
    exit 1
}

# Test Django configuration
echo "🧪 Testing Django configuration..."
poetry run python manage.py check --deploy || {
    echo "⚠️ Django deployment check failed, but continuing..."
}

# Return to project root for virtual environment verification
cd ..

# Verify virtual environment and gunicorn
echo "🔍 Verifying virtual environment setup..."
echo "📁 Current directory: $(pwd)"
echo "🔍 Poetry virtual environment path:"
POETRY_VENV_PATH=$(poetry env info --path)
echo "📁 Poetry virtual environment: $POETRY_VENV_PATH"
echo "📁 Checking .venv directory:"
ls -la .venv/ || echo "❌ .venv directory not found"
echo "📁 Checking .venv/bin directory:"
ls -la .venv/bin/ || echo "❌ .venv/bin directory not found"

# Check both .venv and Poetry's actual virtual environment
GUNICORN_PATH=""
if [ -f ".venv/bin/gunicorn" ]; then
    GUNICORN_PATH=".venv/bin/gunicorn"
elif [ -f "$POETRY_VENV_PATH/bin/gunicorn" ]; then
    GUNICORN_PATH="$POETRY_VENV_PATH/bin/gunicorn"
fi

if [ -z "$GUNICORN_PATH" ]; then
    echo "❌ Gunicorn not found in virtual environment"
    echo "🔧 Installing gunicorn in virtual environment..."
    poetry add gunicorn || {
        echo "❌ Failed to install gunicorn"
        exit 1
    }
    echo "📁 After gunicorn installation:"
    ls -la .venv/bin/gunicorn || echo "❌ Gunicorn still not found in .venv"
    ls -la "$POETRY_VENV_PATH/bin/gunicorn" || echo "❌ Gunicorn still not found in Poetry venv"
fi

echo "✅ Virtual environment verification complete"

# Setup directories
echo "🔧 Setting up directories..."
sudo mkdir -p /run/gunicorn
sudo chown daniel:daniel /run/gunicorn
sudo chmod 755 /run/gunicorn

sudo mkdir -p /var/log/gunicorn
sudo chown daniel:daniel /var/log/gunicorn
sudo chmod 755 /var/log/gunicorn

# Setup systemd service
echo "🔧 Setting up systemd service..."
# Determine the correct gunicorn path
if [ -f ".venv/bin/gunicorn" ]; then
    GUNICORN_PATH=".venv/bin/gunicorn"
elif [ -f "$POETRY_VENV_PATH/bin/gunicorn" ]; then
    GUNICORN_PATH="$POETRY_VENV_PATH/bin/gunicorn"
else
    echo "❌ Could not find gunicorn executable"
    exit 1
fi

echo "🔍 Using gunicorn path: $GUNICORN_PATH"

# Create a temporary service file with the correct path
TEMP_SERVICE_FILE="/tmp/gunicorn-codeblock.service"
cp "$PROJECT_DIR/gunicorn.service" "$TEMP_SERVICE_FILE"
sed -i "s|ExecStart=.*|ExecStart=$GUNICORN_PATH core.wsgi:application --bind unix:/run/gunicorn/codeblock.sock --workers 3 --timeout 120 --keep-alive 2 --max-requests 1000 --max-requests-jitter 100 --access-logfile /var/log/gunicorn/access.log --error-logfile /var/log/gunicorn/error.log --log-level info|" "$TEMP_SERVICE_FILE"

sudo cp "$TEMP_SERVICE_FILE" "$SERVICE_FILE"

# Reload systemd and enable service
echo "🔄 Reloading systemd..."
sudo systemctl daemon-reload

# Stop any existing gunicorn processes
echo "🛑 Stopping existing gunicorn processes..."
sudo pkill -f "gunicorn.*codeblock-website.sock" || true
sleep 2

# Enable and start the service
echo "▶️ Starting gunicorn service..."
sudo systemctl enable "$SERVICE_NAME"
sudo systemctl start "$SERVICE_NAME"

# Wait for service to start
echo "⏳ Waiting for service to start..."
sleep 5

# Check service status
echo "🔍 Checking service status..."
if sudo systemctl is-active --quiet "$SERVICE_NAME"; then
    echo "✅ Gunicorn service is running"
else
    echo "❌ Gunicorn service failed to start"
    sudo systemctl status "$SERVICE_NAME"
    exit 1
fi

# Restart Nginx
echo "🌐 Restarting Nginx..."
sudo systemctl restart nginx

# Health check
echo "🏥 Performing health check..."
sleep 3
for i in {1..5}; do
    if curl -f http://localhost > /dev/null 2>&1; then
        echo "✅ Deployment successful!"
        echo "🎉 CodeBlock.io is now live!"
        exit 0
    else
        echo "⚠️ Health check attempt $i failed, retrying..."
        sleep 2
    fi
done

echo "❌ Health check failed after 5 attempts"
echo "🔍 Checking service logs..."
sudo journalctl -u "$SERVICE_NAME" --no-pager -n 20
exit 1 