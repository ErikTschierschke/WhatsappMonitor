from datetime import datetime as dt

import plot

online_data = list()


def generate_plot(start_time):
    for entry in online_data:
        plot.add(entry)
    plot.show(start_time, dt.now())


def get(name):
    for entry in online_data:
        if entry.name == name:
            return entry

    entry = Entry(name)
    online_data.append(entry)
    return entry


def finish(start_time):
    for entry in online_data:
        entry.set_offline()
    generate_plot(start_time)


class Entry:

    def __init__(self, name):
        self.name = name
        self.online = False
        self.start_dt = None
        self.data = list()

    def set_online(self):
        if not self.online:
            self.online = True
            self.start_dt = dt.now()

    def set_offline(self):
        if self.start_dt is not None:
            self.online = False
            self.data.append((self.start_dt, dt.now()))
