# Form for uploading images

from django import forms
from .models import Images

class ImageForm(forms.ModelForm):
    COLORS_CHOICES = [
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('yellow', 'Yellow'),
        ('orange', 'Orange'),
        ('pink', 'Pink'),
        ('purple', 'Purple')
    ]

    name = forms.CharField(max_length=100, required=True)
    favorite_colors = forms.MultipleChoiceField(choices=COLORS_CHOICES, widget=forms.CheckboxSelectMultiple)
    favorite_songs = forms.CharField(widget=forms.Textarea, required=False)
    image = forms.ImageField(required=True)  # Set required to True for mandatory field

    class Meta:
        model = Images
        fields = ['name', 'favorite_colors', 'favorite_songs', 'image']

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if not image:
            raise forms.ValidationError("Image is required.")
        if image.size > 1024 * 1024:  # 1MB limit
            raise forms.ValidationError("The image size should not exceed 1MB.")
        return image
    


