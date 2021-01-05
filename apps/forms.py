from django import forms
from django.core.mail import EmailMessage

class InquiryForm(forms.Form):
    name=forms.CharField(label="name", max_length=30)
    email=forms.EmailField(label="mail address")
    title=forms.CharField(label="title", max_length=30)
    message=forms.CharField(label="message", widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class']='form-control col-9'
        self.fields['name'].widget.attrs['placeholder']='名前を入力する'
        
        self.fields['email'].widget.attrs['class']='form-control col-11'
        self.fields['email'].widget.attrs['placeholder']='メールアドレスを入力する'
        
        self.fields['title'].widget.attrs['class']='form-control col-11'
        self.fields['title'].widget.attrs['placeholder']='タイトルを入力する'
        
        self.fields['message'].widget.attrs['class']='form-control col-12'
        self.fields['message'].widget.attrs['placeholder']='メッセージを入力する'
        

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        title = self.cleaned_data['title']
        message = self.cleaned_data['message']

        subject = '問い合わせ {}'.format(title)
        message = '送信者 {} \n アドレス {} \n メッセージ {} '.format(name, email, message)

        from_email = 'admin@example.com'
        to_list = [
            'test@example.com'
        ]
        cc_list = [
            email
        ]

        message = EmailMessage(subject=subject, body=message, from_email=from_email, to=to_list,
                    cc=cc_list)
        message.send()
