# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 GNS3 Technologies Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


VPCS_CREATE_SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "description": "Request validation to create a new VPCS instance",
    "type": "object",
    "properties": {
        "name": {
            "description": "VPCS device name",
            "type": "string",
            "minLength": 1,
        },
        "id": {
            "description": "VPCS device instance ID",
            "type": "integer"
        },
        "uuid": {
            "description": "VPCS device UUID",
            "type": "string",
            "minLength": 36,
            "maxLength": 36,
            "pattern": "^[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$"
        },
        "console": {
            "description": "console TCP port",
            "minimum": 1,
            "maximum": 65535,
            "type": "integer"
        },
    },
    "additionalProperties": False,
    "required": ["name"]
}


VPCS_NIO_SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "description": "Request validation to add a NIO for a VPCS instance",
    "type": "object",

    "definitions": {
        "UDP": {
            "description": "UDP Network Input/Output",
            "properties": {
                "type": {
                    "enum": ["nio_udp"]
                },
                "lport": {
                    "description": "Local port",
                    "type": "integer",
                    "minimum": 1,
                    "maximum": 65535
                },
                "rhost": {
                    "description": "Remote host",
                    "type": "string",
                    "minLength": 1
                },
                "rport": {
                    "description": "Remote port",
                    "type": "integer",
                    "minimum": 1,
                    "maximum": 65535
                }
            },
            "required": ["type", "lport", "rhost", "rport"],
            "additionalProperties": False
        },
        "TAP": {
            "description": "TAP Network Input/Output",
            "properties": {
                "type": {
                    "enum": ["nio_tap"]
                },
                "tap_device": {
                    "description": "TAP device name e.g. tap0",
                    "type": "string",
                    "minLength": 1
                },
            },
            "required": ["type", "tap_device"],
            "additionalProperties": False
        },
    },

    "oneOf": [
        {"$ref": "#/definitions/UDP"},
        {"$ref": "#/definitions/TAP"},
    ],
    "additionalProperties": True,
    "required": ['type']
}

VPCS_OBJECT_SCHEMA = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "description": "VPCS instance",
    "type": "object",
    "properties": {
        "name": {
            "description": "VPCS device name",
            "type": "string",
            "minLength": 1,
        },
        "id": {
            "description": "VPCS device instance ID",
            "type": "integer"
        },
        "console": {
            "description": "console TCP port",
            "minimum": 1,
            "maximum": 65535,
            "type": "integer"
        },
    },
    "additionalProperties": False,
    "required": ["name", "id", "console"]
}
