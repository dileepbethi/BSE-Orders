"""
OrderIQ Database Migration Runner
Version: 1.0

Runs all database migrations.
"""

import sqlite3
from pathlib import Path
import importlib.util


DATABASE_FILE = Path("database") / "bse_orders.db"
MIGRATIONS_FOLDER = Path("database") / "migrations"


def run_migrations():

    connection = sqlite3.connect(DATABASE_FILE)

    migration_files = sorted(MIGRATIONS_FOLDER.glob("*.py"))
    print("Migration Folder:", MIGRATIONS_FOLDER.resolve())
    print("Files Found:", migration_files)

    print("=" * 50)
    print("OrderIQ Migration Runner")
    print("=" * 50)

    for migration in migration_files:

        print(f"Running {migration.name}")

        spec = importlib.util.spec_from_file_location(
            migration.stem,
            migration
        )

        module = importlib.util.module_from_spec(spec)

        spec.loader.exec_module(module)

        module.upgrade(connection)

    connection.commit()

    connection.close()

    print("=" * 50)
    print("All migrations completed successfully.")
    print("=" * 50)


if __name__ == "__main__":

    run_migrations()