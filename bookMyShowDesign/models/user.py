from bookMyShowDesign.services.booking import Booking


class User:
    def __init__(self, username):
        self.username = username
        self.bookings = []

    def book_tickets(self, event, number_of_tickets):
        if event.book_seats(number_of_tickets):
            booking = Booking(event, self, number_of_tickets)
            self.bookings.append(booking)
            return "Booked Successfully"
        return "Sorry!! Tickets are not available"

    def show_user_bookings(self):
        for booking in self.bookings:
            if booking:
                print(booking.event.name, booking.tickets)

