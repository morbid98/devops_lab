from unittest import TestCase
import func


class TestPrime(TestCase):

    def test_func1(self):
        self.assertEqual(func.reverse("Something amazing"), "gnihtemoS gnizama")

    def test_func2(self):
        self.assertEqual(func.reverse("Is it even amazing?"), "sI ti neve ?gnizama")
