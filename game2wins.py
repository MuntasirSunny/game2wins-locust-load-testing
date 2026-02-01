from locust import HttpUser, task, between, SequentialTaskSet, TaskSet

# ---------- WEBSITE PAGE TESTING ----------
class WebsiteUserTasks(SequentialTaskSet):
    @task
    def load_homepage(self):
        self.client.get("/", name="Home Page")

    @task
    def load_login(self):
        self.client.get("/signin", name="Sign In Page")

    @task
    def load_game_page(self):
        self.client.get("/category/leaderboard-games", name="Category Details Page")

    @task
    def load_token_bundles(self):
        self.client.get("/game/ninja-dash", name="Ninja Game Page")

    @task
    def load_token_bundles(self):
        self.client.get("/purchase-packages", name="Subscription Package Page")


# ---------- API TESTING ----------
class ApiUserTasks(SequentialTaskSet):
    @task
    def get_all_games(self):
        self.client.get(
            "https://stage.game2wins.com/api/page-layouts/homelayout",
            name="Home Page Layout API"
        )

    @task
    def get_all_battle_games(self):
        self.client.get(
            "https://stage.game2wins.com/api/banners?page=home",
            name="Banner List API"
        )

    @task
    def get_all_campaigns(self):
        self.client.get(
            "https://stage.game2wins.com/api/subscription-packages?countryCode=BD",
            name="Subscription Package API"
        )

    @task
    def get_leaderboard_games(self):
        self.client.get(
            "https://stage.game2wins.com/api/category-list?slug=leaderboard-games&page=1&limit=10",
            name="Leaderboard Games API"
        )


# ---------- USER CLASSES ----------
class WebsiteUser(HttpUser):
    """Simulates users browsing the main Game2wins site"""
    host = "https://stage.game2wins.com"
    tasks = [WebsiteUserTasks]
    wait_time = between(1, 5)  # Wait between 1 and 5 seconds between tasks


class ApiUser(HttpUser):
    """Simulates API traffic to the Game2wins API endpoints"""
    host = "https://stage.game2wins.com"
    tasks = [ApiUserTasks]
    wait_time = between(1, 3)  # Slightly faster requests to simulate API load
