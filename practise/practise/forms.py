from django import forms
import datetime

Star=[
    ('1','1 Start'),
    ('2','2 Start'),
    ('3','3 Start'),
    ('4','4 Start'),
    ('5','5 Start'),
]

class PractiseForm(forms.Form):
    name=forms.CharField()


    comment=forms.CharField(widget=forms.Textarea(attrs={'rows':3}))

    email=forms.EmailField()

    agree=forms.BooleanField()

    date=forms.DateField()

    birth_date = forms.CharField(widget=forms.DateInput(attrs= {'type' : 'date'}))

    birth_year=forms.DateField(widget=forms.SelectDateWidget)
    

    value=forms.DecimalField()

    name=forms.CharField(
        max_length=10
    )

    email_adress=forms.EmailField(
        label='Please Enter Your Email'
    )

    first_name=forms.CharField(initial='Enter Your Name')
    
    # Today date
    day=forms.DateField(initial=datetime.date.today) 


    #1 choice Field
    Send_Star=forms.ChoiceField(choices=Star)

   # Multi choice Field
    Multiple_star=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=Star)



    

    



