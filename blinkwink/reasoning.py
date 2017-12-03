class Category:

    def __init__(self, category, prefix=None):
        if prefix:
            self.primary = "{} {}".format(prefix.lower(), category.lower())
        else:
            self.primary = category.lower()

        self.secondary = category.lower()


class UniversalAffirmative:

    def __init__(self, first_category, second_category):
        self.first_category = first_category
        self.second_category = second_category

    def __str__(self):
        return "All {} are {}.".format(
            self.first_category.primary,
            self.second_category.secondary
        )
