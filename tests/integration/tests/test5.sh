#!/usr/bin/env bash

curl -X POST \
  http://localhost:8181/api/kytos/mef_eline/v2/evc/ \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -d '{
	"name": "Teste5",
	"uni_a": {
		"interface_id": "00:00:00:00:00:00:00:04:11",
		"tag": {
			"tag_type": 1,
			"value": 414
		}
	},
	"uni_z": {
		"interface_id": "00:00:00:00:00:00:00:03:11",
		"tag": {
			"tag_type": 1,
			"value": 311
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
		},
		{
			"endpoint_a": {"id": "00:00:00:00:00:00:00:06:1"},
			"endpoint_b": {"id": "00:00:00:00:00:00:00:01:3"}
		},
		{
			"endpoint_a": {"id": "00:00:00:00:00:00:00:01:1"},
			"endpoint_b": {"id": "00:00:00:00:00:00:00:03:1"}
		}
	],
	"backup_path": [
		{
			"endpoint_a": {"id": "00:00:00:00:00:00:00:04:2" },
			"endpoint_b": {"id": "00:00:00:00:00:00:00:05:3" }
		},
		{
			"endpoint_a": {"id": "00:00:00:00:00:00:00:05:1" },
			"endpoint_b": {"id": "00:00:00:00:00:00:00:02:2" }
		},		{
			"endpoint_a": {"id": "00:00:00:00:00:00:00:02:1"},
			"endpoint_b": {"id": "00:00:00:00:00:00:00:03:2"}
		}
	],
	"circuit_scheduler": [
		{
			"frequency": "*/2 * * * *",
			"action": "create"
		},
		{
			"frequency": "1-59/2 * * * *",
			"action": "remove"
		}
	],
	"end_date": "2018-12-29T15:16:50",
	"dynamic_backup_path": true,
	"active": true,
	"enabled": true
}'
