#!/usr/bin/env python3

# -*- coding: utf-8 -*-
# ***************************************************************************
# *   Copyright (c) 2024 Ronny Scharf-W. <ronny.scharf08@gmail.com>         *
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU Lesser General Public License (LGPL)    *
# *   as published by the Free Software Foundation; either version 2 of     *
# *   the License, or (at your option) any later version.                   *
# *   for detail see the LICENCE text file.                                 *
# *                                                                         *
# *   This program is distributed in the hope that it will be useful,       *
# *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
# *   GNU Library General Public License for more details.                  *
# *                                                                         *
# *   You should have received a copy of the GNU Library General Public     *
# *   License along with this program; if not, write to the Free Software   *
# *   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
# *   USA                                                                   *
# *                                                                         *
# ***************************************************************************

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
from uuid import UUID

from base_item import BaseItem
if TYPE_CHECKING:
    from node_item import NodeItem


class AttributeItem(BaseItem):
    def __init__(self, name: str = "Attribute Item", is_input: bool = True, parent: Optional[NodeItem] = None,
                 uuid: Optional[UUID] = None) -> None:
        super().__init__(name= name, uuid=uuid)

        self._is_input: bool = is_input
        self._parent: Optional[NodeItem] = parent

    @property
    def is_input(self) -> bool:
        return self._is_input

    @is_input.setter
    def is_input(self, value: bool) -> None:
        self._is_input: bool = value

    @property
    def parent(self) -> Optional[NodeItem]:
        return self._parent

    @parent.setter
    def parent(self, value: Optional[NodeItem]) -> None:
        self._parent: Optional[NodeItem] = value
