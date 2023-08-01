import psutil

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent

if plugged:
    print(f"⚡ Charger ON: Battery Power is {percent}%")
else:
    print(f"🍃 Charger OFF: Battery Power is {percent}%")
