from locust import HttpLocust, TaskSet, task, between

class ElbTasks(TaskSet):
  @task
  def status(self):
    payload = {"key": "value"}
    response = self.client.post("/", json=payload)
    if not response.ok:
    	print(response.status_code, " content: ", response.content)

class ElbWarmer(HttpLocust):
  task_set = ElbTasks
  wait_time = between(1, 20)