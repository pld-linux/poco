# TODO
# - split separate -debug-devel?
#
# Conditional build:
%bcond_without	tests		# build without tests
%bcond_without	samples		# build without tests

Summary:	C++ class libraries and frameworks for building network- and internet-based applications
Name:		poco
Version:	1.6.1
Release:	0.1
License:	Boost
Group:		Libraries
Source0:	http://pocoproject.org/releases/poco-%{version}/%{name}-%{version}-all.tar.gz
# Source0-md5:	05961d10195d0f760b707752e88938e9
Patch0:		pcre.patch
URL:		http://pocoproject.org/
BuildRequires:	expat-devel
BuildRequires:	libiodbc-devel
BuildRequires:	libstdc++-devel
BuildRequires:	mysql-devel
BuildRequires:	openssl-devel
BuildRequires:	pcre-devel
BuildRequires:	sqlite3-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The POCO C++ Libraries (POCO stands for POrtable COmponents) are open
source C++ class libraries that simplify and accelerate the
development of network-centric, portable applications in C++. The POCO
C++ Libraries are built strictly on standard ANSI/ISO C++, including
the standard library.

%package foundation
Summary:	The Foundation POCO component
Group:		Libraries

%description foundation
This package contains the Foundation component of POCO. (POCO is a set
of C++ class libraries for network-centric applications.)

%package xml
Summary:	The XML POCO component
Group:		Libraries

%description xml
This package contains the XML component of POCO. (POCO is a set of C++
class libraries for network-centric applications.)

%package util
Summary:	The Util POCO component
Group:		Libraries

%description util
This package contains the Util component of POCO. (POCO is a set of
C++ class libraries for network-centric applications.)

%package net
Summary:	The Net POCO component
Group:		Libraries

%description net
This package contains the Net component of POCO. (POCO is a set of C++
class libraries for network-centric applications.)

%package crypto
Summary:	The Crypto POCO component
Group:		Libraries

%description crypto
This package contains the Crypto component of POCO. (POCO is a set of
C++ class libraries for network-centric applications.)

%package netssl
Summary:	The NetSSL POCO component
Group:		Libraries

%description netssl
This package contains the NetSSL component of POCO. (POCO is a set of
C++ class libraries for network-centric applications.)

%package data
Summary:	The Data POCO component
Group:		Libraries

%description data
This package contains the Data component of POCO. (POCO is a set of
C++ class libraries for network-centric applications.)

%package sqlite
Summary:	The Data/SQLite POCO component
Group:		Libraries

%description sqlite
This package contains the Data/SQLite component of POCO. (POCO is a
set of C++ class libraries for network-centric applications.)

%package odbc
Summary:	The Data/ODBC POCO component
Group:		Libraries

%description odbc
This package contains the Data/ODBC component of POCO. (POCO is a set
of C++ class libraries for network-centric applications.)

%package mysql
Summary:	The Data/MySQL POCO component
Group:		Libraries

%description mysql
This package contains the Data/MySQL component of POCO. (POCO is a set
of C++ class libraries for network-centric applications.)

%package zip
Summary:	The Zip POCO component
Group:		Libraries

%description zip
This package contains the Zip component of POCO. (POCO is a set of C++
class libraries for network-centric applications.)

%package devel
Summary:	Headers for developing programs that will use POCO
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki POCO C++
Group:		Development/Libraries
Requires:	%{name}-crypto = %{version}-%{release}
Requires:	%{name}-data = %{version}-%{release}
Requires:	%{name}-debug = %{version}-%{release}
Requires:	%{name}-foundation = %{version}-%{release}
Requires:	%{name}-mysql = %{version}-%{release}
Requires:	%{name}-net = %{version}-%{release}
Requires:	%{name}-netssl = %{version}-%{release}
Requires:	%{name}-odbc = %{version}-%{release}
Requires:	%{name}-pagecompiler = %{version}-%{release}
Requires:	%{name}-sqlite = %{version}-%{release}
Requires:	%{name}-util = %{version}-%{release}
Requires:	%{name}-xml = %{version}-%{release}
Requires:	%{name}-zip = %{version}-%{release}
Requires:	expat-devel
Requires:	zlib-devel

