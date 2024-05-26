import time


def track(activity):
    start = time.time()
    input(f"Press Enter to stop tracking '{activity}'...")
    end = time.time()
    duration = end - start
    tracked = {activity: duration}
    return tracked
