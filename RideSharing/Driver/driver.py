class Driver:
    def __init__(self, d_name, d_rating):
        self.name = d_name
        self.rating = d_rating
        self.available = False

    def get_drive_name(self):
        return self.name

    def get_rating(self):
        return self.rating

    def update_avail(self, d_avail):
        self.available = d_avail
