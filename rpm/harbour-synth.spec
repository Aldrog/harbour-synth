# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       harbour-synth

# >> macros
# << macros

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}
Summary:    A piano synthesizer
Version:    0.1
Release:    1
Group:      Qt/Qt
License:    LICENSE
URL:        http://example.org/
Source0:    %{name}-%{version}.tar.bz2
Source100:  harbour-synth.yaml
Requires:   sailfishsilica-qt5 >= 0.10.9
BuildRequires:  pkgconfig(sailfishapp) >= 1.0.2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(audioresource)
BuildRequires:  cmake
BuildRequires:  readline-devel
BuildRequires:  desktop-file-utils

%description
Short description of my Sailfish OS Application


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
#rm -rf fluidsynth
mkdir -p fluidsynth
cd fluidsynth
echo "%{_datadir}"
cmake ../../%{name}/fluidsynth -DCMAKE_INSTALL_PREFIX:PATH=%{_datadir}/%{name}
%qtc_make %{?_smp_mflags}
cd ..
mkdir -p $PWD/tempdest
DESTDIR=$PWD/tempdest make -C fluidsynth install
# << build pre

%qtc_qmake5 

%qtc_make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
DESTDIR=%{buildroot} make -C fluidsynth install
mkdir -p %{buildroot}%{_datadir}/%{name}/soundfonts/
install -p ../%{name}/soundfonts/FluidR3_GM.sf2 %{buildroot}%{_datadir}/%{name}/soundfonts/
# << install pre
%qmake5_install

# >> install post
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%{_bindir}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
# >> files
# << files
