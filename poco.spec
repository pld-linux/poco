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

%{__sed} -i -e 's|$(INSTALLDIR)/lib\b|$(INSTALLDIR)/%{_lib}|g' Makefile
#%{__sed} -i -e 's|ODBCLIBDIR = /usr/lib\b|ODBCLIBDIR = %{_libdir}|g' Data/ODBC/Makefile Data/ODBC/testsuite/Makefile
%{__sed} -i -e 's|flags=""|flags="%{optflags}"|g' configure
%{__sed} -i -e 's|SHAREDOPT_LINK  = -Wl,-rpath,$(LIBPATH)|SHAREDOPT_LINK  =|g' build/config/Linux
%{__sed} -i -e 's|#endif|#define POCO_UNBUNDLED 1\n\n#endif|g' Foundation/include/Poco/Config.h
#%{__sed} -i -e 's|"Poco/zlib.h"|<zlib.h>|g' Zip/src/ZipStream.cpp

%{__rm} Foundation/src/MSG00001.bin
%{__rm} Foundation/include/Poco/zconf.h
%{__rm} Foundation/include/Poco/zlib.h
%{__rm} Foundation/src/adler32.c
%{__rm} Foundation/src/compress.c
%{__rm} Foundation/src/crc32.c
%{__rm} Foundation/src/crc32.h
%{__rm} Foundation/src/deflate.c
%{__rm} Foundation/src/deflate.h
%{__rm} Foundation/src/gzio.c
%{__rm} Foundation/src/infback.c
%{__rm} Foundation/src/inffast.c
%{__rm} Foundation/src/inffast.h
%{__rm} Foundation/src/inffixed.h
%{__rm} Foundation/src/inflate.c
%{__rm} Foundation/src/inflate.h
%{__rm} Foundation/src/inftrees.c
%{__rm} Foundation/src/inftrees.h
%{__rm} Foundation/src/trees.c
%{__rm} Foundation/src/trees.h
%{__rm} Foundation/src/zconf.h
%{__rm} Foundation/src/zlib.h
%{__rm} Foundation/src/zutil.c
%{__rm} Foundation/src/zutil.h
%{__rm} Foundation/src/pcre.h
%{__rm} Foundation/src/pcre_chartables.c
%{__rm} Foundation/src/pcre_compile.c
%{__rm} Foundation/src/pcre_exec.c
%{__rm} Foundation/src/pcre_fullinfo.c
%{__rm} Foundation/src/pcre_globals.c
%{__rm} Foundation/src/pcre_maketables.c
%{__rm} Foundation/src/pcre_newline.c
%{__rm} Foundation/src/pcre_ord2utf8.c
%{__rm} Foundation/src/pcre_study.c
%{__rm} Foundation/src/pcre_try_flipped.c
%{__rm} Foundation/src/pcre_valid_utf8.c
%{__rm} Foundation/src/pcre_xclass.c
#%{__rm} Data/SQLite/src/sqlite3.h
#%{__rm} Data/SQLite/src/sqlite3.c
%{__rm} XML/include/Poco/XML/expat.h
%{__rm} XML/include/Poco/XML/expat_external.h
%{__rm} XML/src/ascii.h
%{__rm} XML/src/asciitab.h
%{__rm} XML/src/expat_config.h
%{__rm} XML/src/iasciitab.h
%{__rm} XML/src/internal.h
%{__rm} XML/src/latin1tab.h
%{__rm} XML/src/nametab.h
%{__rm} XML/src/utf8tab.h
%{__rm} XML/src/xmlparse.cpp
%{__rm} XML/src/xmlrole.c
%{__rm} XML/src/xmlrole.h
%{__rm} XML/src/xmltok.c
%{__rm} XML/src/xmltok.h
%{__rm} XML/src/xmltok_impl.c
%{__rm} XML/src/xmltok_impl.h
%{__rm} XML/src/xmltok_ns.c

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
