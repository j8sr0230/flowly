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

from typing import Optional
from uuid import UUID

from base_item import BaseItem
from attribute_item import AttributeItem


class NodeItem(BaseItem):
    def __init__(self, name: str = "Node Item", uuid: Optional[UUID] = None) -> None:
        super().__init__(name= name, uuid=uuid)

        self._input_attributes: list[AttributeItem] = [
            AttributeItem(name="A"), AttributeItem(name="B")
        ]

        self._output_attributes: list[AttributeItem] = [
            AttributeItem(name="Res")
        ]
