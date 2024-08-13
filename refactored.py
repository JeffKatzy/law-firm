store = {'client': {}, 'matter': {}, 'time_entry': {}}
# store global so accessible in Matter#total_hours

class PointOneSystem:
    def add_client(self, name, display_number):
        if display_number in store['client']:
            raise Exception(f'client id {display_number} not unique')
        else:
            store['client'][display_number] = Client(name, display_number)

    def add_matter(self, client_number, name, display_number):
        if not self.client_exists(client_number):
            raise Exception('Client with number {display_number} does not exist')
        matter = Matter(client_number, name, display_number)
        if self.id_exists(matter):
            raise Exception(f'Matter id {matter.get_id()} not unique')
        store['matter'][matter.get_id()] = matter

    def add_time_entry(self, client_number, display_number, narrative, hours, date):
        unique_id = f'{client_number}_{display_number}'
        time_entry = TimeEntry(client_number, display_number, narrative, hours, date)
        store['time_entry'].setdefault(unique_id, []).append(time_entry)

    def client_exists(self, display_number):
        return display_number in store['client']

    def id_exists(self, obj):
        return obj.get_id() in store[type(obj).__name__.lower()]

class Client:
    name: str = None
    display_number: str = None

    def get_id(self):
        return self.display_number

class Matter:
    def __init__(self, client_number, name, display_number):
        self.client_number = client_number
        self.name = name
        self.display_number = display_number

    def get_id(self):
        return f'{self.client_number}_{self.display_number}'

    def total_hours(self):
        return sum(entry.hours for entry in store['time_entry'].get(self.get_id(), []))

    def total_hours_for_range(self, start_date, end_date):
        return sum(
            entry.hours for entry in store['time_entry'].get(self.get_id(), [])
            if start_date <= entry.date <= end_date
        )

class TimeEntry:
    def __init__(self, client_number, display_number, narrative, hours, date):
        self.client_number = client_number
        self.display_number = display_number
        self.narrative = narrative
        self.hours = hours
        self.date = date


system = PointOneSystem()
system.add_client("Dropbox Inc.", "C002")
system.add_matter("C002", "Series C Financing", "M0004")
system.add_time_entry("C002", "M0004", "Worked on project", 1.2134, "2024-01-11")
system.add_time_entry("C002", "M0004", "Worked on project", 1, "2024-01-12")

matter = list(store['matter'].values())[0]
total_hours = matter.total_hours_for_range("2024-01-11", "2024-01-13")
print(total_hours)
