#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#

import os

from dagster import Field, InitResourceContext, StringSource, resource

from .file_managers.local_file_manager import SimpleLocalFileManager


@resource(
    config_schema={
        "base_dir": Field(StringSource, is_required=False),
    },
)
def simple_local_file_manager(resource_context: InitResourceContext) -> SimpleLocalFileManager:
    """FileManager that provides abstract access to Local file storage.

    Implements the :py:class:`~dagster._core.storage.file_manager.FileManager` API.
    """

    return SimpleLocalFileManager(
        base_dir=resource_context.resource_config.get(
            "base_dir", os.path.join(resource_context.instance.storage_directory(), "file_manager")
        )
    )
