from couch.activity import Walk, Jog


class WorkoutGenerator:
    def __init__(self, week, workout):
        self._week = week
        self._workout = workout

    @property
    def week(self):
        return self._week

    @property
    def workout(self):
        return self._workout

    def get_workout(self):
        if self._week == 1:
            return self._week_one_workout()
        elif self._week == 2:
            return self._week_two_workout()
        elif self._week == 3:
            return self._week_three_workout()
        elif self._week == 4:
            return self._week_four_workout()
        elif self._week == 5:
            return self._week_five_workout()
        elif self._week == 6:
            return self._week_six_workout()
        elif self._week == 7:
            return self._week_seven_workout()
        elif self._week == 8:
            return self._week_eight_workout()
        elif self._week == 9:
            return self._week_nine_workout()

    def _week_one_workout(self):
        workout = Walk(300)
        workout.add_to_tail(Jog(60, Walk(90)))
        workout.add_to_tail(Jog(60, Walk(90)))
        workout.add_to_tail(Jog(60, Walk(90)))
        workout.add_to_tail(Jog(60, Walk(90)))
        workout.add_to_tail(Jog(60, Walk(90)))
        workout.add_to_tail(Jog(60, Walk(90)))
        workout.add_to_tail(Jog(60, Walk(90)))
        workout.add_to_tail(Jog(60, Walk(90)))
        return workout

    def _week_two_workout(self):
        workout = Walk(300)
        workout.add_to_tail(Jog(90, Walk(120)))
        workout.add_to_tail(Jog(90, Walk(120)))
        workout.add_to_tail(Jog(90, Walk(120)))
        workout.add_to_tail(Jog(90, Walk(120)))
        workout.add_to_tail(Jog(90, Walk(120)))
        workout.add_to_tail(Jog(90, Walk(60)))
        return workout

    def _week_three_workout(self):
        workout = Walk(300)
        workout.add_to_tail(Jog(90, Walk(90, Jog(180, Walk(180)))))
        workout.add_to_tail(Jog(90, Walk(90, Jog(180, Walk(180)))))
        return workout

    def _week_four_workout(self):
        workout = Walk(300)
        workout.add_to_tail(Jog(180, Walk(90, Jog(300, Walk(150, Jog(180))))))
        workout.add_to_tail(Walk(90, Jog(300)))
        return workout

    def _week_five_workout(self):
        workout = Walk(300)
        if self._workout == 1:
            workout.add_to_tail(Jog(300, Walk(180, Jog(300, Walk(300, Jog(300))))))
        elif self._workout == 2:
            workout.add_to_tail(Jog(480, Walk(300, Jog(480))))
        else:
            workout.add_to_tail(Jog(1200))
        return workout

    def _week_six_workout(self):
        workout = Walk(300)
        if self._workout == 1:
            workout.add_to_tail(Jog(300, Walk(180, Jog(480, Walk(180, Jog(300))))))
        elif self._workout == 2:
            workout.add_to_tail(Jog(600, Walk(180, Jog(600))))
        else:
            workout.add_to_tail(Jog(1320))
        return workout

    def _week_seven_workout(self):
        workout = Walk(300)
        workout.add_to_tail(Jog(25 * 60))
        return workout

    def _week_eight_workout(self):
        workout = Walk(300)
        workout.add_to_tail(Jog(28 * 60))
        return workout

    def _week_nine_workout(self):
        workout = Walk(300)
        workout.add_to_tail(Jog(30 * 60))
        return workout
