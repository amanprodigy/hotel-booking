from typing import List
from datetime import timedelta, date


def getDatesInRange(from_date: date, to_date: date) -> List[date]:
    dates = []
    delta = to_date - from_date
    for i in range(delta.days + 1):
        day = from_date + timedelta(days=i)
        dates.append(day)
    return dates
