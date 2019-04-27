#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-dbplyr
Version  : 1.3.0
Release  : 23
URL      : https://cran.r-project.org/src/contrib/dbplyr_1.3.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/dbplyr_1.3.0.tar.gz
Summary  : A 'dplyr' Back End for Databases
Group    : Development/Tools
License  : MIT
BuildRequires : R-DBI
BuildRequires : R-RSQLite
BuildRequires : R-bit64
BuildRequires : R-blob
BuildRequires : R-memoise
BuildRequires : R-mime
BuildRequires : R-nycflights13
BuildRequires : R-pkgconfig
BuildRequires : R-purrr
BuildRequires : R-tibble
BuildRequires : R-tidyselect
BuildRequires : R-utf8
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
export SOURCE_DATE_EPOCH=1552907653

%install
export SOURCE_DATE_EPOCH=1552907653
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
R CMD check --no-manual --no-examples --no-codoc  dbplyr || :


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
/usr/lib64/R/library/dbplyr/doc/sql-translation.R
/usr/lib64/R/library/dbplyr/doc/sql-translation.Rmd
/usr/lib64/R/library/dbplyr/doc/sql-translation.html
/usr/lib64/R/library/dbplyr/help/AnIndex
/usr/lib64/R/library/dbplyr/help/aliases.rds
/usr/lib64/R/library/dbplyr/help/dbplyr.rdb
/usr/lib64/R/library/dbplyr/help/dbplyr.rdx
/usr/lib64/R/library/dbplyr/help/figures/logo.png
/usr/lib64/R/library/dbplyr/help/paths.rds
/usr/lib64/R/library/dbplyr/html/00Index.html
/usr/lib64/R/library/dbplyr/html/R.css
/usr/lib64/R/library/dbplyr/tests/testthat.R
/usr/lib64/R/library/dbplyr/tests/testthat/explain-sqlite.txt
/usr/lib64/R/library/dbplyr/tests/testthat/helper-output.R
/usr/lib64/R/library/dbplyr/tests/testthat/helper-src.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-arrange.r
/usr/lib64/R/library/dbplyr/tests/testthat/test-collect.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-colwise.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-compute.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-copy_to.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-distinct.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-do.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-escape.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-explain.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-filter.r
/usr/lib64/R/library/dbplyr/tests/testthat/test-group-by.r
/usr/lib64/R/library/dbplyr/tests/testthat/test-group-size.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-ident.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-joins-consistent.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-joins.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-lazy-ops.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-mutate.r
/usr/lib64/R/library/dbplyr/tests/testthat/test-output.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-partial_eval.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-pull.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-remote.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-schema.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-select.r
/usr/lib64/R/library/dbplyr/tests/testthat/test-sets.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-sql-build.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-sql-escape.r
/usr/lib64/R/library/dbplyr/tests/testthat/test-sql-expr.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-sql-optimise.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-sql-query-select.txt
/usr/lib64/R/library/dbplyr/tests/testthat/test-sql-query.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-sql-render.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-sql-translator.txt
/usr/lib64/R/library/dbplyr/tests/testthat/test-sql-variant.txt
/usr/lib64/R/library/dbplyr/tests/testthat/test-src_dbi.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-summarise.r
/usr/lib64/R/library/dbplyr/tests/testthat/test-tbl-sql.r
/usr/lib64/R/library/dbplyr/tests/testthat/test-translate-MySQL.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-translate-access.r
/usr/lib64/R/library/dbplyr/tests/testthat/test-translate-hive.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-translate-impala.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-translate-literals.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-translate-math.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-translate-mssql.r
/usr/lib64/R/library/dbplyr/tests/testthat/test-translate-odbc.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-translate-oracle.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-translate-postgresql.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-translate-sql-helpers.r
/usr/lib64/R/library/dbplyr/tests/testthat/test-translate-sql-paste.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-translate-sql-window.r
/usr/lib64/R/library/dbplyr/tests/testthat/test-translate-sqlite.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-translate-teradata.r
/usr/lib64/R/library/dbplyr/tests/testthat/test-translate-vectorised.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-translate-window.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-translate.r
/usr/lib64/R/library/dbplyr/tests/testthat/test-utils.R
/usr/lib64/R/library/dbplyr/tests/testthat/test-win_over.R
