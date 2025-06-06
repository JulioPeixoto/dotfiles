import datetime
from datetime import timezone
from typing import Any, Callable, Literal

import numpy as np

from .artist import Artist, allow_rasterization
from .axes import Axes
from .backend_bases import MouseEvent, RendererBase
from .backends.backend_mixed import MixedModeRenderer
from .cbook import CallbackRegistry
from .lines import Line2D
from .patches import Patch
from .text import Text
from .ticker import Formatter, Locator
from .transforms import Bbox, Transform

GRIDLINE_INTERPOLATION_STEPS: int = ...

class Tick(Artist):
    tick1line: Line2D
    tick2line: Line2D
    gridline: Line2D
    label1: Text
    label2: Text

    def __init__(
        self,
        axes,
        loc,
        *,
        size=None,
        width=None,
        color=None,
        tickdir=None,
        pad=None,
        labelsize=None,
        labelcolor=None,
        zorder=None,
        gridOn=None,
        tick1On=True,
        tick2On=True,
        label1On=True,
        label2On=False,
        major=True,
        labelrotation=0,
        grid_color=None,
        grid_linestyle=None,
        grid_linewidth=None,
        grid_alpha=None,
        **kwargs,
    ) -> None: ...
    @property
    def label(self) -> Text: ...
    def apply_tickdir(self, tickdir) -> None: ...
    def get_tickdir(self): ...
    def get_tick_padding(self) -> float: ...
    def get_children(self) -> list[Line2D | Text]: ...
    def set_clip_path(self, clippath: Patch, transform: Transform | None = None) -> None: ...
    def get_pad_pixels(self) -> float: ...
    def contains(self, mouseevent) -> bool: ...
    def set_pad(self, val: float) -> None: ...
    def get_pad(self) -> float: ...
    def get_loc(self) -> int: ...
    @allow_rasterization
    def draw(self, renderer) -> None: ...
    def set_label1(self, s: str) -> None: ...
    set_label = set_label1
    def set_label2(self, s: str) -> None: ...
    def set_url(self, url: str) -> None: ...
    def get_view_interval(self) -> tuple: ...
    def update_position(self, loc) -> None: ...

class XTick(Tick):
    def __init__(self, *args, **kwargs) -> None: ...
    def update_position(self, loc: int) -> None: ...
    def get_view_interval(self) -> tuple: ...

class YTick(Tick):
    def __init__(self, *args, **kwargs) -> None: ...
    def update_position(self, loc: int) -> None: ...
    def get_view_interval(self) -> tuple: ...

class Ticker:
    def __init__(self) -> None: ...
    @property
    def locator(self) -> Locator: ...
    @locator.setter
    def locator(self, locator: Locator): ...
    @property
    def formatter(self) -> Formatter: ...
    @formatter.setter
    def formatter(self, formatter: Formatter): ...

class _LazyTickList:
    def __init__(self, major: bool) -> None: ...
    def __get__(self, instance: XAxis | YAxis, cls: type[XAxis | YAxis]) -> list[XTick | YTick]: ...

