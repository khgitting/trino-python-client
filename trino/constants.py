# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from typing import Any, Optional


DEFAULT_PORT = 8080
DEFAULT_TLS_PORT = 443
DEFAULT_SOURCE = "trino-python-client"
DEFAULT_CATALOG: Optional[str] = None
DEFAULT_SCHEMA: Optional[str] = None
DEFAULT_AUTH: Optional[Any] = None
DEFAULT_MAX_ATTEMPTS = 3
DEFAULT_REQUEST_TIMEOUT: float = 30.0

HTTP = "http"
HTTPS = "https"

URL_STATEMENT_PATH = "/v1/statement"

TRINO_OR_PRESTO = os.environ.get("TRINO_OR_PRESTO_HTTP_HEADER", "Trino")

HEADER_CATALOG = f"X-{TRINO_OR_PRESTO}-Catalog"
HEADER_SCHEMA = f"X-{TRINO_OR_PRESTO}-Schema"
HEADER_SOURCE = f"X-{TRINO_OR_PRESTO}-Source"
HEADER_USER = f"X-{TRINO_OR_PRESTO}-User"
HEADER_CLIENT_INFO = f"X-{TRINO_OR_PRESTO}-Client-Info"
HEADER_EXTRA_CREDENTIAL = f"X-{TRINO_OR_PRESTO}-Extra-Credential"

HEADER_SESSION = f"X-{TRINO_OR_PRESTO}-Session"
HEADER_SET_SESSION = f"X-{TRINO_OR_PRESTO}-Set-Session"
HEADER_CLEAR_SESSION = f"X-{TRINO_OR_PRESTO}-Clear-Session"

HEADER_STARTED_TRANSACTION = f"X-{TRINO_OR_PRESTO}-Started-Transaction-Id"
HEADER_TRANSACTION = f"X-{TRINO_OR_PRESTO}-Transaction-Id"

HEADER_PREPARED_STATEMENT = f'X-{TRINO_OR_PRESTO}-Prepared-Statement'
HEADER_ADDED_PREPARE = f'X-{TRINO_OR_PRESTO}-Added-Prepare'
HEADER_DEALLOCATED_PREPARE = f'X-{TRINO_OR_PRESTO}-Deallocated-Prepare'
