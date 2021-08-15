from .core import ad_to_bs
from .date_format import change_to_slash, change_to_minus

def to_bs(test_data):
    date_in_bs = ad_to_bs(change_to_slash(test_data))
    year = date_in_bs['en']['year']
    month = date_in_bs['en']['month']
    day = date_in_bs['en']['day']
    complete_date = str(year)+'/'+str(month)+'/'+str(day)
    return str(change_to_minus(complete_date))