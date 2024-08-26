from rest_framework.reverse import reverse_lazy


class TestUrl:
    def test_users_list(self):
        url = reverse_lazy('users:user-list')
        assert url == '/api/v1/users/users'

    def test_auth_send_code(self):
        url = reverse_lazy('users:send_code')
        assert url == '/api/v1/users/auth/send-code'
