from django import forms

from .models import Material


class MaterialSearchForm(forms.Form):
    name = forms.CharField(
        label='Search by material name',
        required=False,
    )


class MaterialCreateAndUpdateForm(forms.ModelForm):
    name = forms.CharField(
        label='Material name',
        help_text='Material name can only contain letters, numbers and spaces.',
    )
    density = forms.IntegerField(
        label='Material density',
        help_text='Material density value must be positive integer.',
        required=False,
        min_value=0,
    )

    def clean_name(self):
        msg_err = 'Invalid symbols! ' \
                  'Material name can only contain letters, numbers and spaces.'
        name = self.cleaned_data['name']
        if not self.__is_valid_name(name):
            raise forms.ValidationError(msg_err)
        return name

    class Meta:
        model = Material
        fields = ('name', 'density',)

    # TODO: переписать через регулярное выражение
    def __is_valid_name(self, name: str) -> bool:
        space = {32}
        digits = set(range(48, 58))
        alphabet_upper = set(range(65, 91))
        alphabet_lower = set(range(97, 123))
        valid_chars = space | digits | alphabet_upper | alphabet_lower
        for i in name:
            if ord(i) not in valid_chars:
                return False
        return True
