Summary:	A library to encode and decode Vorbis or Speex compressed audio
Summary(pl.UTF-8):	Biblioteka do kodowania i dekodowania dźwięku w formacie Speex lub Vorbis
Name:		libfishsound
Version:	1.0.0
Release:	3
License:	BSD
Group:		Libraries
Source0:	http://downloads.xiph.org/releases/libfishsound/%{name}-%{version}.tar.gz
# Source0-md5:	02c5c7b361a35c9da3cf311d68800dab
URL:		http://www.xiph.org/fishsound/
BuildRequires:	flac-devel >= 1.1.3
BuildRequires:	liboggz-devel >= 0.5.40
BuildRequires:	libsndfile-devel >= 1.0.0
BuildRequires:	libvorbis-devel >= 1:1.0
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	speex-devel >= 1:1.1.6
Requires:	libvorbis >= 1:1.0
Requires:	speex >= 1:1.1.6
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
Requires:	flac-devel >= 1.1.3
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

%package apidocs
Summary:	API documentation for libfishsound library
Summary(pl.UTF-8):	Dokumentacja API biblioteki libfishsound
Group:		Documentation
BuildArch:	noarch

%description apidocs
API documentation for libfishsound library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libfishsound.

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

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libfishsound.la

rm -rf $RPM_BUILD_ROOT%{_docdir}/libfishsound

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libfishsound.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libfishsound.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libfishsound.so
%{_includedir}/fishsound
%{_pkgconfigdir}/fishsound.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libfishsound.a

%files apidocs
%defattr(644,root,root,755)
%doc doc/libfishsound/html/*
