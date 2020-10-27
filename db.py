from typing import List, Set
from models.user import User
from models.hotel import Hotel
from models.booking import Booking
from models.room_date import RoomDate

bookings: List[Booking] = []
users: List[User] = []
hotels: List[Hotel] = []
registered_emails: Set[str] = set()
room_dates: List[RoomDate] = []
