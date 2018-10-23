import eventlet
from eventlet.green import socket

PORT = 3001
participants = set()

def read_chat_forever(writer, reader, address):
    line = reader.readline()
    while line:
        print('Chat:', line.strip())
        for p in participants:
            try:
                if p is not writer:  # Don't echo
                    msg = address[0] + ':'
                    msg += line
                    p.write(msg)
                    p.flush()
            except socket.error as e:
                # ignore broken pipes, they just mean the participant
                # closed its connection already
                if e[0] != 32:
                    raise
        line = reader.readline()
    participants.remove(writer)
    print("participant left chat")

try:
    print("ChatServer starting up on port %s" % PORT)
    server = eventlet.listen(('0.0.0.0', PORT))
    while True:
        new_connection, address = server.accept()
        print("Participant joined chat.")
        new_writer = new_connection.makefile('w')
        participants.add(new_writer)
        eventlet.spawn_n(
            read_chat_forever,
            new_writer,
            new_connection.makefile('r'),
            address)
except (KeyboardInterrupt, SystemExit):
    print("ChatServer exiting")