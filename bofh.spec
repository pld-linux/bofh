Summary:	Console utility for maintaing user accounts
Summary(pl):	Konsolowe narzêdzie do zarz±dzania kontami u¿ytkowników
Name:		bofh
Version:	0.2
Release:	4
License:	GPL
Group:		Applications/Console
Source0:	ftp://morgoth.uznam.net.pl/bofh/%{name}-%{version}.tar.gz
# Source0-md5:	aa3af230280e36c0dcaf20e87014cd52
Patch0:		%{name}-pl.po_fix.patch
Requires:	dml
Requires:	grep
Requires:	shadow
Requires:	textutils
Requires:	bash
Requires:	gettext
BuildRequires:	gettext-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It is a utility that lets you maintain user accounts easily. Currently
it supports adding, removing and modifying accounts. It has nice,
DML-based interface.

%description -l pl
Jest to narzêdzie, które pozwala na ³atwe zarz±dzanie kontami
u¿ytkowników. Aktualnie pozwala na ich usuwanie, dodawanie oraz
poprawianie. Posiada ³adny, oparty na DMLu interfejs.

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT

# %{_datadir} is intentional here. Everything inside _is_ arch independent
./install.sh DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{_datadir}/bofh \
	sbindir=%{_sbindir} \
	localedir=%{_datadir}/locale

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog TODO CREDITS
%defattr(644,root,root,755)
%{_sysconfdir}/bofh
%attr(755,root,root) %{_sbindir}/bofh
%{_datadir}/bofh
%lang(pl) %{_datadir}/locale/pl/LC_MESSAGES/bofh.mo
