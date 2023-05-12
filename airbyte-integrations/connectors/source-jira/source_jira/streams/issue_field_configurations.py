#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#


import requests

from .base import JiraStream


class IssueFieldConfigurations(JiraStream):
    """
    https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issue-field-configurations/#api-rest-api-3-fieldconfiguration-get
    """

    extract_field = "values"
    skip_http_status_codes = [
        # Only Jira administrators can access field configurations
        requests.codes.FORBIDDEN
    ]

    def path(self, **kwargs) -> str:
        return "fieldconfiguration"