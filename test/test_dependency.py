import unittest

from serum import dependency, singleton


class DependencyTests(unittest.TestCase):
    def test_dependency_decorator_adds_flag(self):
        @dependency
        class Dependency:
            pass
        self.assertTrue(Dependency.__is_dependency__)

    def test_singleton(self):
        @singleton
        class Dependency:
            pass
        self.assertTrue(Dependency.__is_dependency__)
        self.assertTrue(Dependency.__is_singleton__)