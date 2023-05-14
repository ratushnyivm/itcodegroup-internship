from django import forms

from .models import Material


class MaterialSearchForm(forms.Form):
    name = forms.CharField(
        label='Search by material name',
        required=False,
    )

    # def clean_name(self):
    #     name = self.cleaned_data['name']
    #     if ';' in name:
    #         raise forms.ValidationError('Имя не должно содержать ";"')
    #     return name

    # def clean(self):
    #     name = self.cleaned_data['name']
    #     if ';' in name:
    #         raise forms.ValidationError('Имя не должно содержать ";"')
    #     return name


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
        name = self.cleaned_data['name']
        if ';' in name:
            raise forms.ValidationError('Имя не должно содержать ";"')
        return name

    class Meta:
        model = Material
        fields = ('name', 'density',)
