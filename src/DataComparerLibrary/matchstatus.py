from enum import Enum

class MatchStatus(Enum):
    MISMATCH  = 0           # Definitive different
    MATCH     = 1           # Match has been made
    NON_MATCH = 2           # Until yet no match. Matching process can be continued.
