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

from attribute_item import AttributeItem


class AttributeDateTypeException(Exception):
    def __init__(self, out_attribute_item: AttributeItem, in_attribute_item: AttributeItem) -> None:
        super().__init__()

        self._message: str = (
            f"Mismatching attribute data types "
            f"(data type of attribute <{out_attribute_item.name}> is {out_attribute_item.data_type}, "
            f"data type of attribute <{in_attribute_item.name}> is {in_attribute_item.data_type})"
        )

    @property
    def message(self) -> str:
        return self._message
