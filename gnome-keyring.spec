#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-keyring
Version  : 40.0
Release  : 17
URL      : https://download.gnome.org/sources/gnome-keyring/40/gnome-keyring-40.0.tar.xz
Source0  : https://download.gnome.org/sources/gnome-keyring/40/gnome-keyring-40.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: gnome-keyring-bin = %{version}-%{release}
Requires: gnome-keyring-data = %{version}-%{release}
Requires: gnome-keyring-lib = %{version}-%{release}
Requires: gnome-keyring-license = %{version}-%{release}
Requires: gnome-keyring-locales = %{version}-%{release}
Requires: gnome-keyring-man = %{version}-%{release}
BuildRequires : Linux-PAM-dev
BuildRequires : buildreq-gnome
BuildRequires : docbook-xml
BuildRequires : gettext
BuildRequires : glibc-staticdev
BuildRequires : libcap-ng-dev
BuildRequires : libgcrypt-dev
BuildRequires : libgpg-error-dev
BuildRequires : libxslt-bin
BuildRequires : openssh
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gck-1)
BuildRequires : pkgconfig(gcr-3)
BuildRequires : pkgconfig(gcr-base-3)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gmodule-no-export-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : valgrind

%description
gnome-keyring is a program that keep password and other secrets for
users. It is run as a daemon in the session, similar to ssh-agent, and
other applications locate it via an environment variable or a D-Bus.

%package bin
Summary: bin components for the gnome-keyring package.
Group: Binaries
Requires: gnome-keyring-data = %{version}-%{release}
Requires: gnome-keyring-license = %{version}-%{release}

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


%prep
%setup -q -n gnome-keyring-40.0
cd %{_builddir}/gnome-keyring-40.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1619050091
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1619050091
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-keyring
cp %{_builddir}/gnome-keyring-40.0/COPYING %{buildroot}/usr/share/package-licenses/gnome-keyring/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/gnome-keyring-40.0/COPYING.LIB %{buildroot}/usr/share/package-licenses/gnome-keyring/01a6b4bf79aca9b556822601186afab86e8c4fbf
%make_install
%find_lang gnome-keyring
## install_append content
mkdir -p %{buildroot}/usr/share/xdg/autostart
cp %{buildroot}/etc/xdg/autostart/* %{buildroot}/usr/share/xdg/autostart/
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
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
/usr/share/xdg/autostart/gnome-keyring-ssh.desktop

%files lib
%defattr(-,root,root,-)
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

%files locales -f gnome-keyring.lang
%defattr(-,root,root,-)