class Axis(Artist):
    isDefault_label: bool
    axes: Axes
    major: Ticker
    minor: Ticker
    callbacks: CallbackRegistry
    label: Text
    labelpad: float = 4
    offsetText: Text
    pickradius: float

    OFFSETTEXTPAD: int = ...

    def __init__(self, axes: Axes, pickradius: float = ...) -> None: ...
    @property
    def isDefault_majloc(self) -> bool: ...
    @isDefault_majloc.setter
    def isDefault_majloc(self, value): ...
    @property
    def isDefault_majfmt(self) -> bool: ...
    @isDefault_majfmt.setter
    def isDefault_majfmt(self, value): ...
    @property
    def isDefault_minloc(self) -> bool: ...
    @isDefault_minloc.setter
    def isDefault_minloc(self, value): ...
    @property
    def isDefault_minfmt(self) -> bool: ...
    @isDefault_minfmt.setter
    def isDefault_minfmt(self, value): ...

    majorTicks: _LazyTickList = ...
    minorTicks: _LazyTickList = ...
    def get_remove_overlapping_locs(self) -> bool: ...
    def set_remove_overlapping_locs(self, val) -> None: ...

    remove_overlapping_locs: property = ...
    def set_label_coords(self, x: float, y: float, transform: None = ...) -> None: ...
    def get_transform(self) -> Transform: ...
    def get_scale(self) -> str: ...
    def limit_range_for_scale(self, vmin: float, vmax: float) -> tuple[float, float]: ...
    def get_children(self) -> list[Text]: ...
    def clear(self) -> None: ...
    def reset_ticks(self) -> None: ...
    def set_tick_params(self, which: str = "major", reset: bool = False, **kwargs) -> None: ...
    def set_clip_path(self, clippath: Patch, transform: Transform | None = ...) -> None: ...
    def get_view_interval(self) -> tuple: ...
    def set_view_interval(self, vmin, vmax, ignore: bool = ...) -> None: ...
    def get_data_interval(self) -> tuple: ...
    def set_data_interval(self, vmin, vmax, ignore: bool = ...) -> None: ...
    def get_inverted(self) -> bool: ...
    def set_inverted(self, inverted: bool) -> None: ...
    def set_default_intervals(self) -> None: ...
    def get_ticklabel_extents(self, renderer: RendererBase) -> tuple[Bbox, Bbox]: ...
    def get_tightbbox(self, renderer: MixedModeRenderer = ..., *, for_layout_only=...) -> Bbox: ...
    def get_tick_padding(self) -> int: ...
    @allow_rasterization
    def draw(self, renderer, *args, **kwargs) -> None: ...
    def get_gridlines(self) -> list[Line2D]: ...
    def get_label(self) -> Text: ...
    def get_offset_text(self) -> Text: ...
    def get_pickradius(self) -> int: ...
    def get_majorticklabels(self) -> list[Text]: ...
    def get_minorticklabels(self) -> list[Text]: ...
    def get_ticklabels(self, minor: bool = ..., which: None | Literal["minor", "major", "both"] = ...) -> list[Text]: ...
    def get_majorticklines(self) -> list[Line2D]: ...
    def get_minorticklines(self) -> list[Line2D]: ...
    def get_ticklines(self, minor=...) -> list[Line2D]: ...
    def get_majorticklocs(self) -> list: ...
    def get_minorticklocs(self) -> list: ...
    def get_ticklocs(self, *, minor=...) -> list: ...
    def get_ticks_direction(self, minor: bool = False) -> np.ndarray: ...
    def get_label_text(self) -> str: ...
    def get_major_locator(self) -> Locator: ...
    def get_minor_locator(
        self,
    ) -> Locator: ...
    def get_major_formatter(
        self,
    ) -> Formatter: ...
    def get_minor_formatter(self) -> Formatter: ...
    def get_major_ticks(self, numticks: None | int = ...) -> list[XTick | YTick]: ...
    def get_minor_ticks(self, numticks: None | int = ...) -> list[XTick | YTick]: ...
    def grid(self, visible: bool | None = None, which: str = "major", **kwargs) -> None: ...
    def update_units(self, data: Any) -> bool: ...
    def have_units(self) -> bool: ...
    def convert_units(self, x): ...
    def set_units(self, u) -> None: ...
    def get_units(self): ...
    def set_label_text(self, label: str, fontdict: dict = ..., **kwargs): ...
    def set_major_formatter(self, formatter: Formatter | str | Callable) -> None: ...
    def set_minor_formatter(self, formatter: Formatter | str | Callable) -> None: ...
    def set_major_locator(self, locator: Locator) -> None: ...
    def set_minor_locator(self, locator: Locator) -> None: ...
    def set_pickradius(self, pickradius: float) -> None: ...
    def set_ticklabels(self, ticklabels: list[str | Text], *, minor: bool = ..., **kwargs) -> list[Text]: ...
    def set_ticks(
        self, ticks: list[float], labels: None | list[str] = ..., *, minor: bool = ..., **kwargs
    ) -> list[XTick | YTick]: ...
    def axis_date(self, tz: str | datetime.tzinfo = ...) -> None: ...
    def get_tick_space(self) -> int: ...
    def get_label_position(self) -> str: ...
    def set_label_position(self, position: Literal["top", "bottom"]) -> None: ...
    def get_minpos(self): ...

class XAxis(Axis):
    axis_name: str = ...
    _tick_class = XTick
    def __init__(self, *args, **kwargs) -> None: ...
    def contains(self, mouseevent) -> bool: ...
    def set_label_position(self, position: Literal["top", "bottom"]) -> None: ...
    def get_text_heights(self, renderer) -> tuple[float, float]: ...
    def set_ticks_position(self, position: Literal["top", "bottom", "both", "default", "none"]) -> None: ...
    def tick_top(self) -> None: ...
    def tick_bottom(self) -> None: ...
    def get_ticks_position(self) -> str: ...
    def get_minpos(self) -> float: ...
    def set_default_intervals(self) -> None: ...
    def get_tick_space(self) -> int: ...

class YAxis(Axis):
    axis_name = ...
    _tick_class = YTick
    def __init__(self, *args, **kwargs) -> None: ...
    def contains(self, mouseevent: MouseEvent) -> bool: ...
    def set_label_position(self, position: Literal["left", "right"]) -> None: ...
    def set_offset_position(self, position: Literal["left", "right"]) -> None: ...
    def get_text_widths(self, renderer): ...
    def set_ticks_position(self, position: Literal["left", "right", "both", "default", "none"]) -> None: ...
    def tick_right(self) -> None: ...
    def tick_left(self) -> None: ...
    def get_ticks_position(self) -> str: ...
    def get_minpos(self) -> float: ...
    def set_default_intervals(self) -> None: ...
    def get_tick_space(self) -> int: ...
