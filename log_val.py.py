
def log_value(name,*args,**kwargs):
    ''' Log will keep all values on note name:str ,args, kwargs'''
    import logging 
    import os
    if os.getcwd()+'/'+'log_test_code' not in os.listdir():
         logging.basicConfig(filename='log_code.log',level=logging.NOTSET,format='%(asctime)s %(name)s %(levelname)s %(message)s')
         code_handler=logging.StreamHandler()
         code_handler.setLevel(level=logging.NOTSET)
         code_handler.setFormatter('%(asctime)s %(name)s %(levelname)s %(message)s')
         logging.getLogger('').addHandler(code_handler)

    logging.getLogger(f'{name}').info(f'{args} {kwargs}')

    if 'shutdown' in args:
        logging.shutdown()

    return 'log registered successfully'