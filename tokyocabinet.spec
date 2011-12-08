#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries

# TODO:
# warning: Installed (but unpackaged) file(s) found:
#    /usr/lib/tcawmgr.cgi
Summary:	Supreme Database Management Library
Summary(pl.UTF-8):	Supreme Database Management Library
Name:		tokyocabinet
Version:	1.4.47
Release:	1
License:	LGPL v2.1
Group:		Libraries
Source0:	http://fallabs.com/tokyocabinet/%{name}-%{version}.tar.gz
# Source0-md5:	3d94fe2aebf5d9ff0478ed895bc46fc9
URL:		http://fallabs.com/tokyocabinet/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	libtool
BuildRequires:	zlib-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tokyo Cabinet is a library of routines for managing a database. The
database is a simple data file containing records, each is a pair of a
key and a value. Every key and value is serial bytes with variable
length. Both binary data and character string can be used as a key and
a value. There is neither concept of data tables nor data types.
Records are organized in hash table, B+ tree, or fixed-length array.

%package libs
Summary:	Shared library for Tokyo Cabinet
Group:		Libraries
Conflicts:	%{name} < 1.4.47-1

%description libs
Shared library for Tokyo Cabinet.

%package devel
Summary:	Header files for tokyocabinet library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki tokyocabinet
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for tokyocabinet library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki tokyocabinet.

%package static
Summary:	Static tokyocabinet library
Summary(pl.UTF-8):	Statyczna biblioteka tokyocabinet
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static tokyocabinet library.

%description static -l pl.UTF-8
Statyczna biblioteka tokyocabinet.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	%{!?with_static_libs:--disable-static} \
	--enable-off64

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/%{name}/doc
%{__rm} $RPM_BUILD_ROOT%{_datadir}/%{name}/{COPYING,ChangeLog}

install -d $RPM_BUILD_ROOT%{_datadir}/idl/%{name}
mv $RPM_BUILD_ROOT%{_datadir}/{%{name},idl/%{name}}/tokyocabinet.idl

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a example/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/tcamgr
%attr(755,root,root) %{_bindir}/tcbmgr
%attr(755,root,root) %{_bindir}/tcfmgr
%attr(755,root,root) %{_bindir}/tchmgr
%attr(755,root,root) %{_bindir}/tctmgr
%attr(755,root,root) %{_bindir}/tcucodec
%attr(755,root,root) %{_bindir}/*test
%{_mandir}/man1/tc*.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib%{name}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/lib%{name}.so.9

%files devel
%defattr(644,root,root,755)
%doc doc/*
%{_libdir}/libtokyocabinet.so
%{_includedir}/tcadb.h
%{_includedir}/tcbdb.h
%{_includedir}/tcfdb.h
%{_includedir}/tchdb.h
%{_includedir}/tctdb.h
%{_includedir}/tcutil.h
%{_pkgconfigdir}/%{name}.pc
%{_datadir}/idl/%{name}/tokyocabinet.idl
%{_mandir}/man3/*.3*
%{_examplesdir}/%{name}-%{version}

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libtokyocabinet.a
%endif
