from .models import Ask, Oreview
from django import forms

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Ask
        fields = ['title','email', 'content']
        labels = {
            'title':'제목',
            'email':'이메일주소',
            'content':'내용',
        }

class OreviewForm(forms.ModelForm):
    content = forms.CharField(
                label='리뷰',
                widget=forms.Textarea(
                        attrs={
                            'row': 5,
                            'col': 50,
                            'placeholder': '매장 방문 후기를 자유롭게 작성해 주세요.',
                            'style': 'height:100px'
                        }
                    )
            )
    class Meta:
        model = Oreview
        fields = ['content']

        