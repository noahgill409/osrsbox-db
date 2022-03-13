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
from typing import List, Dict, Optional

from osrsbox.items_api.modifier import Modifier


@dataclass
class ItemSpecialWeapon:
    """This class defines the properties for an equipable OSRS item that is a special weapon.

    The ItemSpecialWeapon class is the object that retains all the item's properties related
    to equipable items that are special weapons. This includes the name of the special attack,
    the energy used (expressed as an integer percent), the wiki description of the special attack, 
    and optional parameters. These include the damage type rolled by the attacker regardless of 
    active style, the damage type rolled by the defender regardless of active style, a list of attack 
    roll modifiers, and a list of damage roll modifiers. The modifiers are Modifier objects which 
    evaluate as floats and optionally provide information about the use case or source of the value.
    """
    name: str
    energy_used: int
    description: str
    attack_roll_damage_type: Optional[str]
    defence_roll_damage_type: Optional[str]
    special_attack_roll_modifiers: Optional[List[Modifier]]
    special_damage_modifiers: Optional[List[Modifier]]

    def construct_json(self) -> Dict:
        """Construct dictionary/JSON of ItemSpecialWeapon class for exporting or printing.

        :return: All class attributes stored in a dictionary.
        """
        return asdict(self)
