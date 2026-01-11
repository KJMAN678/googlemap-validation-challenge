import pytest

from sample.factories import SampleModelFactory, UserFactory


@pytest.mark.django_db
class TestIndexView:
    def test_correct_response_index_view(self, client):
        sample_models = SampleModelFactory.create()
        user = UserFactory.create()
        client.force_login(user)
        response = client.get("")
        assert response.status_code == 200
        assert response.context["samples"][0].name == sample_models.name
        assert response.context["samples"][0].description == sample_models.description
        assert response.context["samples"][0].created_at == sample_models.created_at
        assert response.context["samples"][0].updated_at == sample_models.updated_at

    def test_correct_size_response_index_view(self, client):
        SampleModelFactory.create_batch(3)
        user = UserFactory.create()
        client.force_login(user)
        response = client.get("")
        assert len(response.context["samples"]) == 3

    def test_clicked_view(self, client):
        user = UserFactory.create()
        client.force_login(user)
        response = client.get("/clicked")
        assert response.status_code == 200
        assert response.context["message"] == "Button clicked!"
