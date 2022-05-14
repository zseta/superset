# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
from superset.db_engine_specs.postgres import PostgresEngineSpec


class TimescaleDbEngineSpec(PostgresEngineSpec):
    engine = "timescaledb"
    engine_name = "TimescaleDB"

    """_time_grain_expressions = {
        None: "{col}",
        "PT1S": "time_bucket('1 sec', {col})",
        "PT5S": "time_bucket('5 sec', {col})",
        "PT1M": "time_bucket('1 min', {col})",
        "PT5M": "time_bucket('5 min', {col})",
        "PT1H": "time_bucket('hour', {col})",
        "P1D": "time_bucket('day', {col})",
        "P1W": "time_bucket('week', {col})",
    }"""
