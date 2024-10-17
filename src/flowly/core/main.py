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

from flowly.core.base_entity import BaseEntity
from flowly.core.attribute import Attribute

if __name__ == "__main__":

    base_entity: BaseEntity = BaseEntity()
    deserialized_base_entity: BaseEntity = BaseEntity.from_json(base_entity.to_json())
    print(base_entity.to_dict())
    print(deserialized_base_entity.to_dict())
    print(base_entity == deserialized_base_entity)

    attribute: Attribute = Attribute(name="My attribute", data_type=int)
    deserialized_attribute: Attribute = Attribute.from_json(attribute.to_json())
    print(attribute.to_dict())
    print(deserialized_attribute.to_dict())
    print(attribute == deserialized_attribute)
