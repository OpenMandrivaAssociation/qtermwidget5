%define major 1
%define oldlibname %mklibname qtermwidget5 1
%define libname %mklibname qtermwidget5
%define devname %mklibname qtermwidget5 -d
%define olddevname %mklibname qtermwidget -d

Summary:	Qt terminal widget
Name:		qtermwidget5
Version:	1.4.0
Release:	1
License:	GPLv2+
Group:		Development/Other
Url:		https://github.com/lxqt/qtermwidget
Source0:	https://github.com/lxqt/qtermwidget/releases/download/%{version}/qtermwidget-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	qmake5
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(Qt5LinguistTools)
BuildRequires:	cmake(lxqt-build-tools)

%description
QTermWidget is an open source project based on KDE4 Konsole application.
The main goal of this project is to provide unicode-enabled,
embeddable Qt widget for using as a built-in console (or terminal
emulation widget).

%files
%{_datadir}/%{name}/

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Qt terminal widget - shared library
Group:		System/Libraries
Requires:	%{name}
%rename %{oldlibname}

%description -n %{libname}
This package provides shared library for Qt4 terminal widget.

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Qt terminal widget - devel package
Group:		Development/Other
Requires:	%{libname} = %{EVRD}
Obsoletes:	%{name}-devel < 0.4.0-1
Provides:	%{name}-devel = %{EVRD}
%rename %{olddevname}

%description -n %{devname}
This package provides headers files for qtermwidget development.

%files -n %{devname}
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n qtermwidget-%{version}
%cmake_qt5 -DUSE_QT5:BOOL=ON -DPULL_TRANSLATIONS=NO -DBUILD_DESIGNER_PLUGIN:BOOL=OFF -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
