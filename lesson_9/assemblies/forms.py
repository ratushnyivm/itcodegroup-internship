from django import forms

from .models import Assembly


class AssemblySearchForm(forms.Form):
    search_query = forms.CharField(
        label='Search by assembly designation or name',
        required=False,
    )


class AssemblyCreateAndUpdateForm(forms.ModelForm):

    designation = forms.CharField(
        label='Designation',
        help_text='Assembly designation can only contain letters, '
                  'numbers and spaces.',
    )
    name = forms.CharField(
        label='Name',
        help_text='Assembly name can only contain letters, numbers and spaces.',
    )

    class Meta:
        model = Assembly
        fields = '__all__'
