#
# Conditional build:
%bcond_without	tests		# build without tests
%bcond_without	samples		# build without tests

Summary:	C++ class libraries and frameworks for building network- and internet-based applications
Name:		poco
Version:	1.4.7p1
Release:	0.1
License:	Boost
Group:		Libraries
Source0:	http://pocoproject.org/releases/poco-1.4.7/%{name}-%{version}-all.tar.gz
# Source0-md5:	12551b729456c985cffd14e977526c01
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
Modern, powerful open source C++ class libraries and frameworks for
building network- and internet-based applications that run on desktop,
server and embedded systems.

%package devel
Summary:	Header files for POCO C++ libraries
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki POCO C++
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for POCO C++ libraries.

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

%prep
%setup -q -n %{name}-%{version}-all
%patch0 -p1

%{__sed} -i -e 's|$(INSTALLDIR)/lib\b|$(INSTALLDIR)/%{_lib}|g' Makefile
%{__sed} -i -e 's|ODBCLIBDIR = /usr/lib\b|ODBCLIBDIR = %{_libdir}|g' Data/ODBC/Makefile Data/ODBC/testsuite/Makefile
%{__sed} -i -e 's|flags=""|flags="%{optflags}"|g' configure
%{__sed} -i -e 's|SHAREDOPT_LINK  = -Wl,-rpath,$(LIBPATH)|SHAREDOPT_LINK  =|g' build/config/Linux
%{__sed} -i -e 's|#endif|#define POCO_UNBUNDLED 1\n\n#endif|g' Foundation/include/Poco/Config.h
%{__sed} -i -e 's|"Poco/zlib.h"|<zlib.h>|g' Zip/src/ZipStream.cpp

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
%attr(755,root,root) %{_bindir}/cpspc
%attr(755,root,root) %{_bindir}/cpspcd
%attr(755,root,root) %{_bindir}/f2cpsp
%attr(755,root,root) %{_bindir}/f2cpspd
%attr(755,root,root) %{_libdir}/libPocoCrypto.so.17
%attr(755,root,root) %{_libdir}/libPocoCryptod.so.17
%attr(755,root,root) %{_libdir}/libPocoData.so.17
%attr(755,root,root) %{_libdir}/libPocoDataMySQL.so.17
%attr(755,root,root) %{_libdir}/libPocoDataMySQLd.so.17
%attr(755,root,root) %{_libdir}/libPocoDataODBC.so.17
%attr(755,root,root) %{_libdir}/libPocoDataODBCd.so.17
%attr(755,root,root) %{_libdir}/libPocoDataSQLite.so.17
%attr(755,root,root) %{_libdir}/libPocoDataSQLited.so.17
%attr(755,root,root) %{_libdir}/libPocoDatad.so.17
%attr(755,root,root) %{_libdir}/libPocoFoundation.so.17
%attr(755,root,root) %{_libdir}/libPocoFoundationd.so.17
%attr(755,root,root) %{_libdir}/libPocoNet.so.17
%attr(755,root,root) %{_libdir}/libPocoNetSSL.so
%attr(755,root,root) %{_libdir}/libPocoNetSSL.so.17
%attr(755,root,root) %{_libdir}/libPocoNetSSLd.so
%attr(755,root,root) %{_libdir}/libPocoNetSSLd.so.17
%attr(755,root,root) %{_libdir}/libPocoNetd.so.17
%attr(755,root,root) %{_libdir}/libPocoUtil.so.17
%attr(755,root,root) %{_libdir}/libPocoUtild.so.17
%attr(755,root,root) %{_libdir}/libPocoXML.so.17
%attr(755,root,root) %{_libdir}/libPocoXMLd.so.17
%attr(755,root,root) %{_libdir}/libPocoZip.so.17
%attr(755,root,root) %{_libdir}/libPocoZipd.so.17

%files devel
%defattr(644,root,root,755)
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
%{_libdir}/libPocoNetd.so
%{_libdir}/libPocoUtil.so
%{_libdir}/libPocoUtild.so
%{_libdir}/libPocoXML.so
%{_libdir}/libPocoXMLd.so
%{_libdir}/libPocoZip.so
%{_libdir}/libPocoZipd.so
%{_includedir}/Poco
