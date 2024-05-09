from django.db import models
from django.utils import timezone


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    def get_duration(self):
        entered_at = self.entered_at
        time_now = timezone.now()
        leaved_at = self.leaved_at if self.leaved_at else time_now
        time_spent = leaved_at - entered_at

        return time_spent

    def format_duration(self, duration=None):
        seconds = duration.seconds % 60
        hours = duration.seconds // 3600
        minutes = (duration.seconds % 3600) // 60

        return f"{hours:02} ч {minutes:02} мин {seconds:02} сек"

    def is_visit_long(self, minutes=60):
        if not self.leaved_at:
            return False

        duration = self.get_duration()
        minutes_spent_inside = duration.total_seconds() / 60
        is_strange = minutes_spent_inside > minutes

        return is_strange
