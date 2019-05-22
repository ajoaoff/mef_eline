#!/usr/bin/env bash

mkdir /tmp/of_core1
cd /tmp/of_core1
git clone https://github.com/kytos/of_core.git
cd of_core
kytos napps install kytos/of_core

