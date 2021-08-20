from django import forms
from django.core.cache import cache
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from stores.models import CartItems, Addresses


class CartUpdateForm(forms.ModelForm):
    quantity = forms.IntegerField(label='Quantity', min_value=1)
    id = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = CartItems
        fields = ['quantity', 'id']

    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get('quantity')
        id = cleaned_data.get('id')

        cart_item = get_object_or_404(CartItems, pk=id)
        if quantity > cart_item.product.stock:
            raise ValidationError(f'Quantity is over! Please less than {cart_item.product.stock}')


class AddressInputForm(forms.ModelForm):
    address = forms.CharField(label='Address', widget=forms.TextInput(attrs={'size': '80'}))

    class Meta:
        model = Addresses
        fields = ['zip_code', 'prefecture', 'address']
        labels = {
            'zip_code': 'Zip code',
            'prefecture': 'Prefecture',
        }

    def save(self):
        address = super().save(commit=False)
        address.user = self.user
        try:
            # uniqueエラーが発生した場合、ValidationErrorを発生させる
            address.validate_unique()
            address.save()
        except ValidationError as e:
            address = get_object_or_404(
                Addresses,
                user=self.user,
                prefecture=address.prefecture,
                zip_code=address.zip_code,
                address=address.address,
            )
            pass

        # キャッシュに保存
        cache.set(f'address_user_{self.user.id}', address)

        return address
