#!/usr/bin/env python3

# -*- coding: utf-8 -*-
# ************************************************************************
# * Copyright (c) 2024 Ronny Scharf-W. <ronny.scharf08@gmail.com>        *
# *                                                                      *
# * This program is free software; you can redistribute it and/or modify *
# * it under the terms of the GNU Lesser General Public License (LGPL)   *
# * as published by the Free Software Foundation; either version 2 of    *
# * the License, or (at your option) any later version.                  *
# * for detail see the LICENSE text file.                                *
# *                                                                      *
# * This program is distributed in the hope that it will be useful,      *
# * but WITHOUT ANY WARRANTY; without even the implied warranty of       *
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the         *
# * GNU Library General Public License for more details.                 *
# *                                                                      *
# * You should have received a copy of the GNU Library General Public    *
# * License along with this program; if not, write to the Free Software  *
# * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307  *
# * USA                                                                  *
# *                                                                      *
# ************************************************************************

from __future__ import annotations
from typing import TYPE_CHECKING, Any, Optional
from uuid import UUID
from enum import Enum

from flowly.core.base_item import BaseItem
if TYPE_CHECKING:
    from flowly.core.node_item import NodeItem


class AttributeFlags(Enum):
    OPTION: int = 0
    INPUT: int = 1
    OUTPUT: int = 2


class AttributeItem(BaseItem):
    def __init__(self, name: str = "Attribute Item", uuid: Optional[UUID] = None, data: Any = None,
                 data_type: type = Any, flag: AttributeFlags = AttributeFlags.INPUT,
                 parent: Optional[NodeItem] = None) -> None:
        super().__init__(name= name, uuid=uuid)

        self._data: Any = data
        self._data_type: Any = data_type
        self._flag: AttributeFlags = flag
        self._parent: Optional[NodeItem] = parent

    @property
    def data(self) -> Any:
        return self._data

    @data.setter
    def data(self, value: Any):
        self._data: Any = value

    @property
    def data_type(self) -> type:
        return self._data_type

    @property
    def flag(self) -> AttributeFlags:
        return self._flag

    @property
    def parent(self) -> Optional[NodeItem]:
        return self._parent
