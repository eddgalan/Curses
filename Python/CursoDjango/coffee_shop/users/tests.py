from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class RegisterViewTests(TestCase):
    def test_register_page_is_available(self):
        response = self.client.get(reverse("register"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/register.html")

    def test_valid_registration_creates_and_logs_in_user(self):
        response = self.client.post(
            reverse("register"),
            {
                "username": "new_customer",
                "email": "customer@example.com",
                "password1": "A-secure-password-2026",
                "password2": "A-secure-password-2026",
            },
        )

        user = get_user_model().objects.get(username="new_customer")
        self.assertEqual(user.email, "customer@example.com")
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("product_list"))
        self.assertEqual(int(self.client.session["_auth_user_id"]), user.pk)

    def test_password_mismatch_does_not_create_user(self):
        response = self.client.post(
            reverse("register"),
            {
                "username": "new_customer",
                "email": "customer@example.com",
                "password1": "A-secure-password-2026",
                "password2": "a-different-password-2026",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "The two password fields didn’t match")
        self.assertFalse(
            get_user_model().objects.filter(username="new_customer").exists()
        )

    def test_authenticated_user_is_redirected_from_registration(self):
        user = get_user_model().objects.create_user(
            username="customer", password="A-secure-password-2026"
        )
        self.client.force_login(user)

        response = self.client.get(reverse("register"))

        self.assertRedirects(response, reverse("product_list"))


class LogoutViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="customer", password="A-secure-password-2026"
        )
        self.client.force_login(self.user)

    def test_post_logs_out_user_and_redirects_to_products(self):
        response = self.client.post(reverse("logout"))

        self.assertRedirects(response, reverse("product_list"))
        self.assertNotIn("_auth_user_id", self.client.session)

    def test_get_does_not_log_out_user(self):
        response = self.client.get(reverse("logout"))

        self.assertEqual(response.status_code, 405)
        self.assertEqual(int(self.client.session["_auth_user_id"]), self.user.pk)
