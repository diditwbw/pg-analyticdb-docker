#!/bin/bash

# Wait for the DB to be ready
sleep 10

# Upgrade DB and create admin user
superset db upgrade

superset fab create-admin \
  --username "${ADMIN_USERNAME:-admin}" \
  --firstname "${ADMIN_FIRSTNAME:-Admin}" \
  --lastname "${ADMIN_LASTNAME:-User}" \
  --email "${ADMIN_EMAIL:-admin@example.com}" \
  --password "${ADMIN_PASSWORD:-admin}"

superset init

# Run Superset
superset run -h 0.0.0.0 -p 8088
