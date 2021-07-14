import web
import terminal
import sdthread

if __name__ == '__main__':
    opcao=input('Opção [j/c/t]: ').lower()[0]

    if opcao == 'j':
        web.socket.run(web.app, debug=True)
    if opcao == 't':
        sdthread.app.mainloop()
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

    else:
        print('Terminado!')
