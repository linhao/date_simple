'''Advanced Python hw3: produce a module, build into a package and write tests for it'''
import datetime

def get_date_object(date=None):
    """ takes an optional string date and returns a date object """
    if date:
        date_obj = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    else:
        date_obj = datetime.date.today()
    return date_obj

def get_date_string(date_object=None):
    """ takes an optional date object and returns a formatted string """
    if date_object:
        date_str = datetime.datetime.strptime(date_object, '%Y-%m-%d').date()
        date_str = date_str.strftime('%Y-%m-%d')
    else:
        date_str = datetime.date.today().strftime('%Y-%m-%d')
    return date_str

# extra credit version
#def get_date_string(date_object=None, format='MM/DD/YYY'):
    """ takes an optional date object and returns a formatted string """
    main()

if __name__ == '__main__':
    get_date_object()
    get_date_object(date='2018-02-26')
    get_date_string()
    get_date_string(date_object='2018-01-01')