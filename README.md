# Arbitrage Script

Script that analyzes bitcoin prices on two exchanges and then calculates if arbitrage trade is profitable.
If it is, it sends notification thorugh pushbullet api.

# Deployment
The script is designed to run on Heroku and it will run every two hours with the use of Heroku Scheduler.
Pushbullet API key is needed for the notificiations.
