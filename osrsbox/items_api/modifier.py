"""
Author:  PH01L
Email:   phoil@osrsbox.com
Website: https://www.osrsbox.com

Copyright (c) 2019, PH01L

- this file -
Author:  bedevere
Email:   noahgill409@gmail.com
Website: https://www.github.com/noahgill409

###############################################################################
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
###############################################################################
"""
from dataclasses import dataclass, asdict
from typing import Optional, Dict, List


@dataclass
class Modifier:
    """This class wraps a float with optional comment to describe the modifier application.
    """
    value: float
    comment: Optional[str]

    def __float__(self) -> float:
        return self.value

    def construct_json(self) -> Dict:
        """Construct dictionary/JSON of Modifier class for exporting or printing.

        :return: All class attributes stored in a dictionary.
        """
        return asdict(self)


def process_modifiers(dictionary: dict, key: str):
    """Transforms and replaces lists of modifiers within a dictionary with a list of Modifier objects.

    If the provided key is not in the dictionary's keys, no action is performed.
    Args:
        dictionary (dict): A dictionary.
        key (str): The key where the list of modifier dictionary objects are stored.
    """
    if dictionary.get(key):
        list_of_modifier_dicts: List[dict] = dictionary.pop(key)
        dictionary[key] = [Modifier(**mod_dict) for mod_dict in list_of_modifier_dicts]
