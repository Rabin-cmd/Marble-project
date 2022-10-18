from sqlite3 import NotSupportedError
from django.db import models


class pic(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)
    price = models.IntegerField()
    img = models.ImageField()
    dat = models.DateTimeField()

    def __enter__(self):
        # Some SQLite schema alterations need foreign key constraints to be
        # disabled. Enforce it here for the duration of the schema edition.
        if not self.connection.disable_constraint_checking():
            raise NotSupportedError(
                'SQLite schema editor cannot be used while foreign key '
                'constraint checks are enabled. Make sure to disable them '
                'before entering a transaction.atomic() context because '
                'SQLite3 does not support disabling them in the middle of '
                'a multi-statement transaction.'
            )
        self.connection.cursor().execute('PRAGMA legacy_alter_table = ON')
        return super().__enter__()
