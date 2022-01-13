FROM RallsTeam/Ralls_thon:latest


RUN git clone https://github.com/RallsTeam/Ralls_thon.git /root/userbot

WORKDIR /root/userbot

# لتنـزيل اضافات السورس
RUN pip3 install -U -r resources/setup/requirements.txt

ENV PATH="/home/userbot/resources/setup/bin:$PATH"

CMD ["python3","-m","userbot"]
