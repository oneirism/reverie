#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "reverie.settings.dev")

    is_testing = 'test' in sys.argv
    if is_testing:
        import coverage
        cov = coverage.coverage(
            source=['campaign', 'reverie'],
            omit=['*/tests/*']
        )
        cov.erase()
        cov.start()

    try:
        from django.core.management import execute_from_command_line

    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            from django.core.management import execute_from_command_line
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)

    if is_testing:
        cov.stop()
        cov.save()
        cov.html_report()
        cov.report()
