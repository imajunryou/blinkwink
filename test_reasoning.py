import unittest

from blinkwink.reasoning import Category, UniversalAffirmative


class TestCategoryBuilder(unittest.TestCase):

    def test_category_builder_primary_without_prefix(self):
        expected = "elephants"
        actual = Category("elephants")
        self.assertEqual(actual.primary, expected)

    def test_category_builder_secondary_without_prefix(self):
        expected = "spiders"
        actual = Category("spiders")
        self.assertEqual(actual.secondary, expected)

    def test_category_builder_primary_with_prefix(self):
        expected_primary = "things that are angry"
        actual = Category("angry", "things that are")
        self.assertEqual(actual.primary, expected_primary)

    def test_category_builder_secondary_with_prefix(self):
        expected_secondary = "angry"
        actual = Category("angry", "things that are")
        self.assertEqual(actual.secondary, expected_secondary)

    def test_category_builder_forces_lower_primary_with_prefix(self):
        cat = Category("HAPPY", "THINGS THAT ARE")
        self.assertEqual(cat.primary, "things that are happy")

    def test_category_builder_forces_lower_primary_without_prefix(self):
        cat = Category("Whales")
        self.assertEqual(cat.primary, "whales")

    def test_category_builder_forces_lower_secondary_with_prefix(self):
        cat = Category("Whales", "Things that are")
        self.assertEqual(cat.secondary, "whales")

    def test_category_builder_forces_lower_secondary_without_prefix(self):
        cat = Category("Whales")
        self.assertEqual(cat.secondary, "whales")


class TestCategoricalStatements(unittest.TestCase):

    def test_universal_affirmative_no_prefixes(self):
        cat1 = Category("Cats")
        cat2 = Category("Animals")
        statement = UniversalAffirmative(cat1, cat2)
        self.assertEqual(str(statement), "All cats are animals.")

    def test_universal_affirmative_first_prefix(self):
        cat1 = Category("Cats", "Things That Are")
        cat2 = Category("Animals")
        statement = UniversalAffirmative(cat1, cat2)
        self.assertEqual(
            str(statement),
            "All things that are cats are animals."
        )

    def test_universal_affirmative_second_prefix(self):
        cat1 = Category("Cats")
        cat2 = Category("Animals", "things that are")
        statement = UniversalAffirmative(cat1, cat2)
        self.assertEqual(str(statement), "All cats are animals.")

    def test_universal_affirmative_both_prefixes(self):
        cat1 = Category("Cats", "things that are")
        cat2 = Category("Animals", "things that are")
        statement = UniversalAffirmative(cat1, cat2)
        self.assertEqual(
            str(statement),
            "All things that are cats are animals."
        )


if __name__ == "__main__":
    unittest.main()
