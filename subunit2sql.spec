#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : subunit2sql
Version  : 1.10.0
Release  : 3
URL      : https://files.pythonhosted.org/packages/4a/15/ea60dce3714edf9f57770178673b189e0829b9600c465ab4ba445c42ca61/subunit2sql-1.10.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/4a/15/ea60dce3714edf9f57770178673b189e0829b9600c465ab4ba445c42ca61/subunit2sql-1.10.0.tar.gz
Summary  : Command to Read a subunit file or stream and put the data in a SQL DB
Group    : Development/Tools
License  : Apache-2.0
Requires: subunit2sql-bin = %{version}-%{release}
Requires: subunit2sql-license = %{version}-%{release}
Requires: subunit2sql-python = %{version}-%{release}
Requires: subunit2sql-python3 = %{version}-%{release}
Requires: SQLAlchemy
Requires: alembic
Requires: matplotlib
Requires: oslo.config
Requires: oslo.db
Requires: pandas
Requires: pbr
Requires: python-dateutil
Requires: python-subunit
Requires: six
Requires: stevedore
BuildRequires : buildreq-distutils3
BuildRequires : pbr

%description
subunit2SQL README
        ==================
        
        subunit2SQL is a tool for storing test results data in a SQL database. Like
        it's name implies it was originally designed around converting `subunit`_
        streams to data in a SQL database and the packaged utilities assume a subunit
        stream as the input format. However, the data model used for the DB does not
        preclude using any test result format. Additionally the analysis tooling built
        on top of a database is data format agnostic. However if you choose to use a
        different result format as an input for the database additional tooling using
        the DB api would need to be created to parse a different test result output
        format. It's also worth pointing out that subunit has several language library
        bindings available. So as a user you could create a small filter to convert a
        different format to subunit. Creating a filter should be fairly easy and then

%package bin
Summary: bin components for the subunit2sql package.
Group: Binaries
Requires: subunit2sql-license = %{version}-%{release}

%description bin
bin components for the subunit2sql package.


%package license
Summary: license components for the subunit2sql package.
Group: Default

%description license
license components for the subunit2sql package.


%package python
Summary: python components for the subunit2sql package.
Group: Default
Requires: subunit2sql-python3 = %{version}-%{release}

%description python
python components for the subunit2sql package.


%package python3
Summary: python3 components for the subunit2sql package.
Group: Default
Requires: python3-core

%description python3
python3 components for the subunit2sql package.


%prep
%setup -q -n subunit2sql-1.10.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541279717
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/subunit2sql
cp LICENSE %{buildroot}/usr/share/package-licenses/subunit2sql/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sql2subunit
/usr/bin/subunit2sql
/usr/bin/subunit2sql-db-manage
/usr/bin/subunit2sql-graph

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/subunit2sql/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
