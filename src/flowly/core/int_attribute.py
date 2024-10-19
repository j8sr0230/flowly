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

from flowly.core.enumerations import AttributeFlags
from flowly.core.attribute import Attribute
if TYPE_CHECKING:
    from flowly.core.node import Node
    from flowly.core.edge import Edge


class IntAttribute(Attribute):
    def __init__(
            self,
            uuid: Optional[UUID] = None,
            name: str = "Attribute",
            data: Any = None,
            data_type: type = Any,
            flag: AttributeFlags = AttributeFlags.INPUT,
            parent: Optional[Node] = None,
            is_multi_edge: bool = True,
            edges: Optional[list[Edge]] = None
    ) -> None:
        super().__init__(
            uuid=uuid, name=name, data=data, data_type=data_type, flag=flag, parent=parent, is_multi_edge=is_multi_edge,
            edges=edges
        )
