# Practicing SQL and database usage

## Creating a toy database

From the command line, let's create a new sqlite3 database named `sdss.db`:
```bash
$ sqlite3 sdss.db
```

This will open a `sqlite>` prompt. Now let's create the tables by running
the following on the sqlite prompt:

```sql
sqlite> CREATE TABLE sources (
    run         INTEGER,
    rerun       INTEGER,
    camcol      INTEGER,
    field       INTEGER,
    obj         INTEGER,
    type        INTEGER,
    ra          REAL,
    dec         REAL,
    psfMag_r    REAL,
    psfMag_g    REAL,
    psfMgErr_r  REAL,
    psfMagErr_g REAL
);

sqlite> CREATE TABLE runs (
    run         INTEGER,
    ra          REAL,
    dec         REAL,
    mjdstart    REAL,
    mjdend      REAL,
    node        REAL,
    inclination REAL,
    mu0    REAL,
    nu0    REAL
);

sqlite> .quit
```

Don't forget the semicolons at the end!

We need to massage the input data a bit before we can load them. In
particular, sqlite won't know how to load data that begin with a header, so
we'll just remove it manually. Do:

```bash
cp runs.txt runs.in
# And then edit runs.in to remove the first line (the header)

cp sample.csv sample.in
# And then edit sample.in to remove the first line
```

Let's go back into sqlite, to do the import:
```sql
sqlite sdss.db

sqlite> .mode csv
sqlite> .separator " "
sqlite> .import runs.in runs
sqlite> .separator ","
sqlite> .import sample.in sources
sqlite> .quit
```

At this point, you have a database with two tables. If you've run this on
your own laptop, you can open and view this database in sqlitebrowser
(sqlitebrowser can't be run remotely on our JupyterHub, unfortunately).

For those on a Mac: The first time you run sqlite browser, you may need to
right-click then select ‘Open’ while holding down the Option key.  This is
to circumvent Mac's security requirement for signed binaries. Note: do not
do this unless you trus the binary; being careful about security is good!

## Practicing basic SQL

Now let's practice some SQL queries:
```sql
SELECT ra, dec, psfMag_r FROM sources
SELECT ra, dec, psfMag_r FROM sources WHERE psfMag_r < 21.5
SELECT ra, dec, psfMag_r FROM sources WHERE psfMag_r < 21.5 LIMIT 5
SELECT COUNT(psfMag_r), AVG(psfMag_r) FROM sources WHERE psfMag_r < 21.5
SELECT COUNT(*), run FROM sources GROUP BY run
SELECT COUNT(*), run FROM sources GROUP BY run ORDER BY run
SELECT COUNT(*) as ct , run FROM sources GROUP BY run ORDER BY ct
```

## Practicing SQL Joins

This query joins the data from two tables (sources and runs):

```sql
SELECT
  sources.ra, sources.dec, sources.run, mjdstart
FROM
  sources JOIN runs ON sources.run = runs.run
```
