#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-dbplyr
Version  : 2.1.1
Release  : 46
URL      : https://cran.r-project.org/src/contrib/dbplyr_2.1.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/dbplyr_2.1.1.tar.gz
Summary  : A 'dplyr' Back End for Databases
Group    : Development/Tools
License  : MIT
Requires: R-DBI
Requires: R-R6
Requires: R-RSQLite
Requires: R-assertthat
Requires: R-blob
Requires: R-dplyr
Requires: R-ellipsis
Requires: R-glue
Requires: R-lifecycle
Requires: R-magrittr
Requires: R-purrr
Requires: R-rlang
Requires: R-tibble
Requires: R-tidyselect
Requires: R-vctrs
Requires: R-withr
BuildRequires : R-DBI
BuildRequires : R-R6
BuildRequires : R-RSQLite
BuildRequires : R-assertthat
BuildRequires : R-blob
BuildRequires : R-dplyr
BuildRequires : R-ellipsis
BuildRequires : R-glue
BuildRequires : R-lifecycle
BuildRequires : R-magrittr
BuildRequires : R-purrr
BuildRequires : R-rlang
BuildRequires : R-tibble
BuildRequires : R-tidyselect
BuildRequires : R-vctrs
BuildRequires : R-withr
BuildRequires : buildreq-R

%description
work with remote database tables as if they are in-memory data frames.
    Basic features works with any database that has a 'DBI' back end; more
    advanced features require 'SQL' translation to be provided by the
    package author.

%prep
%setup -q -c -n dbplyr
cd %{_builddir}/dbplyr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1617721469

