%global commit0 2cffda6222f07cd7d0aa4627a06fa99b05a3956d
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver git%{shortcommit0}

Name: libtgvoip
Version: 2.4.4
Release: 7%{?gver}%{dist}

License: Public Domain and BSD
Url: https://github.com/telegramdesktop/libtgvoip
Summary: VoIP library for Telegram clients
Source0: https://github.com/telegramdesktop/libtgvoip/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz

BuildRequires: automake
BuildRequires: autoconf
BuildRequires: gcc-c++
BuildRequires: libtool
BuildRequires: gcc
BuildRequires: pulseaudio-libs-devel
BuildRequires: alsa-lib-devel
BuildRequires: openssl-devel
BuildRequires: json11-devel
BuildRequires: opus-devel
BuildRequires: tg_owt-devel
BuildRequires: pkgconfig(webrtc-audio-processing)

%description
Provides VoIP library for Telegram clients.

%package devel
Summary: Development files for libtgvoip
Requires: %{name} = %{version}-%{release}

%description devel
evelopment VoIP library for Telegram clients

%prep
%autosetup -n %{name}-%{commit0} 

%build
autoreconf --force --install
export CPPFLAGS="-I/usr/include/tg_owt -I/usr/include/tg_owt/third_party/abseil-cpp"
./configure --prefix=%{_prefix} --libdir=%{_libdir} --disable-dsp --disable-static
%make_build 

%install
%make_install 
rm -f %{buildroot}/%{_libdir}/*.la

%files
%license UNLICENSE
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/tgvoip/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/tgvoip.pc

%changelog
* Fri Dec 17 2021 Unitedrpms Project <unitedrpms AT protonmail DOT com> 2.4.4-7.git2cffda6
- Inital build
