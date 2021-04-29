from django.urls import reverse


def test_todo_list_view_exist(client):
    url = reverse('todo-list')
    response = client.get(url)
    assert response.status_code == 200
