from datetime import datetime


def logger1(old_function):

    def new_function(*args, **kwargs):
        date = datetime.now()
        name = old_function.__name__
        arguments = f' {args}_{kwargs}'
        res = old_function(*args, **kwargs)
        result = old_function(*args, **kwargs)
        with open('main.log', 'a', encoding='utf-8') as log_file:
            log_file.write(f'Datetime: {str(date)} --- Function: {name} --- '
                           f'Arguments: {arguments} --- Result: {res}\n')

        return result

    return new_function


def logger2(path):

    file_name = path

    def __logger(old_function):

        def new_function(*args, **kwargs):
            date = datetime.now()
            name = old_function.__name__
            arguments = f' {args}_{kwargs}'
            res = old_function(*args, **kwargs)
            result = old_function(*args, **kwargs)
            with open(file_name, 'a', encoding='utf-8') as log_file:
                log_file.write(f'Datetime: {str(date)} --- Function: {name} --- '
                               f'Arguments: {arguments} --- Result: {res}\n')
            return result

        return new_function

    return __logger
