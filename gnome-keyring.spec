#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v21
# autospec commit: fbbd4e3
#
Name     : gnome-keyring
Version  : 48.0
Release  : 27
URL      : https://download.gnome.org/sources/gnome-keyring/48/gnome-keyring-48.0.tar.xz
Source0  : https://download.gnome.org/sources/gnome-keyring/48/gnome-keyring-48.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: gnome-keyring-bin = %{version}-%{release}
Requires: gnome-keyring-data = %{version}-%{release}
Requires: gnome-keyring-lib = %{version}-%{release}
Requires: gnome-keyring-license = %{version}-%{release}
Requires: gnome-keyring-locales = %{version}-%{release}
Requires: gnome-keyring-man = %{version}-%{release}
Requires: gnome-keyring-services = %{version}-%{release}
BuildRequires : Linux-PAM-dev
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : dbus
BuildRequires : docbook-xml
BuildRequires : glibc-staticdev
BuildRequires : libcap-ng-dev
BuildRequires : libgcrypt-dev
BuildRequires : libgpg-error-dev
BuildRequires : libxslt-bin
BuildRequires : openssh
BuildRequires : pkgconfig(gck-1)
BuildRequires : valgrind
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: backport-off-by-one.patch

%description
gnome-keyring is a program that keep password and other secrets for
users. It is run as a daemon in the session, similar to ssh-agent, and
other applications locate it via an environment variable or a D-Bus.

%package bin
Summary: bin components for the gnome-keyring package.
Group: Binaries
Requires: gnome-keyring-data = %{version}-%{release}
Requires: gnome-keyring-license = %{version}-%{release}
Requires: gnome-keyring-services = %{version}-%{release}

%description bin
bin components for the gnome-keyring package.


%package data
Summary: data components for the gnome-keyring package.
Group: Data

%description data
data components for the gnome-keyring package.


%package lib
Summary: lib components for the gnome-keyring package.
Group: Libraries
Requires: gnome-keyring-data = %{version}-%{release}
Requires: gnome-keyring-license = %{version}-%{release}

%description lib
lib components for the gnome-keyring package.


%package license
Summary: license components for the gnome-keyring package.
Group: Default

%description license
license components for the gnome-keyring package.


%package locales
Summary: locales components for the gnome-keyring package.
Group: Default

%description locales
locales components for the gnome-keyring package.


%package man
Summary: man components for the gnome-keyring package.
Group: Default

%description man
man components for the gnome-keyring package.


%package services
Summary: services components for the gnome-keyring package.
Group: Systemd services
Requires: systemd

%description services
services components for the gnome-keyring package.


%prep
%setup -q -n gnome-keyring-48.0
cd %{_builddir}/gnome-keyring-48.0
%patch -P 1 -p1
pushd ..
cp -a gnome-keyring-48.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1742910820
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
dbus-run-session make %{?_smp_mflags} check || :

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-keyring
cp %{_builddir}/gnome-keyring-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gnome-keyring/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/gnome-keyring-%{version}/COPYING.LIB %{buildroot}/usr/share/package-licenses/gnome-keyring/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gnome-keyring
## install_append content
mkdir -p %{buildroot}/usr/share/xdg/autostart
cp %{buildroot}/etc/xdg/autostart/* %{buildroot}/usr/share/xdg/autostart/
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/gnome-keyring-3
/V3/usr/bin/gnome-keyring-daemon
/usr/bin/gnome-keyring
/usr/bin/gnome-keyring-3
/usr/bin/gnome-keyring-daemon

%files data
%defattr(-,root,root,-)
/usr/share/GConf/gsettings/org.gnome.crypto.cache.convert
/usr/share/dbus-1/services/org.freedesktop.impl.portal.Secret.service
/usr/share/dbus-1/services/org.freedesktop.secrets.service
/usr/share/dbus-1/services/org.gnome.keyring.service
/usr/share/glib-2.0/schemas/org.gnome.crypto.cache.gschema.xml
/usr/share/p11-kit/modules/gnome-keyring.module
/usr/share/xdg-desktop-portal/portals/gnome-keyring.portal
/usr/share/xdg/autostart/gnome-keyring-pkcs11.desktop
/usr/share/xdg/autostart/gnome-keyring-secrets.desktop

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/gnome-keyring/devel/gkm-gnome2-store-standalone.so
/V3/usr/lib64/gnome-keyring/devel/gkm-secret-store-standalone.so
/V3/usr/lib64/gnome-keyring/devel/gkm-ssh-store-standalone.so
/V3/usr/lib64/gnome-keyring/devel/gkm-xdg-store-standalone.so
/V3/usr/lib64/pkcs11/gnome-keyring-pkcs11.so
/V3/usr/lib64/security/pam_gnome_keyring.so
/usr/lib64/gnome-keyring/devel/gkm-gnome2-store-standalone.so
/usr/lib64/gnome-keyring/devel/gkm-secret-store-standalone.so
/usr/lib64/gnome-keyring/devel/gkm-ssh-store-standalone.so
/usr/lib64/gnome-keyring/devel/gkm-xdg-store-standalone.so
/usr/lib64/pkcs11/gnome-keyring-pkcs11.so
/usr/lib64/security/pam_gnome_keyring.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnome-keyring/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/gnome-keyring/4cc77b90af91e615a64ae04893fdffa7939db84c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/gnome-keyring-3.1
/usr/share/man/man1/gnome-keyring-daemon.1
/usr/share/man/man1/gnome-keyring.1

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/gnome-keyring-daemon.service
/usr/lib/systemd/user/gnome-keyring-daemon.socket

%files locales -f gnome-keyring.lang
%defattr(-,root,root,-)

