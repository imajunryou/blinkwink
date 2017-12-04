import random

class Category:

    def __init__(self, category, prefix=None, always_use_prefix=False):
        """Creates a string for use in categorical statements

        If a prefix is provided, it will be used when the category
        is called as a primary category.

        If a category is used as a secondary category, the prefix,
        if it exists, is ignored."""
        if always_use_prefix and not prefix:
            raise ValueError("Must have a prefix if always_use_prefix is used")

        if prefix:
            self.primary = "{} {}".format(prefix.lower(), category.lower())
        else:
            self.primary = category.lower()

        if always_use_prefix:
            self.secondary = "{} {}".format(prefix.lower(), category.lower())
        else:
            self.secondary = category.lower()


class CategoricalStatement:

    def __init__(self, first_category, second_category):
        self._fmt = "No format for the Categorical Statement has been made"
        self.first_category = first_category
        self.second_category = second_category

    def __str__(self):
        return self._fmt.format(
            self.first_category.primary,
            self.second_category.secondary
        )


class UniversalAffirmative(CategoricalStatement):

    def __init__(self, first_category, second_category):
        super(UniversalAffirmative, self).__init__(
            first_category,
            second_category
        )
        formats = ["All {} are {}."]
        self._fmt = random.choice(formats)
        self.kind = "Universal Affirmative"


class UniversalNegative(CategoricalStatement):

    def __init__(self, first_category, second_category):
        super(UniversalNegative, self).__init__(
            first_category,
            second_category
        )
        formats = ["No {} are {}."]
        self._fmt = random.choice(formats)
        self.kind = "Universal Negative"


class ParticularAffirmative(CategoricalStatement):
    def __init__(self, first_category, second_category):
        super(ParticularAffirmative, self).__init__(
            first_category,
            second_category
        )
        formats = ["Some {} are {}."]
        self._fmt = random.choice(formats)
        self.kind = "Particular Affirmative"


class ParticularNegative(CategoricalStatement):
    def __init__(self, first_category, second_category):
        super(ParticularNegative, self).__init__(
            first_category,
            second_category
        )
        formats = [
            "Some {} are not {}.",
            "Not all {} are {}."
        ]
        self._fmt = random.choice(formats)
        self.kind = "Particular Negative"
