# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements. See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership. The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied. See the License for the
# specific language governing permissions and limitations
# under the License.
#

FROM python:3.6-alpine

LABEL maintainer="Dan Chaffelson <chaffelson@gmail.com>"
LABEL site="https://github.com/Chaffelson/whoville"

ENV PYTHONUNBUFFERED=0
ENV TZ=${TZ:-"Europe/London"}


ADD ./requirements.txt /requirements.txt

RUN apk update && apk upgrade \
    && apk add --no-cache --virtual .build-deps git gcc libffi-dev musl-dev \
    libressl-dev ca-certificates python3-dev linux-headers tzdata \
    && cp /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone \
    && pip install --upgrade pip \
    && pip install --no-cache -r requirements.txt \
    && apk del .build-deps \
    && apk add --no-cache bash


ADD ./ /whoville
WORKDIR /whoville
RUN mv profile.RENAME.yml profile.yml
ENV PYTHONPATH=/whoville

ENTRYPOINT ["python3"]
CMD ["whoville/mayor.py"]


# Build & Run Example from project root /whoville
# docker build -f="./docker/v2/localdev/Dockerfile" -t whoville:next . && docker run -v /whoville:/whoville --env PROFILE=/whoville/profile.yml --name whovillenext whoville:next
# --no-use-pep517 required for bug in pip 19.0+

# Can be exported with docker save whoville:private | gzip > whoville.tar.gz
# Can be imported with docker load < whoville.tar.gz