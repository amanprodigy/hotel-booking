from models.room import Room
from datetime import date


class RoomDate:
    room: Room
    booking_date: date

    def __init__(self, room, booking_date):
        self.room = room
        self.booking_date = date

    def __repr__(self):
        return 'Room #{self.room.room_number}, Date: {self.booking_date}'
