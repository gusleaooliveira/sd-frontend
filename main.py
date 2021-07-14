import socketio as sio

socket = sio.Client()

@socket.event
def connect():
    print()
    print('Estamos conectados!')
    print()

@socket.event
def disconnect():
    print()
    print('Estamos desconectados!')
    print()

@socket.event
def error(erro):
    print()
    print(f'Ocorreu um erro {erro}')
    print()

@socket.on('previousMessages')
def previousMessages(mensagens):
    print()
    print('Mensagens:')
    for mensagem in mensagens:
        print(mensagem)
    print()

@socket.on('recivedMessage')
def recivedMessage(mensagem):
    print()
    print('Nova mensagem:')
    print(mensagem)
    print()

@socket.event
def sendMessage(mensagem):
    print()
    print(f'Enviando mensagem: {mensagem}')
    print()
    socket.emit('sendMessage', mensagem)

if __name__ == '__main__':
    socket.connect('http://localhost:3000')
    while True:
        usr = input('Digite seu nome:')
        msg = input('Digite sua mensagem:')
        mensagem={
            'usuario': usr,
            'mensagem': msg
        }
        sendMessage(mensagem)

        continuar=input('Continuar? ').lower()[0]
        if continuar == 'n':
            socket.disconnect()
            break

    socket.wait()
