# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	OpenDivX - MPEG-4 implementation
Summary(pl.UTF-8):	OpenDivX - implementacja dekodera MPEG-4
Name:		libdivxdecore
Version:	0.4.7
Release:	6
License:	DivX Open License
Group:		Libraries
Source0:	http://download2.projectmayo.com/dnload/divx4linux/xmps/%{name}-%{version}.tar.gz
# Source0-md5:	0defab7d519308aacfb1a0c1448341a1
URL:		http://www.projectmayo.com/projects/detail.php?projectId=4
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenDivX is a implementation of MPEG-4 Video tools as specified in
ISO/IEC 14496-2 standard.

%description -l pl.UTF-8
OpenDivX jest implementacją MPEG-4 określonego w międzynarodowej
normie ISO/IEC 14496-2.

%package devel
Summary:	Header files and development documentation for libdivxdecore
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja do libdivxdecore
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and development documentation for libdivxdecore.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do libdivxdecore.

%package static
Summary:	libdivxdecore static library
Summary(pl.UTF-8):	Statyczna biblioteka libdivxdecore
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
libdivxdecore static library.

%description static -l pl.UTF-8
Biblioteka statyczna libdivxdecore.

%prep
%setup -q

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING README
%attr(755,root,root) %{_libdir}/*.so

%files devel
%defattr(644,root,root,755)
%{_libdir}/*.la
%{_includedir}/divx

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
%endif
