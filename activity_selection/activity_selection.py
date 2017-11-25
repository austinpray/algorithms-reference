class Activity:
    def __init__(self, name, start, end):
        self.name = name
        self.start = start
        self.end = end

    @staticmethod
    def sort_by_end(activities):
        activities.sort(key=lambda a: int(a.end.timestamp()))
        return activities


def select_activities(activities):
    activities = Activity.sort_by_end(activities)
    out = []
    for activity in activities:
        if len(out) < 1:
            out.append(activity)
            continue

        current = out[len(out) - 1]
        if activity.start.timestamp() >= current.end.timestamp():
            out.append(activity)

    return out
