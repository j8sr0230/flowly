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
from flowly.core.int_attribute import IntAttribute
from flowly.core.edge import Edge

if __name__ == "__main__":

    base_entity: BaseEntity = BaseEntity()
    deserialized_base_entity: BaseEntity = BaseEntity.from_json(base_entity.to_json())
    print(base_entity.to_dict())
    print(deserialized_base_entity.to_dict())
    print(base_entity == deserialized_base_entity)
    print()

    attribute: Attribute = Attribute(name="My attribute", data=1, data_type=int)
    deserialized_attribute: Attribute = Attribute.from_json(attribute.to_json())
    print(attribute.to_dict())
    print(deserialized_attribute.to_dict())
    print(attribute == deserialized_attribute)
    print()

    edge: Edge = Edge()
    attribute.connect_edge(edge)
    deserialized_attribute: Attribute = Attribute.from_json(attribute.to_json())
    print(attribute.to_dict())
    print(deserialized_attribute.to_dict())
    print(attribute == deserialized_attribute)
    print()

    int_attribute: IntAttribute = IntAttribute(name="My int attribute", data=5, data_type=int)
    deserialized_int_attribute: Attribute = Attribute.from_json(int_attribute.to_json())
    print(type(deserialized_int_attribute), int_attribute.to_dict())
    print(deserialized_int_attribute.to_dict())
    print(int_attribute == deserialized_int_attribute)
