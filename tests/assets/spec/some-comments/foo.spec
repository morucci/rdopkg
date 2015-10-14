Name:             foo
Epoch:            1
Version:          1.2.3
Release:          42%{?dist}
Summary:          Some package, dude

Group:            Development/Languages
License:          ASL 2.0
URL:              http://pypi.python.org/pypi/%{name}
Source0:          http://pypi.python.org/packages/source/f/%{name}/%{name}-%{version}.tar.gz

# wololo
# before
Patch0001: 0001-something.patch
# one line
Patch0002: 0002-something-else.patch
# two
# lines
Patch0003: 0003-it-doesn-even-exist.patch
Patch0004: 0004-it-doesn-even-exist.patch
Patch0005: 0005-it-doesn-even-exist.patch
#
Patch0006: 0006-it-doesn-even-exist.patch
# after
# ajooo


BuildArch:        noarch
BuildRequires:    python-setuptools
BuildRequires:    python2-devel

Requires:         python-argparse
Requires:         python-iso8601
Requires:         python-prettytable

%description
This is foo! This is foo! This is foo! This is foo! This is foo! This is foo!
This is foo! This is foo! This is foo! 

%prep
%setup -q

# wololo
# before
%patch0001 -p1
# one line
%patch0002 -p1
# two
# lines
%patch0003 -p1
%patch0004 -p1
%patch0005 -p1
#
%patch0006 -p1
# after
# ajooo

# We provide version like this in order to remove runtime dep on pbr.
sed -i s/REDHATNOVACLIENTVERSION/%{version}/ novaclient/__init__.py

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}


%files
%doc README.rst
%{_bindir}/foo

%changelog
* Mon Apr 07 2014 Jakub Ruzicka <jruzicka@redhat.com> 1.2.3-42
- Update to upstream 1.2.3

* Tue Mar 25 2014 Jakub Ruzicka <jruzicka@redhat.com> 1.2.2-1
- Update to upstream 1.2.2