Summary:	Console utility for maintaing user accounts
Summary(pl):	Konsolowe narzêdzie do zarz±dzania kontami u¿ytkowników
Name:		bofh
Version:	0.2
Release:	2
License:	GPL
Group:		Applications/Console
Source0:	ftp://morgoth.uznam.net.pl/bofh/%{name}-%{version}.tar.gz
Requires:	dml
Requires:	grep
Requires:	shadow
Requires:	textutils
Requires:	bash
BuildRequires:	gettext
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It is a utility that lets you maintain user accounts easily. Currently
it supports adding, removing and modyfing accounts. It has nice,
DML-based interface.

%description -l pl
Jest to narzêdzie, które pozwala na ³atwe zarz±dzanie kontami
u¿ytkowników. Aktualnie pozwala na ich usuwanie, dodawanie oraz
poprawianie. Posiada ³adny, oparty na DMLu interfejs.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

./install.sh DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{_libdir}/bofh \
	sbindir=%{_sbindir} \
	localedir=%{_datadir}/locale

gzip -9nf README ChangeLog TODO CREDITS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%defattr(644,root,root,755)
%{_sysconfdir}/bofh
%attr(755,root,root) %{_sbindir}/bofh
%{_libdir}/bofh
%lang(pl) %{_datadir}/locale/pl/LC_MESSAGES/bofh.mo
