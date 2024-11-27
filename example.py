OK_RESULT = 'yes'
FATAL_RESULT = 'no'
pepe = 9


def check_if_aprive_or_not() -> str:

    result = input('¿Eres del madrid?')

    if isinstance(result, str):
        if result.lower() == 'yes':
            return('Aprobado')
        return 'MEGASUSPENDIDO'
    
print(check_if_aprive_or_not())