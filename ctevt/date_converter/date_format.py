from datetime import datetime

def change_to_minus(test_date):
    date_in_string = str(test_date)
    date_with_arguments = date_in_string.split('/')
    year = date_with_arguments[0]
    if len(date_with_arguments[1]) == 1:
        month = "0" + date_with_arguments[1]
    else:
        month = date_with_arguments[1]
    if len(date_with_arguments[2]) == 1:
        day = "0" + date_with_arguments[2]
    else:
        day = date_with_arguments[2]
    complete_date = year + "-" + month + "-" + day
    return datetime.strptime(complete_date, "%Y-%m-%d").date()

def change_to_slash(test_date):
    date_in_string = str(test_date)
    date_with_arguments = date_in_string.split('-')
    year = date_with_arguments[0]
    if len(date_with_arguments[1]) == 1:
        month = "0" + date_with_arguments[1]
    else:
        month = date_with_arguments[1]
    if len(date_with_arguments[2]) == 1:
        day = "0" + date_with_arguments[2]
    else:
        day = date_with_arguments[2]
    return year + "/" + month + "/" + day