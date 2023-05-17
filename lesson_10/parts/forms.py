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
        help_text='Part designation can only contain numbers, '
                  'hyphens and dots.',
    )
    name = forms.CharField(
        label='Name',
        help_text='Part name can only contain letters, numbers and spaces.',
    )

    def clean_designation(self):
        msg_err = 'Invalid symbols! ' \
                  'Part designation can only contain numbers, hyphens and dots.'
        designation = self.cleaned_data['designation']
        if not self.__is_valid_designation(designation):
            raise forms.ValidationError(msg_err)
        return designation

    def clean_name(self):
        msg_err = 'Invalid symbols! ' \
                  'Part name can only contain letters, numbers and spaces.'
        name = self.cleaned_data['name']
        if not self.__is_valid_name(name):
            raise forms.ValidationError(msg_err)
        return name

    class Meta:
        model = Part
        fields = '__all__'

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

    # TODO: переписать через регулярное выражение
    def __is_valid_designation(self, name: str) -> bool:
        hyphen = {45}
        dot = {46}
        digits = set(range(48, 58))
        valid_chars = hyphen | dot | digits
        for i in name:
            if ord(i) not in valid_chars:
                return False
        return True