%install
export SOURCE_DATE_EPOCH=1617721469
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library dbplyr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library dbplyr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library dbplyr
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc dbplyr || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/dbplyr/DESCRIPTION
/usr/lib64/R/library/dbplyr/INDEX
/usr/lib64/R/library/dbplyr/LICENSE
/usr/lib64/R/library/dbplyr/Meta/Rd.rds
/usr/lib64/R/library/dbplyr/Meta/features.rds
/usr/lib64/R/library/dbplyr/Meta/hsearch.rds
/usr/lib64/R/library/dbplyr/Meta/links.rds
/usr/lib64/R/library/dbplyr/Meta/nsInfo.rds
/usr/lib64/R/library/dbplyr/Meta/package.rds
/usr/lib64/R/library/dbplyr/Meta/vignette.rds
/usr/lib64/R/library/dbplyr/NAMESPACE
/usr/lib64/R/library/dbplyr/NEWS.md
/usr/lib64/R/library/dbplyr/R/dbplyr
/usr/lib64/R/library/dbplyr/R/dbplyr.rdb
/usr/lib64/R/library/dbplyr/R/dbplyr.rdx
/usr/lib64/R/library/dbplyr/doc/backend-2.R
/usr/lib64/R/library/dbplyr/doc/backend-2.Rmd
/usr/lib64/R/library/dbplyr/doc/backend-2.html
/usr/lib64/R/library/dbplyr/doc/dbplyr.R
/usr/lib64/R/library/dbplyr/doc/dbplyr.Rmd
/usr/lib64/R/library/dbplyr/doc/dbplyr.html
/usr/lib64/R/library/dbplyr/doc/index.html
/usr/lib64/R/library/dbplyr/doc/new-backend.R
/usr/lib64/R/library/dbplyr/doc/new-backend.Rmd
/usr/lib64/R/library/dbplyr/doc/new-backend.html
/usr/lib64/R/library/dbplyr/doc/reprex.R
/usr/lib64/R/library/dbplyr/doc/reprex.Rmd
/usr/lib64/R/library/dbplyr/doc/reprex.html
/usr/lib64/R/library/dbplyr/doc/sql.R
/usr/lib64/R/library/dbplyr/doc/sql.Rmd
/usr/lib64/R/library/dbplyr/doc/sql.html
/usr/lib64/R/library/dbplyr/doc/translation-function.R
/usr/lib64/R/library/dbplyr/doc/translation-function.Rmd
/usr/lib64/R/library/dbplyr/doc/translation-function.html
/usr/lib64/R/library/dbplyr/doc/translation-verb.R
/usr/lib64/R/library/dbplyr/doc/translation-verb.Rmd
/usr/lib64/R/library/dbplyr/doc/translation-verb.html
/usr/lib64/R/library/dbplyr/help/AnIndex
/usr/lib64/R/library/dbplyr/help/aliases.rds
/usr/lib64/R/library/dbplyr/help/dbplyr.rdb
/usr/lib64/R/library/dbplyr/help/dbplyr.rdx
/usr/lib64/R/library/dbplyr/help/figures/lifecycle-archived.svg
/usr/lib64/R/library/dbplyr/help/figures/lifecycle-defunct.svg
/usr/lib64/R/library/dbplyr/help/figures/lifecycle-deprecated.svg
/usr/lib64/R/library/dbplyr/help/figures/lifecycle-experimental.svg
/usr/lib64/R/library/dbplyr/help/figures/lifecycle-maturing.svg
/usr/lib64/R/library/dbplyr/help/figures/lifecycle-questioning.svg
/usr/lib64/R/library/dbplyr/help/figures/lifecycle-soft-deprecated.svg
/usr/lib64/R/library/dbplyr/help/figures/lifecycle-stable.svg
/usr/lib64/R/library/dbplyr/help/figures/lifecycle-superseded.svg
/usr/lib64/R/library/dbplyr/help/figures/logo.png
/usr/lib64/R/library/dbplyr/help/paths.rds
/usr/lib64/R/library/dbplyr/html/00Index.html
/usr/lib64/R/library/dbplyr/html/R.css
/usr/lib64/R/library/dbplyr/tests/testthat.R
/usr/lib64/R/library/dbplyr/tests/testthat/_snaps/backend-.md
/usr/lib64/R/library/dbplyr/tests/testthat/_snaps/backend-access.md
/usr/lib64/R/library/dbplyr/tests/testthat/_snaps/backend-hana.md
/usr/lib64/R/library/dbplyr/tests/testthat/_snaps/backend-hive.md
/usr/lib64/R/library/dbplyr/tests/testthat/_snaps/backend-impala.md
/usr/lib64/R/library/dbplyr/tests/testthat/_snaps/backend-mssql.md
/usr/lib64/R/library/dbplyr/tests/testthat/_snaps/backend-mysql.md
/usr/lib64/R/library/dbplyr/tests/testthat/_snaps/backend-oracle.md
/usr/lib64/R/library/dbplyr/tests/testthat/_snaps/backend-postgres.md
/usr/lib64/R/library/dbplyr/tests/testthat/_snaps/backend-sqlite.md
/usr/lib64/R/library/dbplyr/tests/testthat/_snaps/backend-teradata.md
/usr/lib64/R/library/dbplyr/tests/testthat/_snaps/escape.md
/usr/lib64/R/library/dbplyr/tests/testthat/_snaps/partial-eval.md
/usr/lib64/R/library/dbplyr/tests/testthat/_snaps/query-join.md
/usr/lib64/R/library/dbplyr/tests/testthat/_snaps/query-select.md
/usr/lib64/R/library/dbplyr/tests/testthat/_snaps/query-semi-join.md
/usr/lib64/R/library/dbplyr/tests/testthat/_snaps/query-set-op.md
/usr/lib64/R/library/dbplyr/tests/testthat/_snaps/schema.md
/usr/lib64/R/library/dbplyr/tests/testthat/_snaps/sql-build.md
/usr/lib64/R/library/dbplyr/tests/testthat/_snaps/tbl-lazy.md
/usr/lib64/R/library/dbplyr/tests/testthat/_snaps/translate-sql-conditional.md
/usr/lib64/R/library/dbplyr/tests/testthat/_snaps/translate-sql-helpers.md
/usr/lib64/R/library/dbplyr/tests/testthat/_snaps/translate-sql-quantile.md
/usr/lib64/R/library/dbplyr/tests/testthat/_snaps/translate-sql-string.md
/usr/lib64/R/library/dbplyr/tests/testthat/_snaps/translate-sql.md
/usr/lib64/R/library/dbplyr/tests/testthat/_snaps/verb-arrange.md
/usr/lib64/R/library/dbplyr/tests/testthat/_snaps/verb-count.md
/usr/lib64/R/library/dbplyr/tests/testthat/_snaps/verb-distinct.md
/usr/lib64/R/library/dbplyr/tests/testthat/_snaps/verb-expand.md
/usr/lib64/R/library/dbplyr/tests/testthat/_snaps/verb-fill.md
/usr/lib64/R/library/dbplyr/tests/testthat/_snaps/verb-joins.md
/usr/lib64/R/library/dbplyr/tests/testthat/_snaps/verb-mutate.md
/usr/lib64/R/library/dbplyr/tests/testthat/_snaps/verb-pivot-longer.md
/usr/lib64/R/library/dbplyr/tests/testthat/_snaps/verb-pivot-wider.md
/usr/lib64/R/library/dbplyr/tests/testthat/_snaps/verb-select.md
/usr/lib64/R/library/dbplyr/tests/testthat/_snaps/verb-slice.md
/usr/lib64/R/library/dbplyr/tests/testthat/_snaps/verb-summarise.md
/usr/lib64/R/library/dbplyr/tests/testthat/_snaps/verb-uncount.md
/usr/lib64/R/library/dbplyr/tests/testthat/helper-src.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-backend-.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-backend-access.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-backend-hana.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-backend-hive.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-backend-impala.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-backend-mssql.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-backend-mysql.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-backend-odbc.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-backend-oracle.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-backend-postgres-old.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-backend-postgres.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-backend-redshift.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-backend-sqlite.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-backend-teradata.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-db-sql.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-escape.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-ident.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-partial-eval.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-query-join.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-query-select.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-query-semi-join.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-query-set-op.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-remote.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-schema.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-sql-build.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-sql-expr.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-sql.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-src_dbi.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-tbl-lazy.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-tbl-sql.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-test-backend-snowflake.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-translate-sql-conditional.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-translate-sql-helpers.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-translate-sql-paste.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-translate-sql-quantile.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-translate-sql-string.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-translate-sql-window.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-translate-sql.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-utils.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-verb-arrange.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-verb-compute.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-verb-copy-to.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-verb-count.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-verb-distinct.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-verb-do.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-verb-expand.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-verb-fill.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-verb-filter.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-verb-group_by.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-verb-head.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-verb-joins.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-verb-mutate.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-verb-pivot-longer.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-verb-pivot-wider.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-verb-pull.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-verb-select.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-verb-set-ops.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-verb-slice.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-verb-summarise.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-verb-uncount.R
