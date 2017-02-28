** What it does
- adds instruction to sql file to not check foreign keys and other checks (speeds up import)
- removes information about charset and collate (no errors during import)

** How to use
- navigate to directory where database.sql is
- run `[path to fixdbdump directory]/fixdbdump.py`

** Requairments
- python
