from django.test import TestCase
from .forms import OrderForm


class TestOrderForm(TestCase):

    def test_create_order_with_required_fields_filled(self):
        form = OrderForm({
            'full_name': 'test test',
            'email': 'test@test.com',
            'phone_number': '123456 111',
            'address_line1': '111 test street',
            'town_or_city': 'test',
            'country': 'HR'})
        self.assertTrue(form.is_valid())

    def test_correct_message_for_empty_form(self):
        form = OrderForm({'form': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['full_name'],
                         [u'This field is required.'])
