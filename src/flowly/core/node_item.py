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

from typing import Any, Optional
from uuid import UUID

from base_item import BaseItem
from attribute_item import AttributeItem


class NodeItem(BaseItem):
    def __init__(self, name: str = "Node Item", uuid: Optional[UUID] = None) -> None:
        super().__init__(name= name, uuid=uuid)

        self._input_attributes: list[AttributeItem] = []
        self._output_attributes: list[AttributeItem] = []

        self.add_attribute_item(AttributeItem(name="A", data_type=int, is_input=True))
        self.add_attribute_item(AttributeItem(name="B", data_type=int, is_input=True))
        self.add_attribute_item(AttributeItem(name="Res", data_type=Any, is_input=False))

    @property
    def input_attributes(self) -> list[AttributeItem]:
        return self._input_attributes

    @property
    def output_attributes(self) -> list[AttributeItem]:
        return self._output_attributes

    @property
    def attributes(self) -> list[AttributeItem]:
        return self._input_attributes + self._output_attributes

    def add_attribute_item(self, attribute_item: AttributeItem):
        attribute_item.name = self.name + ":" + attribute_item.name
        attribute_item.parent = self

        if attribute_item.is_input:
            self._input_attributes.append(attribute_item)
        else:
            self._output_attributes.append(attribute_item)
