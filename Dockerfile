FROM debian:bookworm-slim
RUN dpkg --add-architecture i386 && apt update #לאפשר 32 סביות
RUN apt install -y wine wine32 wine64 xvfb #להוריד wine להרצת קבצי exe ואת xvfb לדמות מסך

