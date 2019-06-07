#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-dbplyr
Version  : 1.4.1
Release  : 25
URL      : https://cran.r-project.org/src/contrib/dbplyr_1.4.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/dbplyr_1.4.1.tar.gz
Summary  : A 'dplyr' Back End for Databases
Group    : Development/Tools
License  : MIT
Requires: R-DBI
Requires: R-RSQLite
Requires: R-bit64
Requires: R-blob
Requires: R-dtplyr
Requires: R-memoise
Requires: R-nycflights13
Requires: R-tibble
Requires: R-tidyselect
BuildRequires : R-DBI
BuildRequires : R-RSQLite
BuildRequires : R-bit64
BuildRequires : R-blob
BuildRequires : R-dtplyr
BuildRequires : R-memoise
BuildRequires : R-nycflights13
BuildRequires : R-tibble
BuildRequires : R-tidyselect
BuildRequires : buildreq-R

%description
# dbplyr <img src="man/figures/logo.png" align="right" height="139" />
<!-- badges: start -->

%prep
%setup -q -c -n dbplyr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1559899727

%install
export SOURCE_DATE_EPOCH=1559899727
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
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
export LANG=C
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
/usr/lib64/R/library/dbplyr/help/figures/logo.png
/usr/lib64/R/library/dbplyr/help/paths.rds
/usr/lib64/R/library/dbplyr/html/00Index.html
/usr/lib64/R/library/dbplyr/html/R.css
/usr/lib64/R/library/dbplyr/tests/testthat.R
/usr/lib64/R/library/dbplyr/tests/testthat/helper-src.R
/usr/lib64/R/library/dbplyr/tests/testthat/sql/backend-quantile.sql
/usr/lib64/R/library/dbplyr/tests/testthat/sql/join-on.sql
/usr/lib64/R/library/dbplyr/tests/testthat/sql/join.sql
/usr/lib64/R/library/dbplyr/tests/testthat/sql/mutate-select-collapse.sql
/usr/lib64/R/library/dbplyr/tests/testthat/sql/mutate-select.sql
/usr/lib64/R/library/dbplyr/tests/testthat/sql/mutate-subqueries.sql
/usr/lib64/R/library/dbplyr/tests/testthat/sql/select-collapse.sql
/usr/lib64/R/library/dbplyr/tests/testthat/sql/select-mutate-collapse.sql
/usr/lib64/R/library/dbplyr/tests/testthat/sql/semi-join.sql
/usr/lib64/R/library/dbplyr/tests/testthat/sql/setop.sql
/usr/lib64/R/library/dbplyr/tests/testthat/test-backend-.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-backend-access.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-backend-hive.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-backend-impala.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-backend-mssql.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-backend-mysql.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-backend-odbc.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-backend-oracle.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-backend-postgres.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-backend-sqlite.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-backend-teradata.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-escape.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-explain-sqlite.txt
/usr/lib64/R/library/dbplyr/tests/testthat/test-ident.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-partial-eval.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-query-join-print.txt
/usr/lib64/R/library/dbplyr/tests/testthat/test-query-join.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-query-select-print.txt
/usr/lib64/R/library/dbplyr/tests/testthat/test-query-select.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-query-semi-join-print.txt
/usr/lib64/R/library/dbplyr/tests/testthat/test-query-semi-join.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-query-set-op-print.txt
/usr/lib64/R/library/dbplyr/tests/testthat/test-query-set-op.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-remote.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-sql-build.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-sql-expr.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-sql-translator.txt
/usr/lib64/R/library/dbplyr/tests/testthat/test-sql-variant.txt
/usr/lib64/R/library/dbplyr/tests/testthat/test-sql.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-src_dbi.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-tbl-lazy-print.txt
/usr/lib64/R/library/dbplyr/tests/testthat/test-tbl-lazy.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-tbl-sql.R
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
/usr/lib64/R/library/dbplyr/tests/testthat/test-verb-distinct.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-verb-do.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-verb-filter.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-verb-group_by.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-verb-head.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-verb-joins.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-verb-mutate.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-verb-pull.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-verb-select.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-verb-set-ops.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-verb-summarise.R
