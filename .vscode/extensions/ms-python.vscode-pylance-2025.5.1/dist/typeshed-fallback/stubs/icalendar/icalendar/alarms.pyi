import datetime
from typing_extensions import TypeAlias

from .cal import Alarm, Event, Todo

__all__ = [
    "Alarms",
    "AlarmTime",
    "IncompleteAlarmInformation",
    "ComponentEndMissing",
    "ComponentStartMissing",
    "LocalTimezoneMissing",
]

Parent: TypeAlias = Event | Todo

class IncompleteAlarmInformation(ValueError): ...
class ComponentStartMissing(IncompleteAlarmInformation): ...
class ComponentEndMissing(IncompleteAlarmInformation): ...
class LocalTimezoneMissing(IncompleteAlarmInformation): ...

class AlarmTime:
    def __init__(
        self,
        alarm: Alarm,
        trigger: datetime.datetime,
        acknowledged_until: datetime.datetime | None = None,
        snoozed_until: datetime.datetime | None = None,
        parent: Parent | None = None,
    ): ...
    @property
    def acknowledged(self) -> datetime.datetime | None: ...
    @property
    def alarm(self) -> Alarm: ...
    @property
    def parent(self) -> Parent | None: ...
    def is_active(self) -> bool: ...
    @property
    def trigger(self) -> datetime.date: ...

class Alarms:
    def __init__(self, component: Alarm | Event | Todo | None = None): ...
    def add_component(self, component: Alarm | Parent) -> None: ...
    def set_parent(self, parent: Parent) -> None: ...
    def add_alarm(self, alarm: Alarm) -> None: ...
    def set_start(self, dt: datetime.date | None) -> None: ...
    def set_end(self, dt: datetime.date | None) -> None: ...
    def acknowledge_until(self, dt: datetime.date | None) -> None: ...
    def snooze_until(self, dt: datetime.date | None) -> None: ...
    def set_local_timezone(self, tzinfo: datetime.tzinfo | str | None) -> None: ...
    @property
    def times(self) -> list[AlarmTime]: ...
    @property
    def active(self) -> list[AlarmTime]: ...
