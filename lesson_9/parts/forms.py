from django import forms

from .models import Part


class PartSearchForm(forms.Form):
    search_query = forms.CharField(
        label='Search by part designation or name',
        required=False,
    )


class PartCreateAndUpdateForm(forms.ModelForm):

    designation = forms.CharField(
        label='Designation',
        help_text='Part designation can only contain letters, '
                  'numbers and spaces.',
    )
    name = forms.CharField(
        label='Name',
        help_text='Part name can only contain letters, numbers and spaces.',
    )

    class Meta:
        model = Part
        fields = '__all__'
