import keyboard as kb

konami_code = ['flecha arriba', 'flecha arriba', 
               'flecha abajo', 'flecha abajo', 
               'flecha izquierda', 'flecha derecha',
               'flecha izquierda', 'flecha derecha', 
               'b', 'a']

konami_input = list()

def pressed_key(key):
    konami_input.append(key.name)
    
    if key.name == 'q':
        konami_input.pop()
        print(konami_input)
        
        if (konami_code == konami_input):
            print('KONAMI CODE')
        else:
            print("KONAMIN'T CODE")


kb.on_press(pressed_key)

kb.wait()
