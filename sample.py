
store = {'client': {}, 'matter': {}, 'time_entry': {}}
# store global so accessible in Matter#total_hours
class PointOneSystem:
    def add_client(self, name, display_number):
        if display_number in store['client']:
            raise ValueError(f'client id {display_number} not unique')
        else:
            store['client'][display_number] = Client(name, display_number)

    def add_matter(self, client_number, name, display_number):
        matter = Matter(client_number, name, display_number)
        if self.id_exists(matter):
            raise ValueError('id not unique')
        elif not self.client_from(client_number):
             raise ValueError('client does not exist')
        else:
            matter_id = matter.get_id()
            store['matter'][matter_id] = matter
    
    def add_time_entry(self, client_number, display_number, narrative, hours, date):
        time_entry = TimeEntry(client_number, display_number, narrative, hours, date)
        unique_id = f'{client_number}_{display_number}'
        store['time_entry'].setdefault(unique_id, []).append(time_entry)

    def client_from(self, display_number):
        return store['client'].get(display_number)
    
    def id_exists(self, obj):
      obj_id = obj.get_id()
      obj_name = type(obj).__name__.lower()
      return bool(store[obj_name].get(obj_id))

class Client:
    def __init__(self, name, display_number):
        self.name = name
        self.display_number = display_number
        
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
        return sum(time_entry.hours for time_entry in self.time_entries())

    def total_hours_for_range(self, start_date, end_date):
        return sum(time_entry.hours 
            for time_entry in self.time_entries() if end_date >= time_entry.date >= start_date)

    def time_entries(self):
        unique_id = self.get_id()
        return store['time_entry'].get(unique_id, [])

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

# system.add_matter("C001", "Series C Financing", "M0004")
system.add_time_entry("C002", "M0004", 
"Worked on project", 1.2134, "2024-01-11")
system.add_time_entry("C002", "M0004", 
"Worked on project", 1, "2024-01-12")


matter = list(store['matter'].values())[0]
matter.total_hours_for_range("2024-01-11", "2024-01-13")

# validate
    # client exists