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
from uuid import UUID, uuid1


class Hashable:
    """
    A base class for objects that can be uniquely identified and compared using a UUID.

    The `Hashable` class generates a UUID for each instance, which is used to make instances
    hashable and comparable. If a UUID is not provided during initialization, a new UUID
    is generated automatically.

    :ivar UUID _uuid: The unique identifier for the instance. This is either provided during
                     initialization or generated automatically using `uuid1()`.
    """

    def __init__(self, uuid: Optional[UUID] = None) -> None:
        """
        Initializes a Hashable instance.

        :param uuid: The UUID for the instance. If not provided, a new UUID is generated
                    using `uuid1()`.
        :type uuid: Optional[UUID]
        """

        self._uuid: Optional[UUID] = uuid
        if not uuid:
            self._uuid: UUID = uuid1()

    @property
    def uuid(self) -> UUID:
        """
        Returns the UUID of the instance.

        :return: The unique identifier for this instance.
        :rtype: UUID
        """

        return self._uuid

    def __eq__(self, other: Any) -> bool:
        """
        Checks if this instance is equal to another `Hashable` instance based on the UUID.

        :param other: The other object to compare against.
        :type other: Any
        :return: `True` if the other object is a `Hashable` instance with the same UUID, `False` otherwise.
        :rtype: bool
        """

        if not isinstance(other, Hashable):
            return False
        return self._uuid == other.uuid

    def __hash__(self) -> int:
        """
        Returns the hash value of the instance, based on the UUID.

        :return: The hash value of the UUID.
        :rtype: int
        """
        return hash(self._uuid)

    def __repr__(self) -> str:
        """
        Returns a string representation of the instance for debugging.

        :return: A string representation including the module, class name, UUID, and memory address.
        :rtype: str
        """

        return f"<{type(self).__module__}.{type(self).__name__} {self._uuid} at {hex(id(self))}>"
