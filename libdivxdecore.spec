Summary:	OpenDivX - MPEG-4 implementation
Summary(pl):	OpenDivX - implementacja dekodera MPEG-4
Name:		libdivxdecore
Version:	0.4.7
Release:	5
License:	DivX Open License
Group:		Libraries
Source0:	http://download2.projectmayo.com/dnload/divx4linux/xmps/%{name}-%{version}.tar.gz
URL:		http://www.projectmayo.com/projects/detail.php?projectId=4
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenDivX is a implementation of MPEG-4 Video tools as specified in
ISO/IEC 14496-2 standard.

%description -l pl
OpenDivX jest implementacj± MPEG-4 okre¶lonego w miêdzynarodowej
normie ISO/IEC 14496-2.

%package devel
Summary:	Header files and development documentation for libdivxdecore
Summary(pl):	Pliki nag³ówkowe i dokumentacja do libdivxdecore
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files and development documentation for libdivxdecore.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja do libdivxdecore.

%package static
Summary:	libdivxdecore static library
Summary(pl):	Statyczna biblioteka libdivxdecore
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
libdivxdecore static library.

%description static -l pl
Biblioteka statyczna libdivxdecore.

%prep
%setup -q

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

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

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
