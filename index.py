class Client:
  def __init__(self, name, display_number):
    self.name = name
    self.display_number = display_number
    self.validate_unique(display_number)
    store['clients'][display_number] = self

  def validate_unique(self, unique_id):
    if store['clients'].get(unique_id):
      raise 'id not unique'

class Matter:
  def __init__(self, name, display_number, client_display_number):
    self.name = name
    self.display_number = display_number
    self.client_display_number = client_display_number
    unique_id = client_display_number +  '_' + display_number
    self.validate_unique(unique_id)
    store['matters'][unique_id] = self

  def validate_unique(self, unique_id):
    # if exists
    if store['matters'].get(unique_id):
      raise 'id not unique'

  def total_hours(self):
    unique_id = self.client_display_number +  '_' + self.display_number
    entries = store['time_entries'][unique_id]
    return sum([entry.hours for entry in entries])

class TimeEntry:
  def __init__(self, client_display_number, matter_display_number, narrative, hours, date):
    self.narrative = narrative
    self.client_display_number = client_display_number
    self.matter_display_number = matter_display_number
    self.hours = hours
    self.date = date
    unique_id = client_display_number +  '_' + matter_display_number
    if store['time_entries'].get(unique_id):
      store['time_entries'][unique_id].append(self)
    else:
      store['time_entries'][unique_id] = []
      store['time_entries'][unique_id].append(self)