Summary:	Encode and decode Quoted-Printable files
Name:		qprint
Version:	1.1
Release:	1
License:	public domain
Group:		Applications/Mail
Source0:	http://www.fourmilab.ch/webtools/qprint/%{name}-%{version}.tar.gz
# Source0-md5:	f33be0ac4e09aadea161f378140007ea
URL:		http://www.fourmilab.ch/webtools/qprint/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Encode and decode Quoted-Printable files.

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/qprint
%{_mandir}/man1/qprint.1*
