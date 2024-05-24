# Crypto Bot

Crypto Wallet Bot is a Telegram bot that allows users to create a wallet, buy, sell, and exchange cryptocurrencies. This bot is built using Django for the backend and the python-telegram-bot library for Telegram API integration.

## Features

- User registration and profile management
- Cryptocurrency wallet creation and management
- Buy and sell cryptocurrencies
- Transaction history tracking
- Django admin panel for managing users and transactions

## Getting Started

### Prerequisites

- Python 3.7+
- Telegram account

### Installation

1. Clone the repository:

```bash
git clone https://github.com/hsnes/crypto-bot.git
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```
4. Set up the sensitive settings in settings.py:
- Edit the settings.py file and set the SECRET_KEY, TELEGRAM_TOKEN, and CRYPTO_KEY variables with your own values:

```python
# settings.py

# Add your secret key here
SECRET_KEY = 'your_secret_key'

# Set DEBUG to True for development, False for production
DEBUG = True

# Add your Telegram bot token here
TELEGRAM_TOKEN = 'your_telegram_token'

# Add your encryption key here
CRYPTO_KEY = b'your_crypto_key'  # Note: This must be a byte string

# Rest of the settings...

```
5. Apply migrations to set up the database:

```bash
python manage.py makemigrations
python manage.py migrate
```
6. Create a superuser for accessing the Django admin panel:

```bash
python manage.py createsuperuser
```

7. Run the development server:

```bash
python manage.py runserver
```

8. Start the Telegram bot:

```bash
python crypto_bot/bot.py
```

## Usage

### Commands

- /start - Register and start interacting with the bot
- /buy <currency> <amount> - Buy a specified amount of a cryptocurrency
- /sell <currency> <amount> - Sell a specified amount of a cryptocurrency

### Admin Panel

Access the Django admin panel at http://127.0.0.1:8000/admin to manage users, wallets, and transactions.

### Security

- Store sensitive information like tokens and secret keys securely.
- Use encryption for storing sensitive data.
- Ensure all communications with the bot and server use HTTPS.
