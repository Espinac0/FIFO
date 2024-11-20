OK_RESULT = 'yes'
FATAL_RESULT = 'no'



def check_if_aprive_or_not() -> str:

    result = input('¿Eres del madrid?')

    if isinstance(result, str):
        if result.lower() == 'yes':
            return('Aprobado')
        return 'SUSPENDIDO'
    
print(check_if_aprive_or_not())