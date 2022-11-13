FROM TECHNOBOT-OP/TECHNOUSERBOT:slim-buster

#clonning repo 

RUN git clone https://github.com/TECHNOBOT-OP/TECHNOUSERBOT.git /root/Technobot

#working directory 
WORKDIR /root/Technobot

# Install requirements
RUN pip3 install --no-cache-dir -r requirements.txt


ENV PATH="/home/Technobot/bin:$PATH"

CMD ["python3","-m","Technobot"]
