import web
import terminal

if __name__ == '__main__':
    opcao=input('Opção [j/c]: ').lower()[0]

    if opcao == 'c':
        terminal.socket.connect('http://localhost:3000')
        while True:
            usr = input('Digite seu nome:')
            msg = input('Digite sua mensagem:')
            mensagem = {
                'usuario': usr,
                'mensagem': msg
            }
            terminal.sendMessage(mensagem)

            continuar = input('Continuar [s/n]: ').lower()[0]
            if continuar == 'n':
                terminal.socket.disconnect()
                break
        terminal.socket.wait()

    if opcao == 'j':
        web.socket.run(web.app, debug=True)