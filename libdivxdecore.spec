Summary:	OpenDivX - MPEG-4 implementation
Name:		libdivxdecore
Version:	0.4.7
Release:	1
Copyright:	GPL
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	http://download.projectmayo.com/dnload/divx4linux/xmps/%{name}-%{version}.tar.gz
URL:		http://www.projectmayo.com/linux/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenDivX is a implementation of MPEG-4 Video tools as specified in 
ISO/IEC 14496-2 standard.

%description -l pl
OpenDivX jest implementacj± MPEG-4 okre¶lonego w miêdzynarodowej normie
ISO/IEC 14496-2.

%package devel
Summary:	Header files and development documentation for libdivxdecore
Summary(pl):	Pliki nag³ówkowe i dokumentacja do libdivxdecore
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files and development documentation for libdivxdecore.

%description -l pl devel
Pliki nag³ówkowe i dokumentacja do libdivxdecore.

%package static
Summary:	libdivxdecore static library
Summary(pl):	Statyczna biblioteka libdivxdecore
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
libdivxdecore static library.

%description -l pl static
Biblioteka statyczna libdivxdecore.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so

%files devel
%defattr(644,root,root,755)
%doc *.gz
%{_libdir}/*.la
%{_includedir}/divx

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
