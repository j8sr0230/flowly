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

from uuid import UUID
from uuid import uuid1
import logging


class Attribute:
    def __init__(self, name: str, uuid: str = "") -> None:
        self._name: str = name

        if not uuid:
            self._uuid: UUID = uuid1()
        else:
            try:
                self._uuid: UUID = UUID(uuid)
            except ValueError as e:
                logging.error(f"Invalid UUID provided: {e}")
                self._uuid: UUID = uuid1()

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name: str = value

    @property
    def uuid(self) -> UUID:
        return self._uuid

    def __str__(self) -> str:
        return f"{type(self).__name__}(name={self._name}, uuid={self._uuid})"

    def __repr__(self) -> str:
        return f"<{type(self).__module__}.{type(self).__name__} {self._uuid} at {hex(id(self))}>"
