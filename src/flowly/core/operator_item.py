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

from flowly.core.base_entity import BaseEntity
if TYPE_CHECKING:
    from flowly.core.node import Node


class OperatorItem(BaseEntity):
    def __init__(self, name: str = "Operator Item", uuid: Optional[UUID] = None,
                 parent: Optional[Node] = None) -> None:
        super().__init__(name= name, uuid=uuid)

        self._parent: Optional[Node] = parent

    @property
    def parent(self) -> Optional[Node]:
        return self._parent

    # noinspection PyUnusedLocal
    @staticmethod
    def evaluate(*args: Any, **kwargs: Any) -> Any:
        return 0
