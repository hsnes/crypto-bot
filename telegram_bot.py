# crypto_bot/bot.py
import os
import django
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto_bot_project.settings')
django.setup()

from bot_app.models import UserProfile, Wallet, Transaction

# crypto_bot/bot.py
from bot_app.models import UserProfile


def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    private_key = b'your_private_key'

    user_profile, created = UserProfile.objects.get_or_create(
        user_id=user.id,
        defaults={'first_name': user.first_name, 'last_name': user.last_name, 'username': user.username,
                  'private_key': private_key}
    )
    if not created:
        user_profile.private_key = private_key
        user_profile.save()

    update.message.reply_text(f'Hi {user.first_name}! Welcome to the crypto wallet bot.')


# crypto_bot/bot.py
def get_private_key(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    user_profile = UserProfile.objects.get(user_id=user.id)
    private_key = user_profile.get_private_key()

    update.message.reply_text(f'Your private key is: {private_key}')


def buy(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    user_profile = UserProfile.objects.get(user_id=user.id)
    currency = context.args[0]
    amount = float(context.args[1])

    wallet, created = Wallet.objects.get_or_create(user=user_profile, currency=currency)
    wallet.balance += amount
    wallet.save()

    Transaction.objects.create(user=user_profile, transaction_type='buy', currency=currency, amount=amount)
    update.message.reply_text(f'{amount} {currency} bought successfully!')


def sell(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    user_profile = UserProfile.objects.get(user_id=user.id)
    currency = context.args[0]
    amount = float(context.args[1])

    wallet = Wallet.objects.get(user=user_profile, currency=currency)
    if wallet.balance >= amount:
        wallet.balance -= amount
        wallet.save()
        Transaction.objects.create(user=user_profile, transaction_type='sell', currency=currency, amount=amount)
        update.message.reply_text(f'{amount} {currency} sold successfully!')
    else:
        update.message.reply_text(f'Insufficient balance!')


def main() -> None:
    updater = Updater(settings.TELEGRAM_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("buy", buy))
    dispatcher.add_handler(CommandHandler("sell", sell))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
