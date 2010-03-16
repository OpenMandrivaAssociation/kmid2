%define realname kmid

Name:		kmid2
Version:	2.2.2
Release:	%mkrel 4
Summary:	A MIDI/karaoke player for KDE
Group:		Sound
# GPLv2+ for the code, CC-BY-SA for the examples
License:	GPLv2+ and CC-BY-SA
URL:		http://userbase.kde.org/KMid2
Source0:	http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/kmid-%{version}.tar.bz2
Patch1:		kmid2-2.2.2-use-timidity-pulse.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	kdelibs4-devel
BuildRequires:	libalsa-devel
BuildRequires:	drumstick-devel >= 0.3.0
BuildRequires:	desktop-file-utils
Requires:	kdelibs4-core >= 4.3.0
Requires:	oxygen-icon-theme
Requires:	drumstick >= 0.2.99
Requires:	TiMidity++

%description
KMid2 is a MIDI/karaoke file player, with configurable midi mapper, real
Session Management, drag & drop, customizable fonts, etc. It has a very
nice interface which let you easily follow the tune while changing the
color of the lyrics.
It supports output through external synthesizers, AWE, FM and GUS cards.
It also has a keyboard view to see the notes played by each instrument.

%files -f %{realname}.lang
%defattr(-,root,root,-)
%doc ChangeLog README TODO
%{_kde_bindir}/%{realname}
%{_kde_appsdir}/%{realname}/*
%{_kde_applicationsdir}/%{realname}.desktop
%{_kde_datadir}/config.kcfg/%{realname}.kcfg
%{_kde_services}/*
%{_kde_servicetypes}/*
%{_kde_iconsdir}/hicolor/*/*/*
%{_kde_libdir}/kde4/*

#-------------------------------------------------------------------------------

%prep
%setup -qn %{realname}-%{version}
# (ahmad) use timidity by default. Also pulseaudio by default since it's enabled
# by default in mdv installs
%patch1 -p0

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}

%makeinstall_std -C build

# fix the .desktop file
desktop-file-install \
		--vendor="" \
		--add-category="AudioVideo" \
		--add-category="Audio" \
		--remove-category="Music" \
		--dir %{buildroot}%{_kde_applicationsdir} %{buildroot}%{_kde_applicationsdir}/%{realname}.desktop

%find_lang %{realname} --with-html

%clean
rm -rf %{buildroot}
