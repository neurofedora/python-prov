%global modname prov

Name:           python-%{modname}
Version:        1.4.0
Release:        1%{?dist}
Summary:        W3C Provenance Data Model supporting PROV-JSON and PROV-XML import/export

License:        MIT
URL:            https://pypi.python.org/pypi/prov
Source0:        https://github.com/trungdong/prov/archive/%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%description
A library for W3C Provenance Data Model supporting PROV-JSON and PROV-XML
import/export.

%package -n python2-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{modname}}
BuildRequires:  python2-devel python2-setuptools
BuildRequires:  python2-six
BuildRequires:  python-lxml
BuildRequires:  python-networkx-core
BuildRequires:  python2-pydotplus
Requires:       python2-six
Requires:       python-lxml
Requires:       python-networkx-core
Requires:       python2-pydotplus

%description -n python2-%{modname}
A library for W3C Provenance Data Model supporting PROV-JSON and PROV-XML
import/export.

Python 2 version.

%package -n python3-%{modname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel python3-setuptools
BuildRequires:  python3-six
BuildRequires:  python3-lxml
BuildRequires:  python3-networkx-core
BuildRequires:  python3-pydotplus
Requires:       python3-six
Requires:       python3-lxml
Requires:       python3-networkx-core
Requires:       python3-pydotplus

%description -n python3-%{modname}
A library for W3C Provenance Data Model supporting PROV-JSON and PROV-XML
import/export.

Python 3 version.

%prep
%autosetup -n %{modname}-%{version}

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

sed -i -e '1s|^#!.*$|#!%{__python3}|' %{buildroot}%{_bindir}/*

%check
%{__python2} setup.py test
%{__python2} setup.py test

%files -n python2-%{modname}
%license LICENSE
%doc AUTHORS.rst HISTORY.rst README.rst
%{python2_sitelib}/%{modname}*

%files -n python3-%{modname}
%license LICENSE
%doc AUTHORS.rst HISTORY.rst README.rst
%{_bindir}/%{modname}-*
%{python3_sitelib}/%{modname}*

%changelog
* Sun Dec 06 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.4.0-1
- Initial package
