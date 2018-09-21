#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-keyring
Version  : 3.28.2
Release  : 9
URL      : https://download.gnome.org/sources/gnome-keyring/3.28/gnome-keyring-3.28.2.tar.xz
Source0  : https://download.gnome.org/sources/gnome-keyring/3.28/gnome-keyring-3.28.2.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: gnome-keyring-bin
Requires: gnome-keyring-lib
Requires: gnome-keyring-data
Requires: gnome-keyring-locales
Requires: gnome-keyring-doc
BuildRequires : Linux-PAM-dev
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
Requires: gnome-keyring-data

%description bin
bin components for the gnome-keyring package.


%package data
Summary: data components for the gnome-keyring package.
Group: Data

%description data
data components for the gnome-keyring package.


%package doc
Summary: doc components for the gnome-keyring package.
Group: Documentation

%description doc
doc components for the gnome-keyring package.


%package lib
Summary: lib components for the gnome-keyring package.
Group: Libraries
Requires: gnome-keyring-data

%description lib
lib components for the gnome-keyring package.


%package locales
Summary: locales components for the gnome-keyring package.
Group: Default

%description locales
locales components for the gnome-keyring package.


%prep
%setup -q -n gnome-keyring-3.28.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1525704391
%configure --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1525704391
rm -rf %{buildroot}
%make_install
%find_lang gnome-keyring

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
/usr/share/dbus-1/services/org.freedesktop.secrets.service
/usr/share/dbus-1/services/org.gnome.keyring.service
/usr/share/glib-2.0/schemas/org.gnome.crypto.cache.gschema.xml

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/gnome-keyring/devel/gkm-gnome2-store-standalone.so
/usr/lib64/gnome-keyring/devel/gkm-secret-store-standalone.so
/usr/lib64/gnome-keyring/devel/gkm-ssh-store-standalone.so
/usr/lib64/gnome-keyring/devel/gkm-xdg-store-standalone.so
/usr/lib64/pkcs11/gnome-keyring-pkcs11.so
/usr/lib64/security/pam_gnome_keyring.so

%files locales -f gnome-keyring.lang
%defattr(-,root,root,-)

