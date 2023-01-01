echo "Cloning Repo...."
git clone https://github.com/TECHNOBOT-OP/tbot /tbot
cd /tbot
pip3 install -r requirements.txt
echo "Starting Bot...."
python3 -m Technobot
