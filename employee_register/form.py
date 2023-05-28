from cProfile import label
from .models import Employee
from django.forms import ModelForm

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        labels = {
            'name': 'Full Name',
            'emp_code': 'EMP.Code',
        }
    
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = 'Select'
        self.fields['emp_code'].required = False