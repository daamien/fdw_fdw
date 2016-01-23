#!/bin/bash
set -e

gosu postgres psql -f /tmp/install.sql
