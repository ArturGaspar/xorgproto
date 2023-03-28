Name:       xorgproto
Version:    2024.1
Release:    1%{?dist}
Summary:    X Window System Unified Protocol
License:    MIT
URL:        https://gitlab.freedesktop.org/xorg/proto/%{name}
Source0:    %{name}-%{version}.tar.bz2
BuildArch:  noarch
BuildRequires:  meson

%description
Base package for %{name}.

%package devel
Summary:    X Window System Unified Protocol

%description devel
This package provides the headers and specification documents defining
the core protocol and (many) extensions for the X Window System. The
extensions are those common among servers descended from X11R7. It
also includes a number of headers that aren't purely protocol related,
but are depended upon by many other X Window System packages to provide
common definitions and porting layer.

%package doc
Summary:    Documentation for %{name}

%description doc
%{summary}.

%prep
%autosetup -n %{name}-%{version}/upstream

%build
%meson
%meson_build

%install
%meson_install

%files devel
%license COPYING-*
%{_includedir}/GL
%{_includedir}/X11/dri
%{_includedir}/X11/extensions
%{_includedir}/X11/fonts
%{_includedir}/X11/*.h
%{_datadir}/pkgconfig/*.pc

%files doc
%license COPYING-*
%{_docdir}/xorgproto