%description devel
The POCO C++ Libraries (POCO stands for POrtable COmponents) are open
source C++ class libraries that simplify and accelerate the
development of network-centric, portable applications in C++. The POCO
C++ Libraries are built strictly on standard ANSI/ISO C++, including
the standard library.

This package contains the header files needed for developing POCO
applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki POCO C++.

%package static
Summary:	Static POCO C++ library
Summary(pl.UTF-8):	Statyczna biblioteka POCO C++
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static POCO C++ libraries.

%description static -l pl.UTF-8
Statyczna biblioteka POCO C++.

%package pagecompiler
Summary:	The PageCompiler POCO component
Group:		Libraries

%description pagecompiler
This package contains the PageCompiler component of POCO. (POCO is a
set of C++ class libraries for network-centric applications.)

%package debug
Summary:	Debug builds of the POCO libraries
Group:		Development/Libraries

%description debug
This package contains the debug builds of the POCO libraries for
application testing purposes.

%prep
%setup -q -n %{name}-%{version}-all
%patch0 -p1

%{__sed} -i -e 's|$(INSTALLDIR)/lib\b|$(INSTALLDIR)/%{_lib}|g' Makefile
%{__sed} -i -e 's|ODBCLIBDIR = /usr/lib\b|ODBCLIBDIR = %{_libdir}|g' Data/ODBC/Makefile Data/ODBC/testsuite/Makefile
%{__sed} -i -e 's|flags=""|flags="%{optflags}"|g' configure
%{__sed} -i -e 's|SHAREDOPT_LINK  = -Wl,-rpath,$(LIBPATH)|SHAREDOPT_LINK  =|g' build/config/Linux
%{__sed} -i -e 's|#endif|#define POCO_UNBUNDLED 1\n\n#endif|g' Foundation/include/Poco/Config.h
%{__sed} -i -e 's|"Poco/zlib.h"|<zlib.h>|g' Zip/src/ZipStream.cpp

# the file lists came from Foundation/CMakeLists.txt

%{__rm} Foundation/src/MSG00001.bin
%{__rm} Foundation/include/Poco/zconf.h
%{__rm} Foundation/include/Poco/zlib.h
%{__rm} Foundation/src/adler32.c
%{__rm} Foundation/src/compress.c
%{__rm} Foundation/src/crc32.c
%{__rm} Foundation/src/crc32.h
%{__rm} Foundation/src/deflate.c
%{__rm} Foundation/src/deflate.h
#%{__rm} Foundation/src/gzio.c
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

# Foundation/src/pcre* with manual overview
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
%{__rm} Foundation/src/pcre_valid_utf8.c
%{__rm} Foundation/src/pcre_xclass.c
%{__rm} Foundation/src/pcre_byte_order.c
%{__rm} Foundation/src/pcre_config.c
%{__rm} Foundation/src/pcre_config.h
%{__rm} Foundation/src/pcre_dfa_exec.c
%{__rm} Foundation/src/pcre_get.c
%{__rm} Foundation/src/pcre_internal.h
%{__rm} Foundation/src/pcre_jit_compile.c
%{__rm} Foundation/src/pcre_refcount.c
%{__rm} Foundation/src/pcre_string_utils.c
%{__rm} Foundation/src/pcre_tables.c
%{__rm} Foundation/src/pcre_ucd.c
%{__rm} Foundation/src/pcre_version.c

%{__rm} Data/SQLite/src/sqlite3.h
%{__rm} Data/SQLite/src/sqlite3.c

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

# cleanup, makes easier to dig trough bbuild system
find -regextype posix-extended -regex '.*\.(vc.?proj|sln|progen|cmd)' | xargs -r rm -v

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
%{__make} -j1 poco \
	DEFAULT_TARGET=all_release \
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

