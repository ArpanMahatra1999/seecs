from .core import bs_to_ad
from .date_format import change_to_slash, change_to_minus

def to_ad(test_data):
    date_in_ad = bs_to_ad(change_to_slash(test_data))
    year = date_in_ad['year']
    month = date_in_ad['month']
    day = date_in_ad['day']
    complete_date = str(year)+'/'+str(month)+'/'+str(day)
    return change_to_minus(complete_date)