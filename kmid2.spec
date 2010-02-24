Name:		kmid2
Version:	0.2.1
Release:	%mkrel 1
Summary:	A MIDI/karaoke player for KDE
Group:		Sound
# GPLv2+ for the code, CC-BY-SA for the examples
License:	GPLv2+ and CC-BY-SA
URL:		http://userbase.kde.org/KMid2
Source0:	http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}.tar.bz2
# (from Fedora) relax drumstick version check in CMakeLists.txt as 0.3 is not out
# yet 0.2.99-0.3.20100208svn has all the fixes and API additions in the bundled copy
# svn diff -r 1085734:1085733 svn://anonsvn.kde.org/home/kde/trunk/playground/multimedia/kmid2
Patch0:		kmid2-0.2.1-drumstick-version.patch
Patch1:		kmid2-0.2.1-use-timidity-pulse.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	kdelibs4-devel
BuildRequires:	libalsa-devel
BuildRequires:	drumstick-devel >= 0.2.99
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


%prep
%setup -q
# make sure bundled drumstick isn't used
rm -rf drumstick
%patch0 -p0 -b .drumstick-version

# (ahmad) use timidity by default. Also pulseaudio by default since it's enabled
# by default in mdv installs
%patch1 -p0

%build
%cmake_kde4
%make


%install
rm -rf %{buildroot}

%makeinstall_std -C build

%find_lang %{name}


%clean
rm -rf %{buildroot}


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc ChangeLog README TODO
%{_kde_bindir}/%{name}
%{_kde_appsdir}/%{name}/*
%{_kde_applicationsdir}/%{name}.desktop
%{_kde_datadir}/config.kcfg/*
%{_kde_services}/*
%{_kde_servicetypes}/*
%{_kde_iconsdir}/hicolor/*/*/*
%{_kde_libdir}/kde4/*
%{_kde_docdir}/HTML/*/*/*
