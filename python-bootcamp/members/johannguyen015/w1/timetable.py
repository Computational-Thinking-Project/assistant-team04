def by_day(timetable ):
    group = {}
    for course, day in timetable:
        group.setdefault(day, []).append(course)
    for courses in group.values():
        courses.sort()
    return group
