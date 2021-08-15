from django import template

from ctevt.date_converter import ad_to_bs

register = template.Library()


@register.simple_tag
def nepali_date(date_in_ad):
    print("Function successful")
    return ad_to_bs.to_bs(date_in_ad)