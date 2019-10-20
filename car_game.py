cmd = ''
started = False

while True:
    cmd = input('> ').lower()
    if cmd == 'start':
        if started:
            print('Car already started')
        else:
            started = True
            print('Car started ... Ready to go!')
    elif cmd == 'stop':
        if not started:
            print('Car already stopped...')
        else:
            started = False
            print('Car stopped....')
    elif cmd == 'help':
        print("""
 start ---- to start the car
 stop ---- to stop the car
 quit ---- to exit
        """)
    elif cmd == 'quit':
        break
    else:
        print("I don't understand that!")