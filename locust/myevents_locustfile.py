from locust import HttpUser, task, constant

class MyEventsUser(HttpUser):
    # Constant wait time for stable and comparable load
    wait_time = constant(1)

    @task
    def view_my_events(self):
        # Clean request name for grouped statistics
        self.client.get(
            "/my-events?user=locust_user",
            name="/my-events"
        )
