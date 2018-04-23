#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-dbplyr
Version  : 1.2.1
Release  : 5
URL      : https://cran.r-project.org/src/contrib/dbplyr_1.2.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/dbplyr_1.2.1.tar.gz
Summary  : A 'dplyr' Back End for Databases
Group    : Development/Tools
License  : MIT
Requires: R-DBI
Requires: R-RSQLite
Requires: R-assertthat
Requires: R-cli
Requires: R-nycflights13
Requires: R-tibble
Requires: R-tidyselect
Requires: R-utf8
BuildRequires : R-DBI
BuildRequires : R-RSQLite
BuildRequires : R-assertthat
BuildRequires : R-cli
BuildRequires : R-nycflights13
BuildRequires : R-tibble
BuildRequires : R-tidyselect
BuildRequires : R-utf8
BuildRequires : clr-R-helpers

%description
remote database tables as if they are in-memory data frames. Basic features
    works with any database that has a 'DBI' back end; more advanced features 
    require 'SQL' translation to be provided by the package author.

%prep
%setup -q -c -n dbplyr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523298645

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1523298645
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
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library dbplyr|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


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
