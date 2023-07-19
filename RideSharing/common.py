next_trip_id = 1


class RATING:
    UNASSIGNED = 0
    ONE_STAR = 1
    TWO_STARS = 2
    THREE_STARS = 3
    FOUR_STARS = 4
    FIVE_STARS = 5


class TRIP_STATUS:
    UNASSIGNED = 0
    DRIVER_ON_THE_WAY = 1
    DRIVER_ARRIVED = 2
    STARTED = 3
    PAUSED = 4
    CANCELLED = 5
    ENDED = 6


class Util:
    @staticmethod
    def rating_to_string(p_rating):
        if p_rating == RATING.ONE_STAR:
            return "one star"
        elif p_rating == RATING.TWO_STARS:
            return "two stars"
        elif p_rating == RATING.THREE_STARS:
            return "three stars"
        elif p_rating == RATING.FOUR_STARS:
            return "four stars"
        elif p_rating == RATING.FIVE_STARS:
            return "five stars"
        return "invalid rating"

    @staticmethod
    def is_high_rating(p_rating):
        return p_rating in [RATING.FOUR_STARS, RATING.FIVE_STARS]
