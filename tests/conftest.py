# -*- coding: utf-8 -*-
#
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
import pytest
import os
from rocketmq.client import Producer, PushConsumer

topic_orderly = 'test-topic-normal-orderly'
name_srv = os.getenv('NAMESRV_ADDR', 'localhost:9876')


@pytest.fixture(scope='session')
def producer():
    prod = Producer('testGroup', True)
    prod.set_namesrv_addr(name_srv)
    prod.start()
    yield prod
    prod.shutdown()


@pytest.fixture(scope='function')
def push_consumer():
    consumer = PushConsumer('testGroup')
    consumer.set_namesrv_addr(name_srv)
    yield consumer
    consumer.shutdown()