%post	foundation -p /sbin/ldconfig
%postun	foundation -p /sbin/ldconfig

%post	xml -p /sbin/ldconfig
%postun	xml -p /sbin/ldconfig

%post	util -p /sbin/ldconfig
%postun	util -p /sbin/ldconfig

%post	net -p /sbin/ldconfig
%postun	net -p /sbin/ldconfig

%post	crypto -p /sbin/ldconfig
%postun	crypto -p /sbin/ldconfig

%post	netssl -p /sbin/ldconfig
%postun	netssl -p /sbin/ldconfig

%post	data -p /sbin/ldconfig
%postun	data -p /sbin/ldconfig

%post	sqlite -p /sbin/ldconfig
%postun	sqlite -p /sbin/ldconfig

%post	odbc -p /sbin/ldconfig
%postun	odbc -p /sbin/ldconfig

%post	mysql -p /sbin/ldconfig
%postun	mysql -p /sbin/ldconfig

%post	zip -p /sbin/ldconfig
%postun	zip -p /sbin/ldconfig

%post	debug -p /sbin/ldconfig
%postun	debug -p /sbin/ldconfig

%files
%defattr(644,root,root,755)

%files foundation
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libPocoFoundation.so.17

%files xml
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libPocoXML.so.17

%files util
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libPocoUtil.so.17

%files net
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libPocoNet.so.17

%files crypto
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libPocoCrypto.so.17

%files netssl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libPocoNetSSL.so.17

%files data
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libPocoData.so.17

%files sqlite
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libPocoDataSQLite.so.17

%files odbc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libPocoDataODBC.so.17

%files mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libPocoDataMySQL.so.17

%files zip
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libPocoZip.so.17

%files pagecompiler
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cpspc
%attr(755,root,root) %{_bindir}/f2cpsp

%files debug
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cpspcd
%attr(755,root,root) %{_bindir}/f2cpspd
%attr(755,root,root) %{_libdir}/libPocoCryptod.so.17
%attr(755,root,root) %{_libdir}/libPocoDataMySQLd.so.17
%attr(755,root,root) %{_libdir}/libPocoDataODBCd.so.17
%attr(755,root,root) %{_libdir}/libPocoDataSQLited.so.17
%attr(755,root,root) %{_libdir}/libPocoDatad.so.17
%attr(755,root,root) %{_libdir}/libPocoFoundationd.so.17
%attr(755,root,root) %{_libdir}/libPocoNetSSLd.so.17
%attr(755,root,root) %{_libdir}/libPocoNetd.so.17
%attr(755,root,root) %{_libdir}/libPocoUtild.so.17
%attr(755,root,root) %{_libdir}/libPocoXMLd.so.17
%attr(755,root,root) %{_libdir}/libPocoZipd.so.17

%files devel
%defattr(644,root,root,755)
%doc README NEWS LICENSE CONTRIBUTORS CHANGELOG doc/*
%{_libdir}/libPocoCrypto.so
%{_libdir}/libPocoCryptod.so
%{_libdir}/libPocoData.so
%{_libdir}/libPocoDataMySQL.so
%{_libdir}/libPocoDataMySQLd.so
%{_libdir}/libPocoDataODBC.so
%{_libdir}/libPocoDataODBCd.so
%{_libdir}/libPocoDataSQLite.so
%{_libdir}/libPocoDataSQLited.so
%{_libdir}/libPocoDatad.so
%{_libdir}/libPocoFoundation.so
%{_libdir}/libPocoFoundationd.so
%{_libdir}/libPocoNet.so
%{_libdir}/libPocoNetSSL.so
%{_libdir}/libPocoNetSSLd.so
%{_libdir}/libPocoNetd.so
%{_libdir}/libPocoUtil.so
%{_libdir}/libPocoUtild.so
%{_libdir}/libPocoXML.so
%{_libdir}/libPocoXMLd.so
%{_libdir}/libPocoZip.so
%{_libdir}/libPocoZipd.so
%{_includedir}/Poco
