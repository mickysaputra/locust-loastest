from locust import HttpUser, TaskSet, task
import json
import os

api_key = "Bearer " + os.getenv('grafana-old_SQLITE_API_KEY')
header_template = {
    "Content-Type":"application/json",
    "Authorization":api_key,
    "Accept":"application/json"
}

def MemoryUsageJob(self):
    data1 = {
        "queries":[
            {
                "refId":"A",
                "datasource":{
                    "type": "prometheus",
                    "uid":"jAg31STVk"
                },
            "editorMode": "builder",
            "expr": "avg(nomad_client_allocs_memory_allocated{exported_job=\"mimir-distributed\"}) by (task,task_group,namespace)",
            "queryType": "timeSeriesQuery",
            "maxLines": 1000,
            "legendFormat": "__auto",
            "datasourceId": 13,
            "intervalMs": 15000,
            "maxDataPoints": 1459
            }
        ],
        "from":"now-1h",
        "to":"now"
    }
    self.client.post(
        url="http://grafana-old.service.consul/api/ds/query",
        data=json.dumps(data1),
        auth=None,
        headers=header_template
    )
    data2 = {
        "queries":[
            {
                "refId":"A",
                "datasource":{
                    "type": "prometheus",
                    "uid":"jAg31STVk"
                },
            "editorMode": "builder",
            "expr": "avg(nomad_client_allocs_memory_usage{exported_job=\"mimir-distributed\"}) by (task,task_group,namespace)",
            "queryType": "timeSeriesQuery",
            "maxLines": 1000,
            "legendFormat": "__auto",
            "datasourceId": 13,
            "intervalMs": 15000,
            "maxDataPoints": 1459
            }
        ],
        "from":"now-1h",
        "to":"now"
    }
    self.client.post(
        url="http://grafana-old.service.consul/api/ds/query",
        data=json.dumps(data2),
        auth=None,
        headers=header_template
    )

def CpuUsageJob(self):
    data1 = {
        "queries":[
            {
                "refId":"A",
                "datasource":{
                    "type": "prometheus",
                    "uid":"jAg31STVk"
                },
            "editorMode": "builder",
            "expr": "avg(nomad_client_allocs_cpu_allocated{exported_job=\"mimir-distributed\"}) by (task,task_group,namespace)",
            "queryType": "timeSeriesQuery",
            "maxLines": 1000,
            "legendFormat": "__auto",
            "datasourceId": 13,
            "intervalMs": 15000,
            "maxDataPoints": 1459
            }
        ],
        "from":"now-1h",
        "to":"now"
    }
    self.client.post(
        url="http://grafana-old.service.consul/api/ds/query",
        data=json.dumps(data1),
        auth=None,
        headers=header_template
    )
    data2 = {
        "queries":[
            {
                "refId":"A",
                "datasource":{
                    "type": "prometheus",
                    "uid":"jAg31STVk"
                },
            "editorMode": "builder",
            "expr": "avg(nomad_client_allocs_cpu_total_ticks{exported_job=\"mimir-distributed\"}) by (task,task_group,namespace)",
            "queryType": "timeSeriesQuery",
            "maxLines": 1000,
            "legendFormat": "__auto",
            "datasourceId": 13,
            "intervalMs": 15000,
            "maxDataPoints": 1459
            }
        ],
        "from":"now-1h",
        "to":"now"
    }
    self.client.post(
        url="http://grafana-old.service.consul/api/ds/query",
        data=json.dumps(data2),
        auth=None,
        headers=header_template
    )

def MemoryUtilizationJob(self):
    data = {
        "queries":[
            {
                "refId":"A",
                "datasource":{
                    "type": "prometheus",
                    "uid":"jAg31STVk"
                },
            "editorMode": "builder",
            "expr": "(avg(nomad_client_allocs_memory_usage{exported_job=\"mimir-distributed\"}) by (task,task_group,namespace) \r\n/\r\navg(nomad_client_allocs_memory_allocated{exported_job=\"mimir-distributed\"}) by (task,task_group,namespace)) * 100",
            "queryType": "timeSeriesQuery",
            "maxLines": 1000,
            "legendFormat": "__auto",
            "datasourceId": 13,
            "intervalMs": 15000,
            "maxDataPoints": 1459
            }
        ],
        "from":"now-1h",
        "to":"now"
    }
    self.client.post(
        url="http://grafana-old.service.consul/api/ds/query",
        data=json.dumps(data),
        auth=None,
        headers=header_template
    )

def CpuUtilizationJob(self):
    data = {
        "queries":[
            {
                "refId":"A",
                "datasource":{
                    "type": "prometheus",
                    "uid":"jAg31STVk"
                },
            "editorMode": "builder",
            "expr": "(avg(nomad_client_allocs_cpu_total_ticks{exported_job=\"mimir-distributed\"}) by (task,task_group,namespace) \r\n/\r\navg(nomad_client_allocs_cpu_allocated{exported_job=\"mimir-distributed\"}) by (task,task_group,namespace)) * 100",
            "queryType": "timeSeriesQuery",
            "maxLines": 1000,
            "legendFormat": "__auto",
            "datasourceId": 13,
            "intervalMs": 15000,
            "maxDataPoints": 1459
            }
        ],
        "from":"now-1h",
        "to":"now"
    }
    self.client.post(
        url="http://grafana-old.service.consul/api/ds/query",
        data=json.dumps(data),
        auth=None,
        headers=header_template
    )

