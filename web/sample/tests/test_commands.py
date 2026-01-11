import pytest
from django.core.management import call_command

from sample.models import SampleModel


@pytest.mark.django_db
class TestSampleCommand:
    def test_sample_command(self):
        call_command("sample_command", 3)
        assert SampleModel.objects.count() == 3

    def test_sample_command_outputs_success_message(self, capsys):
        call_command("sample_command", 3)
        captured = capsys.readouterr()
        # 成功メッセージが stdout に出力されていることを確認
        assert "3 件の SampleModel のデータを作成しました。" in captured.out
