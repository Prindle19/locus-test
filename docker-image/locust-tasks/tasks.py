#!/usr/bin/env python

# Copyright 2015 Google Inc. All rights reserved.
#
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


import uuid

from datetime import datetime
from locust import HttpLocust, TaskSet, task
from random import randint

class MetricsTaskSet(TaskSet):
    _deviceid = None

    def on_start(self):
        self._deviceid = str(uuid.uuid4())

    @task(1)
    def tile(self):
	z = str(randint(0,20))
	x = str(randint(0,10000000))
	y = str(randint(0,10000000))
	name = "loadtest"
	key = "loadtest"
	urlString = "/getTile/?z=%s&x=%s&y=%s&key=%s&name=%s" % (z,x,y,key,name) 
        self.client.get(urlString)

class MetricsLocust(HttpLocust):
    task_set = MetricsTaskSet
    min_wait = 100
    max_wait = 5000