def MemoryUsageAlloc(self):
    data1 = {
        "queries":[
            {
                "refId":"A",
                "datasource":{
                    "type": "prometheus",
                    "uid":"jAg31STVk"
                },
            "editorMode": "builder",
            "expr": "avg(nomad_client_allocs_memory_allocated{exported_job=\"mimir-distributed\"}) by (task,task_group,namespace)",
            "queryType": "timeSeriesQuery",
            "maxLines": 1000,
            "legendFormat": "__auto",
            "datasourceId": 13,
            "intervalMs": 15000,
            "maxDataPoints": 1459
            }
        ],
        "from":"now-1h",
        "to":"now"
    }
    self.client.post(
        url="http://grafana-old.service.consul/api/ds/query",
        data=json.dumps(data1),
        auth=None,
        headers=header_template
    )
    data2 = {
        "queries":[
            {
                "refId":"A",
                "datasource":{
                    "type": "prometheus",
                    "uid":"jAg31STVk"
                },
            "editorMode": "builder",
            "expr": "nomad_client_allocs_memory_usage{exported_job=\"mimir-distributed\"}",
            "queryType": "timeSeriesQuery",
            "maxLines": 1000,
            "legendFormat": "__auto",
            "datasourceId": 13,
            "intervalMs": 15000,
            "maxDataPoints": 1459
            }
        ],
        "from":"now-1h",
        "to":"now"
    }
    self.client.post(
        url="http://grafana-old.service.consul/api/ds/query",
        data=json.dumps(data2),
        auth=None,
        headers=header_template
    )

def CpuUsageAlloc(self):
    data1 = {
        "queries":[
            {
                "refId":"A",
                "datasource":{
                    "type": "prometheus",
                    "uid":"jAg31STVk"
                },
            "editorMode": "builder",
            "expr": "avg(nomad_client_allocs_cpu_allocated{exported_job=\"mimir-distributed\"}) by (task,task_group,namespace) * 1000000",
            "queryType": "timeSeriesQuery",
            "maxLines": 1000,
            "legendFormat": "__auto",
            "datasourceId": 13,
            "intervalMs": 15000,
            "maxDataPoints": 1459
            }
        ],
        "from":"now-1h",
        "to":"now"
    }
    self.client.post(
        url="http://grafana-old.service.consul/api/ds/query",
        data=json.dumps(data1),
        auth=None,
        headers=header_template
    )
    data2 = {
        "queries":[
            {
                "refId":"A",
                "datasource":{
                    "type": "prometheus",
                    "uid":"jAg31STVk"
                },
            "editorMode": "builder",
            "expr": "nomad_client_allocs_cpu_total_ticks{exported_job=\"mimir-distributed\"} * 1000000",
            "queryType": "timeSeriesQuery",
            "maxLines": 1000,
            "legendFormat": "__auto",
            "datasourceId": 13,
            "intervalMs": 15000,
            "maxDataPoints": 1459
            }
        ],
        "from":"now-1h",
        "to":"now"
    }
    self.client.post(
        url="http://grafana-old.service.consul/api/ds/query",
        data=json.dumps(data2),
        auth=None,
        headers=header_template
    )

def MemoryUtilizationAlloc(self):
    data = {
        "queries":[
            {
                "refId":"A",
                "datasource":{
                    "type": "prometheus",
                    "uid":"jAg31STVk"
                },
            "editorMode": "builder",
            "expr": "(nomad_client_allocs_memory_usage{exported_job=\"mimir-distributed\"} \r\n/\r\nnomad_client_allocs_memory_allocated{exported_job=\"mimir-distributed\"}) * 100",
            "queryType": "timeSeriesQuery",
            "maxLines": 1000,
            "legendFormat": "__auto",
            "datasourceId": 13,
            "intervalMs": 15000,
            "maxDataPoints": 1459
            }
        ],
        "from":"now-1h",
        "to":"now"
    }
    self.client.post(
        url="http://grafana-old.service.consul/api/ds/query",
        data=json.dumps(data),
        auth=None,
        headers=header_template
    )

def CpuUtilizationAlloc(self):
    data = {
        "queries":[
            {
                "refId":"A",
                "datasource":{
                    "type": "prometheus",
                    "uid":"jAg31STVk"
                },
            "editorMode": "builder",
            "expr": "(nomad_client_allocs_cpu_total_ticks{exported_job=\"mimir-distributed\"} \r\n/\r\nnomad_client_allocs_cpu_allocated{exported_job=\"mimir-distributed\"}) * 100",
            "queryType": "timeSeriesQuery",
            "maxLines": 1000,
            "legendFormat": "__auto",
            "datasourceId": 13,
            "intervalMs": 15000,
            "maxDataPoints": 1459
            }
        ],
        "from":"now-1h",
        "to":"now"
    }
    self.client.post(
        url="http://grafana-old.service.consul/api/ds/query",
        data=json.dumps(data),
        auth=None,
        headers=header_template
    )


class JobDashboard(TaskSet):

    @task
    def job_dashboard(self):
        MemoryUsageJob(self)
        CpuUsageJob(self)
        MemoryUtilizationJob(self)
        CpuUtilizationJob(self)
        MemoryUsageAlloc(self)
        CpuUsageAlloc(self)
        MemoryUtilizationAlloc(self)
        CpuUtilizationAlloc(self)

class grafana-oldSQLite(HttpUser):
    
    tasks = {JobDashboard}
