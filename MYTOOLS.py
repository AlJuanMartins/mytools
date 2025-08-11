PI_INT = '1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'
E_INT = '7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274'

def pi_real():
    x = int(input('Digite um número inteiro entre 0 e 100 '))
    
    if x == 0:
        print('3')
    else:
        print(f'3,{PI_INT[:x]}')
        return None

def e_real():
    x = int(input('Digite um número inteiro entre 0 e 100 '))

    if x == 0:
        print('2')
    else:
        print(f'2,{E_INT[:x]}')
        return None





