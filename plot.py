import matplotlib as mpl
import matplotlib.dates as mpdates
import matplotlib.pyplot as plot

mpl.rcParams['toolbar'] = 'None'
fig, ax = plot.subplots()
y_value = .5
y_ticks = []
y_labels = []
fig.canvas.set_window_title('WhatsappMonitor')


def add(entry):
    global y_value, y_ticks, y_labels
    x_values = []
    for data in entry.data:
        x_values.append((mpdates.date2num(data[0]), mpdates.date2num(data[1]) - mpdates.date2num(data[0])))
    ax.broken_barh(x_values, (y_value, .5))
    y_ticks.append(y_value + .25)
    y_labels.append(entry.name)
    y_value += 1.5


def show(start_time, finish_time):
    run_time = (finish_time - start_time).seconds
    start_time = mpdates.date2num(start_time)
    finish_time = mpdates.date2num(finish_time)
    ax.set_xlim(start_time, finish_time)
    ax.set_ylim(0, y_value + 1)
    ax.set_yticks(y_ticks)
    ax.set_yticklabels(y_labels)

    plot.title('Monitored online times')

    if set_locator(run_time):
        plot.show()
    else:
        print('The script must run at least 5 min to show a graph.')


def set_locator(run_time):
    if run_time < 300:
        return False
    if run_time < 3600:
        ax.xaxis.set_major_locator(mpdates.MinuteLocator())
        ax.xaxis.set_major_formatter(mpdates.DateFormatter('%H:%M'))
        return True
    if run_time < 18000:
        ax.xaxis.set_major_locator(mpdates.MinuteLocator(byminute=[0, 15, 30, 45]))
        ax.xaxis.set_minor_locator(mpdates.MinuteLocator())
        ax.xaxis.set_major_formatter(mpdates.DateFormatter('%H:%M'))
        return True
    if run_time < 86400:
        ax.xaxis.set_major_locator(mpdates.HourLocator())
        ax.xaxis.set_minor_locator(mpdates.MinuteLocator(byminute=[15, 30, 45]))
        ax.xaxis.set_major_formatter(mpdates.DateFormatter('%H:%M'))
        return True
    ax.xaxis.set_major_locator(mpdates.HourLocator())
    ax.xaxis.set_minor_locator(mpdates.MinuteLocator(byminute=[15, 30, 45]))
    ax.xaxis.set_major_formatter(mpdates.DateFormatter('%d.%b %H:%M'))
