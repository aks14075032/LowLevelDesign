from bookMyShowDesign.models.user import User
from bookMyShowDesign.models.event import Event
from bookMyShowDesign.models.venue import *
from bookMyShowDesign.services.eventFactory import *

user1 = User('ak')
user2 = User('vk')

theater = Theatre(1, 'INOX', 'Mumbai')
concert = ConcertHall(2, 'LAK', 'Bengaluru')

event1 = EventFactory.create_event('Movie', 1, 'Bahubali', theater, '12PM-3PM', 20)
event2 = EventFactory.create_event('Concert', 2, 'Arjit', concert, '6PM-9PM', 10)

print(user1.book_tickets(event1, 5))
print(user2.book_tickets(event2, 10))

print(user1.book_tickets(event1, 20))
print(user2.book_tickets(event2, 11))

print(user1.show_user_bookings())
print(user2.show_user_bookings())
