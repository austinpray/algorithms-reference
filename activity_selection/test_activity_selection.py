import datetime

from activity_selection.activity_selection import Activity, select_activities

a1 = Activity('a1', datetime.datetime(2017, 5, 21, 9), datetime.datetime(2017, 5, 21, 10))
a2 = Activity('a2', datetime.datetime(2017, 5, 21, 11), datetime.datetime(2017, 5, 21, 12))
a3 = Activity('a3', datetime.datetime(2017, 5, 21, 13), datetime.datetime(2017, 5, 21, 14))
a4 = Activity('a4', datetime.datetime(2017, 5, 21, 9), datetime.datetime(2017, 5, 21, 14))
a5 = Activity('a5', datetime.datetime(2017, 5, 21, 9), datetime.datetime(2017, 5, 21, 12))


def test_activity_sort():
    activities = [a3, a2, a1]
    sorted_list = Activity.sort_by_end(activities)
    print(sorted_list)
    assert sorted_list[0].name == 'a1'

def test_select_activities():
    sel = select_activities([a1, a3, a2, a4])
    assert len(sel) == 3
    assert sel[0].name == 'a1'
    assert sel[1].name == 'a2'
    assert sel[2].name == 'a3'
    sel = select_activities([a1, a3, a2, a4, a5])
    assert len(sel) == 3
    assert sel[0].name == 'a1'
    assert sel[1].name == 'a2'
    assert sel[2].name == 'a3'

