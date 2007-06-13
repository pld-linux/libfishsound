Summary:	A library to encode and decode Vorbis or Speex compressed audio
Summary(pl.UTF-8):	Biblioteka do kodowania i dekodowania dźwięku w formacie Speex lub Vorbis
Name:		libfishsound
Version:	0.8.0
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://annodex.net/software/libfishsound/download/%{name}-%{version}.tar.gz
# Source0-md5:	c21539b2c0b20c458ec3eb3f92fe3f26
URL:		http://annodex.net/software/libfishsound/index.html
BuildRequires:	liboggz-devel >= 0.5.40
BuildRequires:	libsndfile-devel >= 1.0.0
BuildRequires:	libvorbis-devel >= 1:1.0
BuildRequires:	pkgconfig
BuildRequires:	speex-devel >= 1:1.1.6
Requires:	libvorbis-devel >= 1:1.0
Requires:	speex-devel >= 1:1.1.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libfishsound provides a simple programming interface for decoding and
encoding audio data using Xiph.Org codecs (Vorbis and Speex).

libfishsound by itself is designed to handle raw codec streams from a
lower level layer such as UDP datagrams. When these codecs are used in
files, they are commonly encapsulated in Ogg to produce Ogg Vorbis
and Speex files.

%description -l pl.UTF-8
libfishsound udostępnia prosty interfejs programistyczny do
dekodowania i kodowania plików dźwiękowych przy użyciu kodeków
Xiph.Org (Vorbis i Speex).

Sama biblioteka libfishsound jest przeznaczona do obsługi surowych
strumieni kodeków z niższej warstwy takiej jak datagramy UDP. W
przypadku gdy kodeki te są użyte w plikach, są zwykle obudowane w Ogg,
tworząc pliki Ogg Vorbis i Ogg Speex.

%package devel
Summary:	Header files for libfishsound library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libfishsound
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libvorbis-devel >= 1:1.0
Requires:	speex-devel >= 1:1.1.6

%description devel
Header files for libfishsound library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libfishsound.

%package static
Summary:	Static libfishsound library
Summary(pl.UTF-8):	Statyczna biblioteka libfishsound
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libfishsound library.

%description static -l pl.UTF-8
Statyczna biblioteka libfishsound.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	docdir=$RPM_BUILD_ROOT%{_docdir}/libfishsound

rm -rf $RPM_BUILD_ROOT%{_docdir}/libfishsound

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libfishsound.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/libfishsound/html/*
%attr(755,root,root) %{_libdir}/libfishsound.so
%{_libdir}/libfishsound.la
%{_includedir}/fishsound
%{_pkgconfigdir}/fishsound.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libfishsound.a
