#!/usr/bin/env bash

curl -X POST \
  http://localhost:8181/api/kytos/mef_eline/v2/evc/ \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -d '{
	"name": "Teste3",
	"uni_a": {
		"interface_id": "00:00:00:00:00:00:00:04:13",
		"tag": {
			"tag_type": 1,
			"value": 431
		}
	},
	"uni_z": {
		"interface_id": "00:00:00:00:00:00:00:02:11",
		"tag": {
			"tag_type": 1,
			"value": 213
		}
	},
	"primary_path": [
		{
			"endpoint_a": {"id": "00:00:00:00:00:00:00:04:1" },
			"endpoint_b": {"id": "00:00:00:00:00:00:00:01:2" }
		},
		{
			"endpoint_a": {"id": "00:00:00:00:00:00:00:01:1" },
			"endpoint_b": {"id": "00:00:00:00:00:00:00:03:1" }
		},		{
			"endpoint_a": {"id": "00:00:00:00:00:00:00:03:2"},
			"endpoint_b": {"id": "00:00:00:00:00:00:00:02:1"}
		}
	],
	"end_date": "2018-12-29T15:16:50",
	"dynamic_backup_path": true,
	"active": true,
	"enabled": true
}'
