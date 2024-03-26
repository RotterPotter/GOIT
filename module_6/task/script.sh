#!/usr/bin/env bash


psql -U root -d mydb -a -f $1
