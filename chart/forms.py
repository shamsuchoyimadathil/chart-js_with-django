from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit,Column
from crispy_forms.bootstrap import FormActions

from . models import Chart


class ChartForm(forms.ModelForm):
    class Meta:
        model = Chart
        fields = "__all__"
        labels = {
            "heading":"What percentage do you want to see ?",
            "content":"subject/year/content",
            "percentage":"value"
        }

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method ="POST"
        self.helper.layout = Layout(
            Column('heading',id="heading_form"),
            Column(
                'content',
                'percentage'
            ),


            FormActions(

            Submit('save','Save',css_class="btn btn-primary col text-center mt-2 mb-2",),
            #Submit('','Clear All',css_class="btn btn-danger col text-center mt-2",id="clear_btn", sdfas=True)
            )
        )


class ChartForm1(forms.ModelForm):
    class Meta:
        model = Chart
        fields = ["content","percentage"]
        labels = {
            "content":"subject/year/content",
            "percentage":"value"
        }

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method ="POST"
        self.helper.layout = Layout(
            #Column('heading',id="heading_form"),
            Column(
                'content',
                'percentage'
            ),


            FormActions(

            Submit('save','Save',css_class="btn btn-primary col text-center mt-2 ml-2 mb-2",),
            )
        )






