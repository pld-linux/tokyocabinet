Summary:	Supreme Database Management Library
Summary(pl.UTF-8):	Supreme Database Management Library
Name:		tokyocabinet
Version:	1.4.33
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://1978th.net/tokyocabinet/%{name}-%{version}.tar.gz
# Source0-md5:	d81c3b04921d189f843c64d56b81a8d4
URL:		http://1978th.net/tokyocabinet/
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tokyo Cabinet is a library of routines for managing a database. The
database is a simple data file containing records, each is a pair of a
key and a value. Every key and value is serial bytes with variable
length. Both binary data and character string can be used as a key and
a value. There is neither concept of data tables nor data types.
Records are organized in hash table, B+ tree, or fixed-length array.

%package devel
Summary:	Header files for tokyocabinet library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki tokyocabinet
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

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
	--enable-off64

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/tc*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_datadir}/%{name}
%{_mandir}/man1/tc*.1*

%files devel
%defattr(644,root,root,755)
%doc doc/*
%{_libdir}/lib*.so
%{_includedir}/tc*.h
%{_pkgconfigdir}/*.pc
%{_mandir}/man3/*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
