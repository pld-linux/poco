Summary:	C++ class libraries and frameworks for building network- and internet-based applications
Name:		poco
Version:	1.4.2p1
Release:	0.1
License:	other
Group:		Libraries
Source0:	http://downloads.sourceforge.net/poco/%{name}-%{version}.tar.gz
# Source0-md5:	d4f150b4a4365efccaae3e8263c0e368
URL:		http://pocoproject.org/
#BuildRequires:	-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Modern, powerful open source C++ class libraries and frameworks for building network- and internet-based applications that run on desktop, server and embedded systems.

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
%configure

%{__make} \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	CFLAGS="%{rpmcflags}" \
	CXXFLAGS="%{rpmcxxflags}" \
	LINKFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# if library provides pkgconfig file containing proper {Requires,Libs}.private
# then remove .la pollution
#%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG CONTRIBUTORS README
%if 0
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libFOO.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libFOO.so.N
%{_datadir}/%{name}
%endif

%files devel
%defattr(644,root,root,755)
%if 0
%doc devel-doc/*
%attr(755,root,root) %{_libdir}/libFOO.so
# if no pkgconfig support, or it misses .private deps, then include .la file
#%{_libdir}/libFOO.la
%{_includedir}/foo
%{_aclocaldir}/FOO.m4
%{_pkgconfigdir}/FOO.pc
%endif

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
#%%{_libdir}/libFOO.a
%endif
