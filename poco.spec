#
# Conditional build:
%bcond_without	tests		# build without tests
%bcond_without	samples		# build without tests

Summary:	C++ class libraries and frameworks for building network- and internet-based applications
Name:		poco
Version:	1.4.2p1
Release:	0.1
License:	other
Group:		Libraries
Source0:	http://downloads.sourceforge.net/poco/%{name}-%{version}.tar.gz
# Source0-md5:	d4f150b4a4365efccaae3e8263c0e368
URL:		http://pocoproject.org/
BuildRequires:	expat-devel
BuildRequires:	libiodbc-devel
BuildRequires:	mysql-devel
BuildRequires:	openssl-devel
BuildRequires:	pcre-devel
BuildRequires:	sqlite3-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Modern, powerful open source C++ class libraries and frameworks for
building network- and internet-based applications that run on desktop,
server and embedded systems.

%package devel
Summary:	Header files for FOO library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki FOO
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for poco library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki poco.

%package static
Summary:	Static poco library
Summary(pl.UTF-8):	Statyczna biblioteka poco
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static poco library.

%description static -l pl.UTF-8
Statyczna biblioteka poco.

%prep
%setup -q

%build
# NOTE: not autoconf based configure
./configure \
	--prefix=%{_prefix} \
	--unbundled \
	%{!?with_tests:--no-tests} \
	%{!?with_samples:--no-samples} \
	--include-path=%{_includedir}/libiodbc \
	--library-path=%{_libdir}/mysql

# POCO_BASE needs to be absolute real path (symlinks confuse it)
%{__make} -j1 \
	POCO_BASE=$(readlink -f $(pwd)) \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	CFLAGS="%{rpmcflags}" \
	CXXFLAGS="%{rpmcxxflags}" \
	LINKFLAGS="%{rpmldflags}"
	STRIP=/bin/true

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	POCO_BASE=$(readlink -f $(pwd)) \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG CONTRIBUTORS README
%attr(755,root,root) %{_libdir}/libPocoFoundation.so.11
%attr(755,root,root) %{_libdir}/libPocoFoundationd.so.11
%attr(755,root,root) %{_libdir}/libPocoNet.so.11
%attr(755,root,root) %{_libdir}/libPocoNetd.so.11
%attr(755,root,root) %{_libdir}/libPocoUtil.so.11
%attr(755,root,root) %{_libdir}/libPocoUtild.so.11
%attr(755,root,root) %{_libdir}/libPocoXML.so.11
%attr(755,root,root) %{_libdir}/libPocoXMLd.so.11

%files devel
%defattr(644,root,root,755)
%{_libdir}/libPocoFoundation.so
%{_libdir}/libPocoFoundationd.so
%{_libdir}/libPocoNet.so
%{_libdir}/libPocoNetd.so
%{_libdir}/libPocoUtil.so
%{_libdir}/libPocoUtild.so
%{_libdir}/libPocoXML.so
%{_libdir}/libPocoXMLd.so
%{_includedir}/Poco
