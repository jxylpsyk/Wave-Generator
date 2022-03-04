import platform

# Platform dependencies
# =====================

SYSTEM_OS = platform.system()
BUTTON_WIDTH = 12 if SYSTEM_OS == 'Windows' else 8

# Audio dependencies
# =====================

SAMPLE_RATE = 44100

FORMAT = 2
CHUNK = 1024 * 4
CHANNELS = 1

# Music dependencies
# =====================

DEFAULT_FREQ = 440

OCTAVE_5_NOTES = {
    'C': 440 * 2**(3 / 12),
    'Csh': 440 * 2**(4 / 12),
    'Db': 440 * 2**(4 / 12),
    'D': 440 * 2**(5 / 12),
    'Dsh': 440 * 2**(6 / 12),
    'Eb': 440 * 2**(6 / 12),
    'E': 440 * 2**(7 / 12),
    'F': 440 * 2**(8 / 12),
    'Fsh': 440 * 2**(9 / 12),
    'Gb': 440 * 2**(9 / 12),
    'G': 440 * 2**(10 / 12),
    'Gsh': 440 * 2**(11 / 12),
    'Ab': 440 * 2**(11 / 12),
    'A': 440 * 2,
    'Ash': 440 * 2**(13 / 12),
    'Bb': 440 * 2**(13 / 12),
    'B': 440 * 2**(14 / 12),
}

# GUI dependencies
# =====================

WINDOW_HEIGHT = 800
WINDOW_WIDTH = 1400

MyNewCuteConstant = 64

from ..utils import messenger
#user_dict = messenger.get_user_settings()
user_dict = {
    "bg-color": "#182839",
    "fg-color": "#123456",
    "line-color": "#ffffff"
}

BG_COLOR = user_dict["bg-color"]
FG_COLOR = user_dict["fg-color"]
LINE_COLOR = user_dict["line-color"]

PINKISH_RED = '#ff8cad'
MELLOW_YELLOW = '#ffff8c'
PRETTY_PURPLE = '#c800ff'
BRATTY_BLUE = '#2600ff'
PLAIN_BLANC = '#ffffff'