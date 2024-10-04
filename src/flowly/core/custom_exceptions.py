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
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from node_item import NodeItem
    from attribute_item import AttributeItem


class AttributeIndexException(Exception):
    def __init__(self, node_item: NodeItem, attribute_id: int, is_input: bool) -> None:
        super().__init__()

        self._message: str = "Input " if is_input else "Output "
        self._message += f"attribute item '{node_item.name}.[{attribute_id}]' is not existing."


    @property
    def message(self) -> str:
        return self._message


class AttributeDateTypeException(Exception):
    def __init__(self, out_attribute_item: AttributeItem, in_attribute_item: AttributeItem) -> None:
        super().__init__()

        self._message: str = (
            f"Mismatching attribute data types "
            f"(data type of attribute item '{out_attribute_item.parent.name}.{out_attribute_item.name}' is "
            f"{out_attribute_item.data_type}, "
            f"data type of attribute item '{in_attribute_item.parent.name}.{in_attribute_item.name}' is "
            f"{in_attribute_item.data_type})."
        )

    @property
    def message(self) -> str:
        return self._message
