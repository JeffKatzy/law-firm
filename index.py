store = {'client': {}, 'matter': {}, 'time_entry': {}}
# store global so accessible in Matter#total_hours

class PointOneSystem:
    pass

system = PointOneSystem()
system.add_client("Dropbox Inc.", "C002")
system.add_matter("C002", "Series C Financing", "M0004")
system.add_time_entry("C002", "M0004", "Worked on project", 1.2134, "2024-01-11")
system.add_time_entry("C002", "M0004", "Worked on project", 1, "2024-01-12")

matter = list(store['matter'].values())[0]
total_hours = matter.total_hours_for_range("2024-01-11", "2024-01-13")
print(total_hours)