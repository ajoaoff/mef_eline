#!/usr/bin/env bash

curl -X POST \
  http://localhost:8181/api/kytos/mef_eline/v2/evc/ \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -d '{
	"name": "Teste6",
	"uni_a": {
		"interface_id": "00:00:00:00:00:00:00:04:12",
		"tag": {
			"tag_type": 1,
			"value": 421
		}
	},
	"uni_z": {
		"interface_id": "00:00:00:00:00:00:00:06:12",
		"tag": {
			"tag_type": 1,
			"value": 623
		}
	},
	"primary_path": [
		{
			"endpoint_a": {"id": "00:00:00:00:00:00:00:04:2" },
			"endpoint_b": {"id": "00:00:00:00:00:00:00:05:3" }
		},
		{
			"endpoint_a": {"id": "00:00:00:00:00:00:00:05:4" },
			"endpoint_b": {"id": "00:00:00:00:00:00:00:06:2" }
		}
	],
	"circuit_scheduler": [
		{
			"frequency": "*/10 * * * *",
			"action": "create"
		},
		{
			"frequency": "8-59/10 * * * *",
			"action": "remove"
		}
	],
	"end_date": "2018-12-29T15:16:50",
	"dynamic_backup_path": true,
	"active": true,
	"enabled": true
}'
