#!/usr/bin/env bash

curl -X POST \
  http://localhost:8181/api/kytos/mef_eline/v2/evc/ \
  -H 'Content-Type: application/json' \
  -H 'cache-control: no-cache' \
  -d '{
	"name": "Teste4",
	"uni_a": {
		"interface_id": "00:00:00:00:00:00:00:06:11",
		"tag": {
			"tag_type": 1,
			"value": 611
		}
	},
	"uni_z": {
		"interface_id": "00:00:00:00:00:00:00:02:11",
		"tag": {
			"tag_type": 1,
			"value": 211
		}
	},
	"circuit_scheduler": [
		{
			"frequency": "0 * * * *",
			"action": "create"
		},
		{
			"frequency": "45 * * * *",
			"action": "remove"
		}
	],
	"end_date": "2018-12-29T15:16:50",
	"dynamic_backup_path": true,
	"active": true,
	"enabled": true
}'
