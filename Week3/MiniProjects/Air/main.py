from datetime import datetime, date

class Airline:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.planes = []

class Airplane:
    def __init__(self, id, current_location, company):
        self.id = id
        self.current_location = current_location
        self.company = company
        self.next_flights = []

    def fly(self, destination):
        for flight in self.next_flights:
            if flight.destination == destination:
                flight.take_off()
                self.current_location = destination
                flight.land()
                break

    def location_on_date(self, date):
        for flight in self.next_flights:
            if date == flight.date:
                return flight.origin if flight.origin != self.current_location else flight.destination
        return self.current_location

    def available_on_date(self, date, location):
        for flight in self.next_flights:
            if date == flight.date or self.current_location == location:
                return False
        return True

class Flight:
    def __init__(self, date, destination, origin, plane):
        self.date = date
        self.destination = destination
        self.origin = origin
        self.plane = plane
        self.id = f"{self.destination.city}{self.plane.company.id}{self.date.strftime('%Y%m%d')}"

    def take_off(self):
        print(f"Plane {self.plane.id} taking off from {self.origin.city} to {self.destination.city}")

    def land(self):
        print(f"Plane {self.plane.id} landing at {self.destination.city}")

class Airport:
    def __init__(self, city):
        self.city = city
        self.planes = []
        self.scheduled_departures = []
        self.scheduled_arrivals = []

    def schedule_flight(self, destination, datetime):
        for plane in self.planes:
            if plane.available_on_date(datetime.date(), self):
                flight = Flight(datetime.date(), destination, self, plane)
                self.scheduled_departures.append(flight)
                destination.scheduled_arrivals.append(flight)
                plane.next_flights.append(flight)
                break

    def info(self, start_date, end_date):
        for flight in self.scheduled_departures:
            if start_date <= flight.date <= end_date:
                print(f"Flight {flight.id}: Departure: {flight.date} from {flight.origin.city} to {flight.destination.city}")

        for flight in self.scheduled_arrivals:
            if start_date <= flight.date <= end_date:
                print(f"Flight {flight.id}: Arrival: {flight.date} from {flight.origin.city} to {flight.destination.city}")

# Test Code
airline1 = Airline("AA", "American Airlines")
airline2 = Airline("DL", "Delta Airlines")

airport1 = Airport("JFK")
airport2 = Airport("LAX")

plane1 = Airplane(1, airport1, airline1)
plane2 = Airplane(2, airport1, airline2)
plane3 = Airplane(3, airport2, airline1)

airport1.planes.extend([plane1, plane2])
airport2.planes.append(plane3)

datetime1 = datetime.strptime("2022-08-01", "%Y-%m-%d")
datetime2 = datetime.strptime("2022-08-02", "%Y-%m-%d")
datetime3 = datetime.strptime("2022-08-03", "%Y-%m-%d")

airport1.schedule_flight(airport2, datetime1)
airport1.schedule_flight(airport2, datetime2)
airport2.schedule_flight(airport1, datetime3)

start_date = date(2022, 8, 1)
end_date = date(2022, 8, 3)
airport1.info(start_date, end_date)