from django.forms import ModelForm
from .models import RegistroHoraExtra
from apps.funcionarios.models import Funcionario


class RegistroHoraExtraForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(RegistroHoraExtraForm, self).__init__(*args, **kwargs)
        self.fields['funcionario'].queryset = Funcionario.objects.filter(
            empresa=user.funcionario.empresa
        ).order_by('nome')

    class Meta:
        model = RegistroHoraExtra
        fields = '__all__'