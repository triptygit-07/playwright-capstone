class UsersAPI:

    def __init__(self, request_context):
        self.request = request_context

    def get_user(self, user_id):
        return self.request.get(f"/users/{user_id}")

    def get_users(self):
        return self.request.get("/users")

    def create_user(self, user_data):
        return self.request.post(
            "/users",
            data=user_data
        )

    def update_user(self, user_id, user_data):
        return self.request.put(
            f"/users/{user_id}",
            data=user_data
        )

    def delete_user(self, user_id):
        return self.request.delete(f"/users/{user_id}")

    def health_check(self):
        return self.request.get("/users")