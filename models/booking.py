from typing import List
from uuid import uuid4, UUID
from datetime import datetime, date

from models.room import Room
from models.user import User
from models.hotel import Hotel


class Roomstr:
    room: Room
    booking_date: str

    def __init__(self, room: Room, booking_date: str):
        self.room = room
        self.booking_date = booking_date


class Booking:
    '''
    Booking class representing a booking in the system
    '''
    booking_id: UUID
    user: User
    hotel: Hotel
    rooms: List[Room]
    from_date: date
    to_date: date
    created_at: datetime

    def __init__(self, user, hotel, rooms: List[Room], from_date: date,
                 to_date: date):
        self.user = user
        self.hotel = hotel
        self.rooms = rooms
        self.booked_rooms = rooms
        self.booking_id = uuid4()
        self.from_date = from_date
        self.to_date = to_date

    def __str__(self):
        rooms = ', '.join(x.room_number for x in self.rooms)
        print(self.rooms)
        print(rooms)
        return "Booking Id: %s, user: %s, Hotel: %s, rooms: %s, from_date: %s, to_date: %s" % (
            self.booking_id, self.user, self.hotel, rooms, self.from_date,
            self.to_date)
