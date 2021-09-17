from unittest import TestLoader, TextTestRunner

if __name__ == "__main__":
    loader = TestLoader()
    tests = loader.discover('./convokit/tests/db-storage', top_level_dir='.')
    testRunner = TextTestRunner()
    test_results = testRunner.run(tests)

    if test_results.wasSuccessful():
        exit(0)
    else:
        exit(1)