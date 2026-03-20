from datetime import datetime

def validate_end_date(start_date, end_date):
    start = datetime.strptime(start_date, "%d-%m-%Y")
    end = datetime.strptime(end_date, "%d-%m-%Y")
    return end > start

def validate_date(date):

    if len(date) != 10 or date[2] != '-' or date[5] != '-':
        return False

    try:
        day = int(date[0:2])
        month = int(date[3:5])
        year = int(date[6:10])
    except ValueError:
        return False

    if 0 < day < 32 and 0 < month < 13 and 2026 <= year <= 2030:
        return True
    else:
        return False