from django.test import TestCase


class TestHomeViews(TestCase):

    def test_get_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/includes/home_content_1.html")
        self.assertTemplateUsed(response, "home/includes/home_content_2.html")
        self.assertTemplateUsed(response, "home/includes/home_content_3.html")
        self.assertTemplateUsed(response, "home/includes/home_content_4.html")
        self.assertTemplateUsed(response, "home/includes/home_content_5.html")
        self.assertTemplateUsed(response, "home/includes/home_content_6.html")
        self.assertTemplateUsed(response, "home/includes/adventure_card.html")
